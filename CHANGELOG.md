# Changelog / 版本记录

## 1.2.0 — 2026-10-05

- 支持国产 AI 工具：安装说明补充 Kimi Code CLI、文心快码、Qwen Code、TRAE、豆包、扣子。 / Install notes for Kimi Code CLI, Baidu Comate, Qwen Code, TRAE, Doubao and Coze.
- 新增聊天版 `PROMPT.md`，DeepSeek、Kimi、豆包、通义千问、文心等聊天窗口复制即用；由 `scripts/build_prompt.py` 从 SKILL.md 生成，并有回归检查。 / New chat-app prompt generated from SKILL.md, with a freshness test.
- SKILL.md 说明脚本路径相对于技能目录。 / SKILL.md notes that script paths are relative to the skill folder.

## 1.1.1 — 2026-09-11

- 修复升级时旧 Skill 备份位置：移到技能扫描目录之外，避免宿主发现重复入口；新增 3 项安装回归。 / Move upgrade backups outside the skills discovery directory to avoid duplicate entries; add 3 installer regressions.
- 保留已发布 v1.1.0 和原有历史。 / Keep the published v1.1.0 and its history intact.

## 1.1.0 — 2026-09-11

- 首次 GitHub 开源插件发行：Codex 清单、完整中英文说明、英文执行与方法卡。 / First GitHub plugin release: Codex manifest, bilingual docs and English method/execution guides.
- 英文编辑示范、双语封面、竖版海报、矢量流程图及项目图标。 / English editorial example, bilingual cover/poster, vector workflow and plugin icon.
- 作者署名、来源边界、MIT 使用、隐私、贡献与反馈指南。 / Attribution, source boundaries, MIT reuse, privacy and contribution guides.
- 保留十候选三推荐与 13 项回归；增加发布检查和本地保守安装器。 / Retained ten-to-three behavior and 13 regressions; added release checks and a conservative installer.

## 1.0.0 — 2026-09-10

- 本地中文首版、十张方法卡、小炒与茶饮虚构示范。 / Initial local Chinese Skill, ten method cards and fictional stir-fry/tea examples.
- 独立试用发现并修复多媒介字段兼容问题。 / Independent trial exposed and led to a multi-medium input fix.
