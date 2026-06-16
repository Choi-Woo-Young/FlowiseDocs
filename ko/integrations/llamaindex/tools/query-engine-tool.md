# 쿼리 Engine 도구

Turns 쿼리 Engine into a 도구 which can then be used by [Sub-Question 쿼리 Engine](../engine/sub-question-query-engine.md) or Agent.

<figure><img src="../../../.gitbook/assets/image (9) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

## Inputs

* Vector Store 인덱스

## 매개변수

| Name             | 설명                                         |
| ---------------- | --------------------------------------------------- |
| 도구 Name        | Name of the tool                                    |
| 도구 설명 | A description to tell when LLM should use this tool |

## Outputs

| Name            | 설명                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------ |
| QueryEngineTool | Connecting point to Agent or [Sub-Question 쿼리 Engine](../engine/sub-question-query-engine.md) |
