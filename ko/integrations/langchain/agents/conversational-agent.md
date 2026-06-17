---
description: 채팅 모델용 Conversational Agent입니다. 채팅 특화 프롬프트를 활용합니다.
---

# Conversational Agent

<figure><img src="../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1).png" alt="" width="271"><figcaption><p>Conversational Agent Node</p></figcaption></figure>

## Conversational Agent 설정

## 필수 요구사항:
* Flowise를 설정합니다.
* Docker를 다운로드하고 설치합니다.
* Ollama 언어 모델을 로컬로 다운로드하고 설치합니다.
    * https://ollama.com/
* Redis for AI를 다운로드하고 설치합니다.
    * https://redis.io/redis-for-ai/

## 컨텍스트:
일반적인 용도의 언어 기반 작업을 수행하는 표준 대규모 언어 모델(LLM)과 달리, Conversational Agent는 대화를 효과적으로 관리하도록 특별히 설계되었으므로 더 정교합니다.

Flowise conversational agent를 사용하여 포괄적이고 대화식의 대화 경험을 만들 수 있습니다.

## 단계:
1. Chatflows 메뉴에 접근합니다.
    1. 브라우저를 열고 http://localhost:3000으로 이동합니다.
    2. Flowise에서 **Chatflows**를 클릭합니다.

2. 새로운 chatflow를 생성합니다:
    1. **Add New**를 클릭합니다.
    2. chatflow의 이름을 입력하고 **Save**를 클릭합니다.

3. Conversational Agent 노드를 추가합니다:
    1. **Add Node**를 클릭합니다.
    2. Conversational Agent를 검색합니다.
    3. Conversational Agent 노드를 chatflow 워크스페이스로 드래그하여 놓습니다.

4. SearchAPI 노드를 추가합니다. 이 노드는 agent가 Google 검색 결과에서 데이터를 가져올 수 있게 합니다:
    1. **Add Node**를 클릭합니다.
    2. SearchAPI 노드를 검색합니다. 검색 결과의 **Tools** 섹션에 표시됩니다.
    3. SearchAPI 노드를 chatflow 워크스페이스로 드래그하여 놓습니다.
    4. 무료 SearchAPI 계정을 만들고 SearchAPI API 키를 검색합니다. SearchAPI 노드는 인증 및 검색 쿼리를 수행하기 위해 이 키가 필요합니다.
    5. SearchAPI 노드에서 **Connect Credentials > Create New**를 클릭합니다.
    6. 자격증명 이름(예: SearchAPI Credentials)을 입력하고, SearchAPI API 키를 SearchAPI API Key 필드에 복사하여 붙여넣은 후 **Add**를 클릭합니다.
    7. SearchAPI 노드의 Output 섹션에서 Conversational Agent 노드의 Allowed Tools Inputs 섹션으로 선을 그려 SearchAPI 노드를 Conversational Agent 노드에 연결합니다.
    8. **Save Chatflow**를 클릭하여 진행상황을 저장합니다.

5. ChatOllama 채팅 모델 노드를 추가합니다. 이 노드는 agent가 Ollama 언어 모델을 사용하여 응답을 생성할 수 있게 합니다:
    1. **Add Node**를 클릭합니다.
    2. ChatOllama 노드를 검색합니다. 검색 결과의 **Chat Models** 섹션에 표시됩니다.
    3. ChatOllama 노드를 chatflow 워크스페이스로 드래그하여 놓습니다.
    4. **Model Name** 필드에 사용할 모델을 입력합니다. llama3.2를 권장합니다.
    5. **Temperature** 필드에서 0부터 1 사이의 온도 값을 설정합니다. 온도 매개변수는 모델의 응답의 무작위성을 제어합니다. 낮은 온도는 결정론적이고 초점이 맞춰진 응답을 생성합니다. 높은 온도는 창의적이고 다양한 응답을 생성합니다. 온도 값 0.5를 권장합니다.
    6. ChatOllama 노드의 Output 섹션에서 Conversational Agent 노드의 Chat Model Inputs 섹션으로 선을 그려 ChatOllama 노드를 Conversational Agent 노드에 연결합니다.
    7. **Save Chatflow**를 클릭하여 진행상황을 저장합니다.

6. Redis 채팅 메모리 노드를 추가합니다. 이 노드는 agent가 이전 상호작용을 기억하고 채팅 히스토리에 저장하여 전체 사용자 경험을 향상시킵니다:
    1. **Add Node**를 클릭합니다.
    2. Redis-Backed Chat Memory 노드를 검색합니다. 검색 결과의 **Memory** 섹션에 표시됩니다.
    3. Redis-Backed Chat Memory 노드를 chatflow 워크스페이스로 드래그하여 놓습니다.
    4. Redis-Backed Chat Memory 노드에서 **Connect Credentials > Create New**를 클릭합니다.
    5. Redis API 사용자명과 비밀번호, 또는 Redis 자격증명 이름과 URL을 입력하고 **Add**를 클릭합니다.
    6. Redis 노드의 Output 섹션에서 Conversational Agent 노드의 Memory Inputs 섹션으로 선을 그려 Redis-Backed Chat Memory 노드를 Conversational Agent 노드에 연결합니다.
    7. **Save Chatflow**를 클릭하여 진행상황을 저장합니다.

## 결과:
이 단계들을 따르면 대화할 수 있고 질문할 수 있는 conversational agent를 성공적으로 만들 수 있습니다.

## 다음 단계:
채팅 아이콘을 클릭하여 새로 만든 conversational agent와 상호작용합니다. Redis를 로컬에서 실행하는 경우, 채팅을 시작하기 전에 Redis용 Docker 컨테이너가 실행 중인지 확인하십시오.

## 관련 링크 및 문제 해결:
추가 정보 및 문제 해결은 https://redis.io/tutorials/howtos/solutions/flowise/conversational-agent/를 참조하십시오.


