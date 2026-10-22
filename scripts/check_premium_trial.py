#!/usr/bin/env python3
"""
LinkedIn Premium Trial Expiry Monitor & Auto-Alert System
Monitors the free trial ending on November 22, 2026 and alerts the user in advance
via macOS native notifications, dialogs, and terminal status checks.
"""

import sys
import subprocess
from datetime import datetime, date, timezone

EXPIRY_DATE = date(2026, 11, 22)
ALERT_THRESHOLD_DAYS = 7  # Start alerting 7 days before (Nov 15)
CRITICAL_THRESHOLD_DAYS = 3  # High alert 3 days before (Nov 19)

def send_macos_notification(title, subtitle, message, sound="Glass"):
    apple_script = f'''
    display notification "{message}" with title "{title}" subtitle "{subtitle}" sound name "{sound}"
    '''
    subprocess.run(["osascript", "-e", apple_script], capture_output=True)

def send_macos_dialog(message):
    apple_script = f'''
    display dialog "{message}" with title "LinkedIn Premium 到期提醒" buttons {{"知道了", "立即去取消"}} default button "立即去取消" with icon caution
    '''
    try:
        res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
        if "立即去取消" in res.stdout:
            subprocess.run(["open", "https://www.linkedin.com/premium/manage/"])
    except Exception:
        pass

def check_trial_status(interactive=False):
    today = date.today()
    days_left = (EXPIRY_DATE - today).days

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] LinkedIn Premium Trial Check:")
    print(f"  • Expiry Date : {EXPIRY_DATE.isoformat()} (1-Month Free Trial End)")
    print(f"  • Today's Date: {today.isoformat()}")
    print(f"  • Days Left   : {days_left} days")

    if days_left < 0:
        msg = f"⚠️ 警告：LinkedIn Premium 试用已于 {abs(days_left)} 天前到期（{EXPIRY_DATE}）！如未取消可能已产生扣费。"
        print(f"  [EXPIRED] {msg}")
        send_macos_notification("LinkedIn Premium 已到期！", "请检查信用卡扣费", msg, sound="Sosumi")
        if interactive:
            send_macos_dialog(msg)
        return False

    if days_left == 0:
        msg = "🚨 今天是 LinkedIn Premium 免费试用最后一天！请在今天结束前取消订阅，否则将被扣款！"
        print(f"  [DUE TODAY] {msg}")
        send_macos_notification("【今天到期】LinkedIn Premium 试用最后一天", "最后防扣费关头", msg, sound="Sosumi")
        send_macos_dialog(msg)
        return False

    if days_left <= CRITICAL_THRESHOLD_DAYS:
        msg = f"🚨 紧急提醒：LinkedIn Premium 免费试用仅剩 {days_left} 天到期（{EXPIRY_DATE}）！请尽快前往取消订阅防扣费。"
        print(f"  [CRITICAL] {msg}")
        send_macos_notification(f"【紧急】LinkedIn Premium 仅剩 {days_left} 天", "防扣费提醒", msg, sound="Hero")
        send_macos_dialog(msg)
        return False

    if days_left <= ALERT_THRESHOLD_DAYS:
        msg = f"🔔 提前提醒：LinkedIn Premium 试用还有 {days_left} 天到期（{EXPIRY_DATE}）。如不再需要，建议提前取消。"
        print(f"  [ALERT] {msg}")
        send_macos_notification(f"【提醒】LinkedIn Premium 还剩 {days_left} 天", "到期防扣费", msg, sound="Glass")
        if interactive:
            send_macos_dialog(msg)
        return True

    print(f"  [OK] 试用期安全运行中，将在到期前 7 天（2026-11-15 起）每日桌面弹窗提醒。")
    return True

if __name__ == "__main__":
    is_interactive = "--alert" in sys.argv or "--interactive" in sys.argv
    check_trial_status(interactive=is_interactive)
