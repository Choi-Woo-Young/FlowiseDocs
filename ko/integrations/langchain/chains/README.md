---
description: LangChain Chain Nodes
---

# Chains

***

챗봇과 대규모 언어 모델의 맥락에서 "체인(chains)"은 일반적으로 텍스트 또는 대화 턴의 시퀀스를 의미합니다. 이러한 체인은 챗봇 또는 언어 모델의 대화 이력 및 컨텍스트를 저장하고 관리하는 데 사용됩니다. 체인은 모델이 진행 중인 대화를 이해하고 일관성 있고 상황에 맞는 응답을 제공하도록 도와줍니다.

체인이 작동하는 방식은 다음과 같습니다:

1. **대화 이력**: 사용자가 챗봇 또는 언어 모델과 상호작용할 때, 대화는 종종 일련의 텍스트 메시지 또는 대화 턴으로 표현됩니다. 사용자와 모델의 각 메시지는 대화의 컨텍스트를 유지하기 위해 시간순으로 저장됩니다.
2. **입력 및 출력**: 각 체인은 사용자 입력과 모델 출력 모두로 구성됩니다. 사용자의 입력은 일반적으로 "입력 체인"이라고 불리고, 모델의 응답은 "출력 체인"에 저장됩니다. 이를 통해 모델은 대화의 이전 메시지를 참조할 수 있습니다.
3. **상황 이해**: 이러한 체인에서 전체 대화 이력을 보존함으로써 모델은 컨텍스트를 이해하고 이전 메시지를 참조하여 일관성 있고 상황에 맞는 응답을 제공할 수 있습니다. 이는 사용자와의 자연스럽고 의미 있는 대화를 유지하는 데 중요합니다.
4. **최대 길이**: 체인은 메모리 사용량과 계산 리소스를 관리하기 위해 최대 길이를 가집니다. 체인이 너무 길어지면 오래된 메시지가 제거되거나 잘려서 새 메시지를 위한 공간을 만들 수 있습니다. 이는 중요한 대화 세부 정보가 제거될 경우 컨텍스트 손실로 이어질 수 있습니다.
5. **대화 계속**: 실시간 챗봇 또는 언어 모델 상호작용에서 입력 체인은 사용자의 새로운 메시지로 지속적으로 업데이트되고, 출력 체인은 모델의 응답으로 업데이트됩니다. 이를 통해 모델은 진행 중인 대화를 추적하고 적절하게 응답할 수 있습니다.

체인은 챗봇 및 언어 모델 대화를 구축하고 유지하는 데 기본이 되는 개념입니다. 모델이 의미 있고 상황 인식적 응답을 생성하는 데 필요한 컨텍스트에 접근할 수 있도록 보장하여 사용자에게 더 매력적이고 유용한 상호작용을 제공합니다.

### Chain Nodes:

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
