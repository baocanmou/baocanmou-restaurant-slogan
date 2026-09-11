# 安装与使用 / Installation

[中文首页](../README.md) · [English overview](../README.en.md)

## 1. 选对文件 / Choose a package

| Release 文件 / File | 用途 / Purpose |
|---|---|
| `baocanmou-restaurant-slogan-skill-v1.1.0.zip` | 精简完整 Skill，适合技能目录安装 / Complete standalone Skill |
| `baocanmou-restaurant-slogan-plugin-v1.1.0.zip` | 插件清单、Skill、中英文文档、图片和贡献文件 / Full Codex plugin and repository content |
| `SHA256SUMS.txt` | 核对下载文件 / Verify downloaded archives |

下载入口 / Download: [GitHub Releases](https://github.com/yht0912/baocanmou-restaurant-slogan/releases/latest)。

无需 Python 即可手动安装。先解压；真正要复制的目录内必须直接包含 `SKILL.md`，不要把 ZIP 或外面多套的一层目录放进去。保留 `references/`、`scripts/`、`examples/`，不要只复制入口文件。

Manual installation does not require Python. Extract the archive, locate the folder containing `SKILL.md` directly, and copy that complete folder. Keep its references, scripts and examples.

## 2. 安装 Skill / Install the Skill

| 宿主 / Host | 用户级目录 / User-level destination |
|---|---|
| Codex | `~/.agents/skills/baocanmou-restaurant-slogan/` |
| Claude Code | `~/.claude/skills/baocanmou-restaurant-slogan/` |
| 其他 Agent Skills 宿主 / Other hosts | 使用该宿主当前文档规定的目录或上传入口 / Follow that host’s current documentation |

不同宿主版本可能有项目级和用户级入口差异；本包不宣称全部版本兼容。若已有共享技能源和符号链接，沿用原有结构，不再复制一份同名技能。

Hosts differ in discovery and project-level support. If you already use a shared source with symlinked host entries, preserve that setup instead of creating duplicate skills.

从 GitHub 克隆后可使用本仓库的保守安装工具 / From a clone, use the included installer:

```bash
git clone https://github.com/yht0912/baocanmou-restaurant-slogan.git
cd baocanmou-restaurant-slogan
python3 scripts/install_skill.py --host codex --dry-run
python3 scripts/install_skill.py --host codex
```

Claude Code 把 `codex` 改成 `claude`。工具不联网，只复制本包 Skill。已有同名目标时会停止；确认升级后使用 `--replace`，旧版先移入带时间的备份目录。备份路径会打印，手动恢复时先移走新目录，再把备份改回原名。符号链接目标要求在共享源处处理，不让安装器替你改链接。

For Claude Code, replace `codex` with `claude`. The installer is local-only. It stops on an existing destination; `--replace` explicitly backs up a normal directory before replacing it. Restore by moving the new directory aside and renaming the printed backup. Symlink destinations are refused: manage those at the shared source.

## 3. 调用 / Invoke

重新开始一个会话。用 `$baocanmou-restaurant-slogan` 或明确说“使用餐饮广告语十法三选”。已运行的会话不保证自动发现新版本。

Start a new conversation. Invoke `$baocanmou-restaurant-slogan` or explicitly request this Skill. Already-running conversations may not discover a new installation.

[输入提示及工作要求 / Brief template](USAGE.md)

## Codex 插件包装 / Codex plugin packaging

完整包的根目录含 `.codex-plugin/plugin.json`，声明 `skills/` 和项目图片。它没有 hooks、MCP 服务器或关联 App。

GitHub 仓库不是已配置的插件市场。不要直接把仓库网址当成 `codex plugin add` 的插件名。本版公开分发以可移植 Skill 安装为基础；如需在 Codex 插件面板显示，可请 Codex 用本机 `plugin-creator` 按已安装版本支持的 personal-marketplace 流程登记此本地插件，再安装。个人 marketplace 的建立/修改应使用该版本的官方辅助脚本，保留已有条目。没有把本仓库冒充官方精选插件。

The full package includes a valid Codex manifest and skill discovery directory, with no hooks, MCP server or connected app. A GitHub repository is not automatically a configured plugin marketplace. Do not pass this repository URL as a plugin selector to `codex plugin add`. The portable Skill path above is the public installation route. For a local Codex plugin-panel entry, ask Codex to register this local package using the installed `plugin-creator` personal-marketplace workflow, preserving existing entries. This project is not presented as an official curated listing.

## 检查与卸载 / Check and uninstall

```bash
python3 scripts/verify_release.py
python3 skills/baocanmou-restaurant-slogan/scripts/check_delivery.py examples/late-wok.en.json
```

仅移走你安装的这一个同名 Skill 目录即可停止其后续发现；重开会话。保留自己创作的输出。用插件市场安装的版本应使用宿主的卸载入口，避免直接删缓存。

Remove only the Skill directory you installed and start a new conversation. Keep your own outputs. For marketplace-managed installations, use the host’s uninstall interface rather than deleting cache files directly.
