# Comparison, recommendations and delivery schema

## Applicability first

Check source support, the creative move, restaurant evidence and intended use. Label each candidate eligible, conditional or reject/rewrite. Separate missing **theory prerequisites**, **literal operational facts** and **medium conditions**. A true benefit can still lack USP evidence. Rhyme or an author’s fame cannot compensate for a missing prerequisite.

## Shared editorial comparison

BaoCanMou’s rubric below is an application design, not an original scoring model from the ten authors. Hide author names while judging the copy. Use strong/medium/weak and explain tradeoffs; do not calculate success probabilities or automatically rank a total score.

| Dimension | Strong | Medium | Weak |
|---|---|---|---|
| clarity | Category or choice reason immediately understood | Needs explicit category pairing | Unclear product or benefit |
| appetite | Specific appetite/visit motive for the brief | Some feeling, little specificity | Unrelated to meal choice |
| memory | Natural to repeat, clear memory cue | Fluent but easily confused | Awkward, long or puzzle-dependent |
| brand | Linked to this business’s facts/assets | Fits many in the same category | Fits any category |
| medium | Fits the given medium and task | Needs stated pairing/scope | Requires a different medium or operation |

Explain at least one meaningful cost. Three near-synonyms do not provide three useful directions.

## Final three

Retain original candidate IDs and wording. Recommend a lead and two valid alternatives for the same primary objective. Explain why the lead wins, how each is paired/placed, operational conditions and a practical test. Mark results as editorial advice unless actual consumers were tested.

Possible first test: ask target diners to explain what is sold and why they might choose it. For paid testing, keep budget, visuals and placement comparable and specify the measured outcome. A short-term click difference is not long-term brand impact.

If wording changes, update the candidate and comparison too. Revise invalid candidates before selecting. If missing facts truly prevent three valid choices, report a partial result rather than pad it.

## Optional JSON

The checker runs locally with Python; it validates structure, not taste, truth or effectiveness.

- `schema_version`: `"1.0"`.
- `status`: `"complete"` or `"partial"`.
- `brief`: nonempty `brand`, `category`, `audience_scene`, `task`; `primary_medium` as text or a nonempty array of nonempty strings; `facts` array.
- Each fact: unique `id`, `text`, `source`, `status` = `provided`, `verified`, `unknown` or `fictional`. Fictional facts require `brief.fictional: true`.
- `candidates`: exactly ten, with `id`, `master_id`, `line`, `fact_ids`, `application`, `eligibility`, `conditions`, `comparison`, `tradeoff`.
- `application`: nonempty `principle`, `move`, `limit`.
- `eligibility`: `eligible`, `conditional`, `reject`. `conditions` is a text array; conditional/rejected candidates need a reason.
- `comparison`: exactly `clarity`, `appetite`, `memory`, `brand`, `medium`; values `strong`, `medium`, `weak`.
- `recommendations`: `rank`, `candidate_id`, `reason`, `placement`, `condition`, `test`.
- `shortage_reason`: explain partial results with fewer than three recommendations.
- `validation`: `consumer_test`, `similarity_search`, honestly recorded, for example `not_run`.

A complete result requires ten distinct authors and three distinct eligible recommendations. Unknown facts cannot support eligible candidates. It remains the editor’s job to judge whether a source really supports a creative move and whether the proposed restaurant claim is true.
