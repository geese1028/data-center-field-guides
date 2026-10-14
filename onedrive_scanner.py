#!/usr/bin/env python3
"""
OneDrive 云端资料扫描器
通过 Microsoft Graph API 遍历 OneDrive 云端内容，输出资料盘点报告。
使用 Device Code Flow 进行 OAuth 认证（无需本地 Web 服务器）。
"""

import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

import msal
import requests

# ============================================================
# 配置区域
# ============================================================
# 用户需要在 Azure Portal 注册应用后填入 client_id
# 如果设置了环境变量 ONEDRIVE_CLIENT_ID，优先使用环境变量
CLIENT_ID = os.environ.get("ONEDRIVE_CLIENT_ID", "")

# 支持个人账户 + 工作/学校账户
AUTHORITY = "https://login.microsoftonline.com/consumers"  # 个人账户
# 如果是企业/学校账户，改为：
# AUTHORITY = "https://login.microsoftonline.com/common"

SCOPES = ["Files.Read"]
GRAPH_API = "https://graph.microsoft.com/v1.0"
TOKEN_CACHE_FILE = os.path.join(os.path.dirname(__file__), ".onedrive_token_cache.json")
REPORT_FILE = os.path.join(os.path.dirname(__file__), "onedrive_inventory.json")
REPORT_MD_FILE = os.path.join(os.path.dirname(__file__), "onedrive_inventory.md")

# 扫描配置
MAX_DEPTH = 4          # 最大递归深度
PAGE_SIZE = 200        # 每页返回条目数
REQUEST_DELAY = 0.1    # API 请求间隔（秒），避免限流


# ============================================================
# 工具函数
# ============================================================
def format_size(size_bytes):
    """将字节数格式化为人类可读的大小。"""
    if size_bytes is None:
        return "unknown"
    for unit in ["B", "KB", "MB", "GB"]:
        if abs(size_bytes) < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def get_extension(name):
    """提取文件扩展名（小写）。"""
    if "." in name:
        return "." + name.rsplit(".", 1)[1].lower()
    return "(no ext)"


# ============================================================
# 认证模块
# ============================================================
def build_msal_app():
    """构建 MSAL 公共客户端应用，支持令牌缓存持久化。"""
    cache = msal.SerializableTokenCache()
    if os.path.exists(TOKEN_CACHE_FILE):
        with open(TOKEN_CACHE_FILE, "r") as f:
            cache.deserialize(f.read())

    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        token_cache=cache,
    )
    return app, cache


def save_cache(cache):
    """将令牌缓存写入磁盘。"""
    if cache.has_state_changed:
        with open(TOKEN_CACHE_FILE, "w") as f:
            f.write(cache.serialize())


def authenticate():
    """
    执行 OAuth 认证，返回 access_token。
    优先使用缓存的令牌，过期则自动刷新，无缓存则启动 Device Code Flow。
    """
    app, cache = build_msal_app()

    # 尝试从缓存获取令牌
    accounts = app.get_accounts()
    if accounts:
        result = app.acquire_token_silent(SCOPES, account=accounts[0])
        if result and "access_token" in result:
            print("✅ 使用缓存令牌登录成功。")
            save_cache(cache)
            return result["access_token"]

    # 启动 Device Code Flow
    flow = app.initiate_device_flow(scopes=SCOPES)
    if "user_code" not in flow:
        print(f"❌ 无法启动设备码流程: {flow.get('error_description', 'unknown error')}")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("🔐 OneDrive 授权登录")
    print("=" * 60)
    print(f"\n请在浏览器中打开: {flow['verification_uri']}")
    print(f"输入设备码: {flow['user_code']}")
    print(f"\n(授权码将在 {flow.get('expires_in', 900)} 秒后过期)")
    print("等待你完成浏览器授权...\n")

    result = app.acquire_token_by_device_flow(flow)

    if "access_token" not in result:
        print(f"❌ 认证失败: {result.get('error_description', 'unknown error')}")
        sys.exit(1)

    print("✅ 登录成功！")
    save_cache(cache)
    return result["access_token"]


