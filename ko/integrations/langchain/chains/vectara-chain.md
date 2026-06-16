# Vectara QA Chain

Vectara를 사용하여 질의응답(question-answering) 작업을 수행하는 chain입니다.

<figure><img src="../../../.gitbook/assets/screely-1700662138252.png" alt=""><figcaption></figcaption></figure>

## 정의 (Definitions)

**검색 기반 질의응답 chain**으로, Vectara retrieval component와 통합되어 input parameter를 구성하고 질의응답 작업을 수행할 수 있습니다.

## Inputs

* [Vectara Store](../vector-stores/vectara.md)

## Parameters

| Name                   | Description                                                   |
| ---------------------- | ------------------------------------------------------------- |
| Summarizer Prompt Name | 요약 생성에 사용할 모델                                        |
| Response Language      | 응답에 사용할 언어                                            |
| Max Summarized Results | 요약에 사용할 상위 결과 수 (기본값 7)                         |

## Outputs

| Name           | Description                   |
| -------------- | ----------------------------- |
| VectaraQAChain | 응답을 반환하는 최종 node     |
