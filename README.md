# 包参谋·餐饮广告语：十法三选

[English](README.en.md) · **中文** · [安装包](https://github.com/yht0912/baocanmou-restaurant-slogan/releases) · [包参谋官网](https://www.bcmsj.com)

![包参谋餐饮广告语十法三选：输入餐饮资料，十种方法各写一条，比较后推荐三条](assets/cover-bilingual.png)

**给一家餐饮店的资料，按 10 位广告与定位名家的核心方法各写 1 条广告语，比较后推荐 3 条。**

包参谋为餐饮策划、设计师和经营者编写的开源 AI Skill。支持中英文创作，附理论出处、餐饮事实核对、完整示范和结构检查工具。把“顾客为什么选你”落实到一句能说清、能使用、能兑现的话。

## 先看它实际交付什么

虚构小炒店「晚点小炒」：面向下班晚、一个人吃饭的顾客，提供一人份现炒晚饭。用于菜单首页与店内品牌海报。

| 推荐 | 广告语 | 选它的理由 |
|---|---|---|
| 主推 | **晚点小炒，下班晚也吃现炒。** | 品牌、时段场景和品类理由一起说清 |
| 备选 | **一个人吃饭，也值得起一口锅。** | 用实际的一人份服务回应独食处境 |
| 另一角度 | **小炒滋啦响，晚饭热着上。** | 用真实烹调声音和堂食温度表达食欲 |

三条来自同一组十条候选，不是比较完另外再编三条。品牌名、品类说明、营业时段与堂食条件详见完整示范。

[小炒店完整十条与比较](skills/baocanmou-restaurant-slogan/examples/晚点小炒-十法三选.md) · [茶饮店独立试用](skills/baocanmou-restaurant-slogan/examples/青间茶-十法三选.md) · [英文示范](examples/late-wok.en.md)

**演示品牌与经营资料均为虚构，文案是编辑建议，没有真实客户背书或销量成绩。**

## 三步开始

1. [下载最新 Release](https://github.com/yht0912/baocanmou-restaurant-slogan/releases/latest)，选择 `baocanmou-restaurant-slogan-skill-v1.1.0.zip`；也可以克隆本仓库。
2. 将 Skill 完整文件夹安装到 AI 助手的技能目录；详细步骤见[中英文安装说明](docs/INSTALL.md)。
3. 新开会话，粘贴以下提示与资料。

```text
使用 $baocanmou-restaurant-slogan。
店名：……
品类与主打产品：……
主要顾客与用餐场景：……
能够确认的特点：……
这句话用于：……
按 10 位名家的方法各写 1 条广告语，比较后推荐 3 条，说明主推理由。
```

已有资料直接粘贴或交给宿主助手读取，不必重新填表。资料不全可先试写，但条件须明确。[输入要求与输出说明](docs/USAGE.md)

## 为什么专门做餐饮

- **先看这顿饭**：卖什么、谁来吃、什么时候吃、堂食还是外卖、为什么愿意选。
- **表达能兑现**：“现炒”不自动意味着原料未冷冻；“额外加糖可选”不等于“无糖”；出锅口感不直接保证为配送口感。
- **品牌句与促销句分开判断**：用户要长期主张，就按长期用途选，不能用一次优惠凑三条。
- **每条有依据**：方法前提、经营事实、媒介条件分别核对，缺什么具体写什么。
- **比较有取舍**：看懂、想吃/想来、记住/复述、品牌归属、触点适配。等级属于编辑判断，不是消费者实验。

适用小炒快餐、粉面、正餐、火锅烧烤、咖啡茶饮、烘焙甜品、冷食、外卖和连锁餐饮；不自动把工作扩大为品牌全案。

## 十位名家，十种方法

| 作者 | 本项目采用的核心观点 |
|---|---|
| David Ogilvy 大卫·奥格威 | 品牌形象 |
| Rosser Reeves 罗瑟·瑞夫斯 | 独特销售主张 USP |
| Claude Hopkins 克劳德·霍普金斯 | 具体事实与测试 |
| Bill Bernbach 威廉·伯恩巴克 | 以人为中心的原创表达 |
| Leo Burnett 李奥·贝纳 | 产品内在戏剧性 |
| John Caples 约翰·凯普斯 | 直接标题与反应测试 |
| Eugene Schwartz 尤金·施瓦茨 | 既有欲望与认知阶段 |
| James Webb Young 詹姆斯·韦伯·扬 | 旧元素的新组合 |
| Al Ries 艾·里斯 | 定位与聚焦；保留 Jack Trout 共同作者归属 |
| John Hegarty 约翰·赫加蒂 | 有意义的差异与反常规 |

[中文方法卡与逐项出处](skills/baocanmou-restaurant-slogan/references/masters.md) · [English method cards](skills/baocanmou-restaurant-slogan/references/masters.en.md) · [来源核对层级](skills/baocanmou-restaurant-slogan/references/sources.json)

这十位是本项目的选题范围，不是全球排名。每条采用一个可核对的核心观点，理论摘要与餐饮应用分别标明；不表示整套理论已被一句话完整实现，也不表示原作者参与或认可。部分资料核对到公开摘要、访谈或目录，没有冒称通读全部原著。

## 中英文与谋术鸣

默认跟随用户语言。英文创作按目标市场重新组织自然表达；双语交付保留同一方法、事实与编号，译文不另算第十一条。英文资料和案例已随包提供，尚无英语母语消费者测试。

已有谋术鸣定位可以作为输入：价值观约束承诺；谋确定顾客与购买理由；术组织表达；鸣确定使用触点与反馈。这是包参谋对工作流程的承接说明。十位名家的理论各归原作者，不被改署为包参谋原创；谋术鸣完整体系及原有登记作品不包含在本次开源授权中。

## 项目图片

![示范输出预览：同一份资料得到十条候选与三条推荐；虚构案例](assets/example-preview.png)

[双语封面](assets/cover-bilingual.png) · [竖版宣传图](assets/social-poster-bilingual.png) · [流程图](assets/workflow.svg) · [图片尺寸、用途、署名与替代文字](docs/MEDIA-KIT.md)

图中食物为 AI 辅助宣传插画；示范预览由项目实际样例内容排版，不是宿主软件界面截图。没有使用名家肖像、出版社标志或客户照片。

## 环境与验证

| 项目 | 要求或状态 |
|---|---|
| 基础使用 | 能读取 Agent Skills 或完整提示文档的 AI 助手 |
| Python | 创作无需 Python；可选安装/结构检查使用 Python 3.10+ 标准库 |
| 网络与费用 | 项目不内置 API Key、联网请求、遥测、MCP 或自动发布；宿主自身费用与数据政策另行适用 |
| 测试 | 13 项交付结构回归；中文小炒、茶饮样例与英文样例的结构检查 |
| 插件 | 含 `.codex-plugin/plugin.json`，支持按宿主允许方式导入；GitHub 开源不等于官方市场上架 |

```bash
python3 scripts/verify_release.py
python3 -B -m unittest discover -s skills/baocanmou-restaurant-slogan/tests -v
```

检查数量、引用、状态和文件结构，不能证明文案优秀、无近似、可注册或有效增长。[完整验证范围](docs/VALIDATION.md) · [隐私说明](PRIVACY.md)

## 署名、许可与参与

**项目出品：包参谋 / BaoCanMou。发起与产品方向：易慧庭 / Yi Huiting。** 工作流、代码、说明和视觉由包参谋组织，使用 AI 辅助制作。

新编代码、工作流和随附文档使用 [MIT License](LICENSE)。复制或分发本项目的全部或实质部分须保留版权和许可声明；我们欢迎在教程或衍生工具中展示项目来源，但不会给 MIT 额外增加“广告语必须带包参谋署名”的限制。

[完整署名与版权边界](docs/ATTRIBUTION.md) · [来源与素材说明](NOTICE.md) · [贡献指南](CONTRIBUTING.md) · [提问与反馈](https://github.com/yht0912/baocanmou-restaurant-slogan/issues) · [版本记录](CHANGELOG.md)

推荐引用：**包参谋 BaoCanMou，《餐饮广告语：十法三选》，v1.1.0，2026。** GitHub 的 Cite this repository 可读取 [CITATION.cff](CITATION.cff)。

---

**包参谋®｜懂生意的设计参谋**  
**先定位，后设计。**  
先理清顾客为什么选你，再把选择你的理由，做进 Logo/VI、包装与品牌空间。

[了解包参谋](https://www.bcmsj.com)