# ============================================================
# Graph API 扫描模块
# ============================================================
def graph_get(token, url, params=None):
    """发送 GET 请求到 Microsoft Graph API，自动处理分页和限流。"""
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers, params=params, timeout=30)

    if resp.status_code == 429:
        retry_after = int(resp.headers.get("Retry-After", 5))
        print(f"  ⏳ 被限流，等待 {retry_after} 秒...")
        time.sleep(retry_after)
        return graph_get(token, url, params)

    if resp.status_code != 200:
        print(f"  ⚠️ API 错误 {resp.status_code}: {resp.text[:200]}")
        return None

    return resp.json()


def list_children(token, item_id=None, path=None):
    """列出指定目录下的所有子项（自动处理分页）。"""
    if item_id:
        url = f"{GRAPH_API}/me/drive/items/{item_id}/children"
    elif path:
        url = f"{GRAPH_API}/me/drive/root:/{path}:/children"
    else:
        url = f"{GRAPH_API}/me/drive/root/children"

    all_items = []
    params = {"$top": PAGE_SIZE}

    while url:
        data = graph_get(token, url, params)
        if not data:
            break
        all_items.extend(data.get("value", []))
        url = data.get("@odata.nextLink")
        params = None  # nextLink 已经包含参数
        time.sleep(REQUEST_DELAY)

    return all_items


def scan_directory(token, item_id=None, path="", depth=0, stats=None):
    """
    递归扫描 OneDrive 目录结构。
    返回目录树结构和统计信息。
    """
    if stats is None:
        stats = {
            "total_files": 0,
            "total_folders": 0,
            "total_size": 0,
            "extensions": defaultdict(lambda: {"count": 0, "size": 0}),
            "large_files": [],  # > 1MB 的文件
        }

    indent = "  " * depth
    children = list_children(token, item_id=item_id)
    tree = []

    for item in children:
        name = item.get("name", "?")
        size = item.get("size", 0)
        is_folder = "folder" in item

        if is_folder:
            child_count = item["folder"].get("childCount", 0)
            stats["total_folders"] += 1
            print(f"{indent}📁 {name}/ ({child_count} items)")

            node = {
                "name": name,
                "type": "folder",
                "id": item["id"],
                "child_count": child_count,
                "path": f"{path}/{name}" if path else name,
                "children": [],
            }

            # 递归扫描子目录
            if depth < MAX_DEPTH and child_count > 0:
                sub_tree, stats = scan_directory(
                    token,
                    item_id=item["id"],
                    path=node["path"],
                    depth=depth + 1,
                    stats=stats,
                )
                node["children"] = sub_tree

            tree.append(node)
        else:
            ext = get_extension(name)
            stats["total_files"] += 1
            stats["total_size"] += size
            stats["extensions"][ext]["count"] += 1
            stats["extensions"][ext]["size"] += size

            if size > 1_000_000:  # > 1MB
                stats["large_files"].append({
                    "name": name,
                    "path": f"{path}/{name}" if path else name,
                    "size": size,
                    "size_human": format_size(size),
                })

            if depth <= 2:  # 只在浅层打印文件
                print(f"{indent}📄 {name} ({format_size(size)})")

            tree.append({
                "name": name,
                "type": "file",
                "size": size,
                "extension": ext,
                "path": f"{path}/{name}" if path else name,
            })

    return tree, stats


# ============================================================
# 报告生成模块
# ============================================================
def generate_report(tree, stats):
    """生成 Markdown 格式的盘点报告。"""
    lines = [
        "# OneDrive 云端资料盘点报告",
        "",
        f"扫描时间: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 总体统计",
        "",
        f"| 指标 | 数值 |",
        f"|------|------|",
        f"| 文件总数 | {stats['total_files']} |",
        f"| 文件夹总数 | {stats['total_folders']} |",
        f"| 总大小 | {format_size(stats['total_size'])} |",
        "",
        "## 文件类型分布",
        "",
        "| 扩展名 | 数量 | 大小 |",
        "|--------|------|------|",
    ]

    # 按数量排序
    sorted_exts = sorted(
        stats["extensions"].items(),
        key=lambda x: x[1]["count"],
        reverse=True,
    )
    for ext, info in sorted_exts:
        lines.append(f"| `{ext}` | {info['count']} | {format_size(info['size'])} |")

    lines.extend(["", "## 大文件列表 (> 1MB)", ""])
    if stats["large_files"]:
        lines.append("| 文件 | 路径 | 大小 |")
        lines.append("|------|------|------|")
        for f in sorted(stats["large_files"], key=lambda x: x["size"], reverse=True)[:50]:
            lines.append(f"| {f['name']} | {f['path']} | {f['size_human']} |")
    else:
        lines.append("无大文件。")

    lines.extend(["", "## 顶层目录结构", ""])

    def render_tree(nodes, indent=0):
        for node in nodes:
            prefix = "  " * indent
            if node["type"] == "folder":
                child_info = f" ({node.get('child_count', '?')} items)"
                lines.append(f"{prefix}- 📁 **{node['name']}/**{child_info}")
                if node.get("children"):
                    render_tree(node["children"], indent + 1)
            # 只在前两层显示文件
            elif indent <= 1:
                lines.append(f"{prefix}- 📄 {node['name']} ({format_size(node.get('size', 0))})")

    render_tree(tree)

    return "\n".join(lines)


