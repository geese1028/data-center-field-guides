# 项目执行合同

**项目：** Data Center Field Guides（暂名）  
**日期：** 2026-10-11  
**委托人：** 你  
**执行人：** 本会话  
**状态：** 已确认，生效

这是项目执行约定，不是律师出具的法律意见。

## 1. 目的

用 OneDrive 技术文档做检索素材，写英文技术现场手册，自出版变现。Amazon 与其他平台同时发，不进 KDP Select。AI 生成的正文、图、翻译在 KDP 申报。

## 2. 流水线

1. 做文件名清单，再为范围内、且抽得出正文的文档做摘要，导入 OpenViking。
2. 委托人定题目。
3. `series-editor` 只查已验收的 OpenViking 摘要，出 brief。
4. 委托人点头。
5. `tech-book-writer` 写 1.5–2.5 万词英文现场手册。需要细节时，按摘要里的 `path` 打开原件，不把原文嵌进向量库。
6. `series-editor` 验收：接受、退改、杀掉。写作不能自评。
7. `book-design` 出 EPUB3，过 epubcheck，并出封面。
8. `publish-promote` 出上架包。`author-seo` 出落地页和主题短文。
9. 委托人上传 KDP，并发布主页。
10. 上架满 30 天，只翻译卖得动的。顺序：德、日、西、法、葡。

第一本是试点。卖得动再每月 1 本，上限 2 本。前四本题目：气流、腐蚀、PUE、运维框架。英文未验收前不启动翻译。

## 3. 索引方法

不嵌全文。四套方法合成一套：

- **sumy / Luhn：** 按词密度选代表句，不调用大模型，不改写。
- **RAPTOR：** 摘要要覆盖全文，不只取开头。文档分成最多 6 段，每段取最好的一句。
- **父文档检索：** 摘要里留原路径。写书时再打开原件。
- **OpenViking L0/L1：** 一句摘要用于检索，章节和覆盖句用于导航。L2 全文不导入。

篇幅：

- 抽取出的正文不到 3000 字：一张卡片，上限 1400 字。
- 更长的文档：上限 4000 字。按章节各留一句。章节太多再拆成节卡片，每张仍不超过 1400 字。
- 没有正文的文件只留路径和文件名，并计入缺口清单。

现有中断稿在验收前重做。正文从 NAS 上的 sqlite 远程读取，以及本机已缓存的缺口文件抽取。不再把 3.8GB 库拷回本机，不再在 `sources/` 留下全文副本。

## 4. 导入和使用

- 只导入 `sources/content/summaries/`。
- 命令：`ov add-resource … --processing-mode vectors_only --parent-auto-create viking://resources/book-summaries`。不用语义模式。
- 检索：`ov find "问题" -u viking://resources/book-summaries`。不跑全局 `ov search`。
- 不碰 `viking://resources/project-library-20261005`。
- 索引由 subagent 制作。执行人按第 6 条复核。不过关就删除这次导入，不当作书稿来源。

## 5. 范围

进索引：pdf、doc、docx、ppt、pptx、xls、xlsx、xlsm、csv、md、txt、rtf，以及工作笔记。含 ASHRAE、COBIT、标准、课件、厂商手册。简历进。版权检查在发布前做，不在索引阶段剔除。

不进：优才申请资料、初中报名、home、`CFD逻辑` 和交易记录。文件名含密码、证件、身份证、通讯录的不打开。图片、视频、安装包不进。`OneDrive备份` 不进。

## 6. 验收

- 摘要条数等于文件名清单里有正文、且不在排除范围的文档数。缺的要有清单。
- 抽 20 份：有标题、有 `path`、有章节或覆盖句。短稿不超过 1400 字，长稿不超过 4000 字。
- 优才、报名、home、交易记录为 0。密码、证件、身份证、通讯录为 0。
- 这 5 条必须能查到：气流组织、PUE、ASHRAE、COBIT、一份简历。
- 导入任务完成，错误为 0。嵌入队列清空后，待处理为 0。
- 抽 5 条确认向量里是摘要，不是全文。
- `project-library` 仍在。本机 `sources` 不超过 200MB。

## 7. 书稿

写作只能查已验收的摘要。索引阶段不因版权剔素材。版权检查在发布前做。

写进书里的必须是新的英文表述。贴源文、贴近改写、客户名、现场编号、图纸和参数表，验收杀掉。改写不产生发表权。委托人对发表权负责。

## 8. 交付

六个 skill，放在 `.opencode/skills/<name>/SKILL.md`：`series-editor`、`tech-book-writer`、`book-design`、`publish-promote`、`author-seo`、`tech-translate`。

主页在 `site/`，不放全文。执行人不登录 KDP，不买评，不代投广告。

## 9. 变更

改索引边界、书稿规则或流水线，须先改本合同。未改合同的口头要求，不覆盖第 3、4、5、6 条。

2026-10-11：全文不导入 OpenViking。摘要按篇幅伸缩，上限 4000 字。检索 URI 为 `viking://resources/book-summaries`。

## 10. 生效

委托人于 2026-10-11 确认。第一步写入本合同，然后重做摘要、导入，并按第 6 条验收。
