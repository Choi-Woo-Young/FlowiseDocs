---
description: LangChain Memory Node
---

# Memory

***

Memory를 사용하면 AI가 이전 대화의 기억을 가지고 있는 것처럼 AI와 채팅할 수 있습니다.

_<mark style="color:blue;">Human: hi i am bob</mark>_

_<mark style="color:orange;">AI: Hello Bob! It's nice to meet you. How can I assist you today?</mark>_

_<mark style="color:blue;">Human: what's my name?</mark>_

_<mark style="color:orange;">AI: Your name is Bob, as you mentioned earlier.</mark>_

내부적으로 이러한 대화는 배열이나 데이터베이스에 저장되어 LLM에 컨텍스트로 제공됩니다. 예를 들어:

```
You are an assistant to a human, powered by a large language model trained by OpenAI.

Whether the human needs help with a specific question or just wants to have a conversation about a particular topic, you are here to assist.

Current conversation:
{history}
```

### Memory Node:

* [Buffer Memory](buffer-memory.md)
* [Buffer Window Memory](buffer-window-memory.md)
* [Conversation Summary Memory](conversation-summary-memory.md)
* [Conversation Summary Buffer Memory](conversation-summary-buffer-memory.md)
* [DynamoDB Chat Memory](dynamodb-chat-memory.md)
* [Mem0 Memory](mem0-memory.md)
* [MongoDB Atlas Chat Memory](mongodb-atlas-chat-memory.md)
* [Redis-Backed Chat Memory](redis-backed-chat-memory.md)
* [Upstash Redis-Backed Chat Memory](upstash-redis-backed-chat-memory.md)
* [Zep Memory](zep-memory.md)

## 여러 사용자를 위한 대화 분리

### UI 및 임베디드 채팅 (Embedded Chat)

기본적으로 UI 및 임베디드 채팅은 서로 다른 사용자의 대화를 자동으로 분리합니다. 이는 각 새 상호작용마다 고유한 **`chatId`**를 생성함으로써 이루어집니다. 이 로직은 Flowise에 의해 내부적으로 처리됩니다.

### Prediction API

고유한 **`sessionId`**를 지정하여 여러 사용자의 대화를 분리할 수 있습니다.

1. 모든 memory node에서 input parameter **`Session ID`**를 볼 수 있습니다

<figure><img src="../../../.gitbook/assets/image (76).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Untitled (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

2. `/api/v1/prediction/{your-chatflowid}` POST body 요청에서 **`overrideConfig`** 내에 **`sessionId`**를 지정합니다

```json
{
    "question": "hello!",
    "overrideConfig": {
        "sessionId": "user1"
    }
}
```

### Message API

* GET `/api/v1/chatmessage/{your-chatflowid}`
* DELETE `/api/v1/chatmessage/{your-chatflowid}`

<table><thead><tr><th>Query Param</th><th width="192">Type</th><th>Value</th></tr></thead><tbody><tr><td>sessionId</td><td>string</td><td></td></tr><tr><td>sort</td><td>enum</td><td>ASC or DESC</td></tr><tr><td>startDate</td><td>string</td><td></td></tr><tr><td>endDate</td><td>string</td><td></td></tr></tbody></table>

모든 대화는 UI에서도 시각화하고 관리할 수 있습니다:

<figure><img src="../../../.gitbook/assets/image (78).png" alt=""><figcaption></figcaption></figure>

OpenAI Assistant의 경우, 대화를 저장하는 데 [Threads](../agents/openai-assistant/threads.md)가 사용됩니다.