# ============================================================
# 主入口
# ============================================================
def main():
    global CLIENT_ID, AUTHORITY

    # 检查 client_id
    if not CLIENT_ID:
        print("❌ 尚未配置 Client ID。")
        print("")
        print("请按以下步骤在 Azure Portal 注册应用：")
        print("1. 打开 https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade")
        print("2. 点击 '+ New registration'")
        print("3. Name: 填 'OneDrive Scanner' (任意名称)")
        print("4. Supported account types: 选 'Personal Microsoft accounts only'")
        print("   (如果是企业账户则选 'Accounts in any organizational directory and personal')")
        print("5. Redirect URI: 留空或选 'Public client/native' 填 http://localhost")
        print("6. 点击 Register")
        print("7. 复制 'Application (client) ID'")
        print("8. 左侧菜单 'Authentication' > 底部 'Allow public client flows' 设为 Yes > Save")
        print("9. 左侧菜单 'API permissions' > Add a permission > Microsoft Graph > Delegated")
        print("   > 搜索 'Files.Read' > 勾选 > Add permissions")
        print("")
        CLIENT_ID = input("请粘贴你的 Application (client) ID: ").strip()
        if not CLIENT_ID:
            print("未输入 Client ID，退出。")
            sys.exit(1)

    # 询问账户类型
    if "--enterprise" in sys.argv:
        AUTHORITY = "https://login.microsoftonline.com/common"
        print("📌 使用企业/学校账户模式。")
    else:
        print("📌 使用个人 Microsoft 账户模式。")
        print("   (如果是企业/学校账户，请加 --enterprise 参数运行)")

    # 认证
    token = authenticate()

    # 获取 Drive 信息
    print("\n📊 获取 OneDrive 信息...")
    drive_info = graph_get(token, f"{GRAPH_API}/me/drive")
    if drive_info:
        owner = drive_info.get("owner", {}).get("user", {}).get("displayName", "unknown")
        quota = drive_info.get("quota", {})
        total = format_size(quota.get("total"))
        used = format_size(quota.get("used"))
        print(f"   账户: {owner}")
        print(f"   容量: {used} / {total}")
    print()

    # 开始扫描
    print("🔍 开始扫描 OneDrive 根目录...")
    print("=" * 60)
    tree, stats = scan_directory(token)
    print("=" * 60)

    # 保存 JSON 原始数据
    # 转换 defaultdict 为普通 dict 以支持 JSON 序列化
    stats_json = {
        "total_files": stats["total_files"],
        "total_folders": stats["total_folders"],
        "total_size": stats["total_size"],
        "total_size_human": format_size(stats["total_size"]),
        "extensions": dict(stats["extensions"]),
        "large_files": stats["large_files"],
    }
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        json.dump({"tree": tree, "stats": stats_json}, f, ensure_ascii=False, indent=2)
    print(f"\n💾 JSON 原始数据已保存到: {REPORT_FILE}")

    # 生成 Markdown 报告
    report = generate_report(tree, stats)
    with open(REPORT_MD_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"📝 Markdown 报告已保存到: {REPORT_MD_FILE}")

    # 打印摘要
    print("\n" + "=" * 60)
    print("📋 扫描完成摘要")
    print("=" * 60)
    print(f"  文件总数: {stats['total_files']}")
    print(f"  文件夹总数: {stats['total_folders']}")
    print(f"  总大小: {format_size(stats['total_size'])}")
    print(f"  文件类型数: {len(stats['extensions'])}")
    print(f"  大文件数 (>1MB): {len(stats['large_files'])}")
    print("=" * 60)


if __name__ == "__main__":
    main()
