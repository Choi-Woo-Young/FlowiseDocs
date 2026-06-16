# Simple Chat Engine

A simple chat engine functions as a complete pipeline for engaging in a dialogue between AI and user, without context retrieval. However it does equipped with [메모리](../../langchain/memory/), allowing to remember conversations.

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

## Inputs

* Chat 모델
* [메모리](../../langchain/memory/)

## 매개변수

| Name           | 설명                                   |
| -------------- | --------------------------------------------- |
| 시스템 메시지 | An instruction for LLM on how to answer query |

## Outputs

| Name             | 설명                   |
| ---------------- | ----------------------------- |
| SimpleChatEngine | Final node to return response |
