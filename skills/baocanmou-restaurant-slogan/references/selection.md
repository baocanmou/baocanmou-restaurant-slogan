# 比较、推荐与交付

## 先检查适用

每条检查：来源是否支持所用原理；创作动作是否符合原理；事实是否支持；是否适合本次用途。标为“可比较 / 条件稿 / 重写”。这是应用审核，不等于作者认可。

条件要说明缺在理论前提、经营事实还是媒介适配。文案字面事实成立，仍可能缺少USP竞争依据；不要把两者混成一句“全部不真实”。

未知差异、未确认工序或价格承诺要明确条件。押韵、名气等优点不能抵消兑现缺口。

## 同一把尺子

以下是包参谋餐饮广告语的编辑比较，不冒称大师原有评分模型。先隐藏作者，只看文案及必要品牌/品类搭配，以强/中/弱初评，不计算成功概率。

| 维度 | 强 | 中 | 弱 |
|---|---|---|---|
| 看懂 | 一眼知道品类或明确购买理由 | 连用品类说明才清楚 | 不知卖什么、得到什么 |
| 想吃/想来 | 击中给定场景的食欲或动机 | 有感觉，不够具体 | 与吃饭选择无关 |
| 记住/复述 | 自然复述，记忆点清楚 | 通顺但易混淆 | 拗口、太长、需解释双关 |
| 品牌归属 | 连接本店事实或已有资产 | 同品类多数店可用 | 任何品类都能套 |
| 触点适配 | 适合指定媒介、时段、用途 | 需明确连用或范围 | 必须换媒介或经营条件 |

等级后的理由更重要，至少指出一个代价。不得按总分自动选；优先满足用户目标。相似的三条不算三个方向。

## 最后三条

保留候选编号与原句，选主推与两个确实适用的备选。附：为何选且与另外两条比较；如何摆放及连用；真实兑现条件；简单验证办法。

未做消费者试验写“编辑建议，未实测”，不编样本、投票或购买提升。验证可以先让目标顾客用自己的话说出卖什么、为何想选；进一步投放才比较同预算、同视觉、同触点的理解/点选/订单，不能把短期点选胜出等同长期品牌效果。

改字后须回到十条候选同步更新应用审核与比较；不足3条先修订，确实缺资料就明确缺口，不能给不成立方案盖章。

## 可选结构文件

delivery.json 用于正式复查，由AI填写。短对话按同样逻辑人工检查。

顶层：
- schema_version: "1.0"
- status: "complete" 或 "partial"
- brief: brand, category, audience_scene, task 为非空文字；primary_medium 可以是非空文字或非空文字数组（例如菜单首页与杯身）；另有 facts 数组。
- facts 每项: id, text, status, source。status为 provided（用户提供）、verified（独立证据）、unknown（未确认）、fictional（明确演示）。虚构例另设 brief.fictional: true。
- candidates: 10项。每项 id, master_id, line, fact_ids, application, eligibility, conditions, comparison, tradeoff。
- application: principle（原则）, move（句中如何体现）, limit（边界），均为非空文字。
- eligibility: eligible / conditional / reject；conditions为条件文字数组。
- comparison: clarity, appetite, memory, brand, medium，各为 strong / medium / weak。
- recommendations: 每项 rank, candidate_id, reason, placement, condition, test。
- shortage_reason: partial时解释为何不足3条。
- validation: consumer_test, similarity_search（如 not_run）；不要伪造真实测试。

完整交付需10个不同作者候选、3个不重复推荐。unknown事实不得支持eligible；条件稿不可进入完整推荐。脚本只验证数量、身份、引用和状态一致性；方法质量、语义重复、真实性、等级理由与效果仍须人工判断。
