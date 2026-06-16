# 컨텍스트 Chat Engine

A chat engine serves as an end-to-end pipeline for having a human-like conversation with your data, allowing for multiple exchanges rather than a single question-and-answer interaction.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Inputs

* Chat 모델
* Vector Store Retriever
* [메모리](../../langchain/memory/)

## 매개변수

| Name                    | 설명                                                         |
| ----------------------- | ------------------------------------------------------------------- |
| Return 소스 Documents | To return citations/sources that were used to build up the response |
| 시스템 메시지          | An instruction for LLM on how to answer query                       |

## Outputs

| Name              | 설명                   |
| ----------------- | ----------------------------- |
| ContextChatEngine | Final node to return response |
