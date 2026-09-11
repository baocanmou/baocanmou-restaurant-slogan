# 验证范围 / Validation scope

## 已核对的项目 / Checked scope

- 13 项交付结构回归，覆盖作者重复、句子重复、未知事实、条件稿推荐、引用缺失、数量及多媒介输入。 / 13 structural regressions covering duplicate authors/lines, unknown facts, conditional recommendations, missing references, counts and multiple media.
- 中文小炒、中文茶饮、英文改写三份完整 JSON。茶饮在 v1.0.0 由另一 AI 独立试用；英文例由本次编辑改写。 / Three complete JSON examples. The Chinese tea example came from an independent AI trial in v1.0.0; the English sample is an editorial adaptation in this release.
- `.codex-plugin/plugin.json` 使用 plugin-creator 的校验工具；Skill 入口使用 skill-creator 结构校验。 / Manifest checked with plugin-creator validation and Skill entry checked with skill-creator validation.
- 仓库本地链接、必备中英文文件、PNG 文件头与尺寸、来源方法数、私有路径与常见凭据特征；安装工具在临时目录核对复制、阻止覆盖和备份恢复。 / Local links, bilingual required files, PNG headers/dimensions, method coverage, private paths and common credential patterns; installer copy/refusal/backup behavior exercised in temporary directories.
- 图片主要文字、构图与示范内容进行视觉复核。 / Visual review of principal image text, composition and example content.

最终发布以本次 GitHub commit、Release 文件及 Actions 检查为准。检查脚本源代码随包公开，方便复核。 / The published commit, release files and GitHub Actions record identify the final build; checking code is included.

## 没有验证的项目 / Not established

- 文案在真实消费者中的理解、记忆、购买或传播效果。 / Real consumer comprehension, recall, purchase or sharing impact.
- 英语母语消费者研究、所有餐饮业态与国家的语言/法规适配。 / Native-English consumer research or every cuisine/jurisdiction.
- 全网近似排查、商标可注册性、版权独创性结论。 / Global similarity clearance, trademark registrability or copyright originality.
- 十位作者本人认可、全部原著逐页核对、全球排名。 / Author endorsement, page-by-page review of every book or a global ranking.
- 所有宿主版本的完整端到端测试；Claude 完整实际调用。 / End-to-end testing of every host/version or a full Claude execution.

结构检查通过不等于广告优秀。比较表的强/中/弱是可讨论的编辑判断。 / Structural success does not prove creative excellence; qualitative comparisons are editorial judgments open to review.

## 复现 / Reproduce

在完整仓库根目录执行 / From the repository root:

```bash
python3 scripts/verify_release.py
python3 -B -m unittest discover -s skills/baocanmou-restaurant-slogan/tests -v
python3 skills/baocanmou-restaurant-slogan/scripts/check_delivery.py examples/late-wok.en.json
```

无需安装 Python 第三方依赖。官方 plugin-creator / skill-creator 工具需在装有对应工具的 Codex 环境单独使用，本仓库不镜像或冒充它们。 / These commands need only Python’s standard library. Official plugin-creator/skill-creator checks require the corresponding installed Codex tools; they are not mirrored or impersonated here.
