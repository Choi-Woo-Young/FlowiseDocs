# Sub-Question 쿼리 Engine

A query engine designed to solve problem of answering a complex query using multiple data sources. It first breaks down the complex query into sub questions for each relevant data source, then gather all the intermediate reponses and synthesizes a final response.

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

## Inputs

* 쿼리 Engine Tools
* Chat 모델
* Embeddings
* [응답 Synthesizer](../response-synthesizer/)

## 매개변수

| Name                    | 설명                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| Return 소스 Documents | To return citations/sources that were used to build up the response |

## Outputs

| Name                   | 설명                   |
| ---------------------- | ----------------------------- |
| SubQuestionQueryEngine | Final node to return response |
