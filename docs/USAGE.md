# 使用要求 / Usage requirements

## 中文

**最小输入：** 品类与主打产品、顾客与用餐场景、可兑现的特点、广告语用途。品牌名、城市、价格带、堂食/外卖、连锁差异与语言市场有则补充。已有材料直接使用，不强制长问卷。

```text
用餐饮广告语十法三选。
品牌：……；品类/产品：……；顾客与场景：……。
已知事实：……；未知项：……。
主用途：菜单/包装/海报/外卖店铺/短视频中的……。
目标语言与市场：……。
保留的品牌原则：……。
给10条候选、统一比较、3条推荐，以及每条的理论出处和使用条件。
```

**交付顺序：** 简报摘要 → 10 条候选 → 5 个维度比较 → 3 条推荐 → 来源。主推和两个备选必须来自原有十条并保持同一编号与原句。

每条有作者/方法、广告语、餐饮事实、简短创作理由和条件。三条推荐写清如何连用品牌与品类、为何比另两条更合适、能否兑现、下一步怎样试。主推不是自动总分冠军。

**事实状态：** 用户提供、独立核对、未知、虚构演示。用户给出的材料不自动变成独立验证。条件稿可以进入十条候选；关键前提尚缺时不能进入完整的可用推荐。确实不足三条先修订；仍缺资料时说清缺口，不凑数。

**双语：** 先确定主语言，同一个候选保留事实与方法，再做目标语言改写；清楚标明译文/改写，不虚构本地消费者反馈。

**正式复查：** 可选保存 `delivery.json`，字段见 [selection.md](../skills/baocanmou-restaurant-slogan/references/selection.md)。工具只检查结构；写完仍需编辑读出来，核对具体餐饮体验与媒介。

**实际发布前：** 核对经营事实和所在市场当前要求。公开搜索近似表达前确认可以将未公开句子送给搜索引擎；没有搜索或顾客测试就如实标明。Skill 不自动发布、不联络别人、不代替产品经营或商标查询。

## English

**Minimum brief:** restaurant category and core products, customers and dining occasion, supportable facts, and the intended placement/task. Add brand, city, price range, dine-in/delivery, location differences and language/market when known. Existing material is welcome; a long questionnaire is not required.

```text
Use Restaurant Slogans: Ten Approaches, Three Picks.
Brand: …; category/products: …; audience and dining occasion: ….
Known facts: …; unknowns: ….
Primary use: … on a menu/package/poster/delivery page/video.
Creative language and intended market: ….
Existing brand principles: ….
Return ten candidates, a shared comparison, and three recommendations,
with source-based methods and the conditions for using each line.
```

**Output:** brief summary → ten candidates → five-dimension comparison → three recommendations → sources. The lead and two alternatives retain the same IDs and wording as candidates in the original ten.

Each candidate states its author/method, line, restaurant basis, concise creative rationale and conditions. Each recommendation explains required brand/category pairing, its tradeoff against the other choices, operational conditions and a practical test. The winner is not selected by an automatic total score.

**Fact status:** user-provided, independently verified, unknown, or explicitly fictional. User statements are not automatically independent evidence. A conditional candidate can remain among the ten, but unresolved critical prerequisites exclude it from complete recommendations. Revise weak candidates first; if facts genuinely prevent three valid choices, report the shortfall.

**Bilingual work:** establish a primary language; adapt the same facts and creative mechanism to the second language. Label translations/adaptations and do not invent local consumer findings.

**Optional audit:** save `delivery.json` using [the schema guide](../skills/baocanmou-restaurant-slogan/references/selection.en.md). Structural checks do not replace editorial review of natural wording, food details or suitability.

**Before real publication:** verify operational facts and applicable local requirements. Get permission before sending confidential new wording to a public search engine for similarity checks. State whether search and consumer testing actually occurred. The Skill does not publish, contact other people or perform trademark clearance automatically.
