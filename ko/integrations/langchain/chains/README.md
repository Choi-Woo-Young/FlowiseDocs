---
description: LangChain Chain Node
---

# Chains

***

챗봇 및 대규모 언어 모델의 맥락에서 "chain"은 일반적으로 텍스트 또는 대화 턴의 시퀀스를 의미합니다. 이러한 chain은 챗봇이나 언어 모델의 대화 기록 및 컨텍스트를 저장하고 관리하는 데 사용됩니다. Chain은 모델이 진행 중인 대화를 이해하고 일관되며 맥락에 맞는 응답을 제공하도록 돕습니다.

Chain이 작동하는 방식은 다음과 같습니다:

1. **대화 기록 (Conversation History)**: 사용자가 챗봇이나 언어 모델과 상호작용할 때, 대화는 종종 일련의 텍스트 메시지 또는 대화 턴으로 표현됩니다. 사용자와 모델의 각 메시지는 대화의 컨텍스트를 유지하기 위해 시간 순서대로 저장됩니다.
2. **Input 및 Output**: 각 chain은 사용자 input과 모델 output으로 구성됩니다. 사용자의 input은 보통 "input chain"이라고 하고, 모델의 응답은 "output chain"에 저장됩니다. 이를 통해 모델이 대화의 이전 메시지를 다시 참조할 수 있습니다.
3. **맥락적 이해 (Contextual Understanding)**: 전체 대화 기록을 이러한 chain에 보존함으로써, 모델은 컨텍스트를 이해하고 이전 메시지를 참조하여 일관되며 맥락에 맞는 응답을 제공할 수 있습니다. 이는 사용자와 자연스럽고 의미 있는 대화를 유지하는 데 매우 중요합니다.
4. **최대 길이 (Maximum Length)**: Chain은 메모리 사용량과 계산 리소스를 관리하기 위해 최대 길이를 가집니다. Chain이 너무 길어지면 새 메시지를 위한 공간을 만들기 위해 오래된 메시지가 제거되거나 잘릴 수 있습니다. 이로 인해 중요한 대화 세부 정보가 제거되면 컨텍스트가 손실될 수 있습니다.
5. **대화의 연속 (Continuation of Conversation)**: 실시간 챗봇 또는 언어 모델 상호작용에서, input chain은 사용자의 새 메시지로 계속 업데이트되고, output chain은 모델의 응답으로 업데이트됩니다. 이를 통해 모델은 진행 중인 대화를 추적하고 적절하게 응답할 수 있습니다.

Chain은 챗봇 및 언어 모델 대화를 구축하고 유지하는 데 있어 근본적인 개념입니다. 이는 모델이 의미 있고 맥락을 인식하는 응답을 생성하는 데 필요한 컨텍스트에 접근할 수 있도록 보장하여, 사용자에게 더 매력적이고 유용한 상호작용을 제공합니다.

### Chain Node:

* [GET API Chain](get-api-chain.md)
* [OpenAPI Chain](openapi-chain.md)
* [POST API Chain](post-api-chain.md)
* [Conversation Chain](conversation-chain.md)
* [Conversational Retrieval QA Chain](conversational-retrieval-qa-chain.md)
* [LLM Chain](llm-chain.md)
* [Multi Prompt Chain](multi-prompt-chain.md)
* [Multi Retrieval QA Chain](multi-retrieval-qa-chain.md)
* [Retrieval QA Chain](retrieval-qa-chain.md)
* [Sql Database Chain](sql-database-chain.md)
* [Vectara QA Chain](vectara-chain.md)
* [VectorDB QA Chain](vectordb-qa-chain.md)
