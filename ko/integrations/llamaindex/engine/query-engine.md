# 쿼리 Engine

A query engine serves as an end-to-end pipeline enabling users to ask questions about their data. It receives a natural language query and furnishes a response, accompanied by relevant context information retrieved and passed to the LLM (Large Language 모델).

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

## Inputs

* Vector Store Retriever
* [응답 Synthesizer](../response-synthesizer/)

## 매개변수

| Name                    | 설명                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| Return 소스 Documents | To return citations/sources that were used to build up the response |

## Outputs

| Name        | 설명                   |
| ----------- | ----------------------------- |
| QueryEngine | Final node to return response |
