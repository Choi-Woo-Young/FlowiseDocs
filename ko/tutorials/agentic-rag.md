# 에이전트형 RAG

에이전트형 RAG는 [RAG](rag.md)를 조직화된 방식으로 수행하는 에이전트 기반 접근 방식입니다. 다양한 문서 소스에서 데이터를 검색하고, 요약을 비교하며, 자동 자체 수정 메커니즘을 구현하는 것이 포함될 수 있습니다.

이 튜토리얼에서는 검색된 데이터의 관련성을 확인하고 결과가 관련이 없으면 자동으로 쿼리를 재생성하는 자체 수정 RAG 시스템을 만드는 방법을 살펴봅니다.

## 개요

에이전트형 RAG 흐름은 다음을 수행하는 다단계 프로세스를 구현합니다:

1. 들어오는 쿼리를 검증하고 분류합니다.
2. 벡터 데이터베이스 검색을 위한 최적화된 검색 쿼리를 생성합니다.
3. 검색된 문서의 관련성을 평가합니다.
4. 결과가 관련이 없을 때 쿼리를 재생성하여 자체 수정합니다.
5. 검색된 정보를 기반으로 상황에 맞는 응답을 제공합니다.

<figure><img src="../.gitbook/assets/image (16) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 1단계: Start 노드 설정

캔버스에 **Start** 노드를 추가하여 시작합니다. 이 노드는 에이전트 흐름의 진입점 역할을 합니다.

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **Input Type**: "Chat Input"을 선택하여 사용자 질문을 허용합니다.
* **Flow State**: 키 "`query`"와 빈 값을 가진 상태 변수를 추가합니다.

Start 노드는 프로세스 전체에서 업데이트될 빈 `query` 변수를 사용하여 흐름 상태를 초기화합니다.

### 2단계: 쿼리 검증 추가

**Condition Agent** 노드를 추가하고 Start 노드에 연결합니다.

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **Instructions**: "사용자가 AI 관련 주제에 대해 질문하는지 또는 일반 쿼리인지 확인하세요"
* **Input**: `{{ question }}` (사용자의 입력을 참조합니다)
* **Scenarios**:
  * 시나리오 1: "AI Related"
  * 시나리오 2: "General"

이 노드는 라우터 역할을 하며, 쿼리에 전문 AI 지식이 필요한지 또는 일반적으로 답할 수 있는지를 결정합니다.

### 3단계: 일반 응답 브랜치 생성

AI와 관련이 없는 쿼리의 경우 조건 에이전트의 출력 1에 연결된 **LLM** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

이는 문서 검색이 필요 없는 일반 쿼리에 대한 직접적인 응답을 제공합니다. Direct Reply 노드로 바꾸어 미리 정의된 답변을 반환할 수도 있습니다.

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

### 4단계: 쿼리 생성 설정

AI 관련 쿼리의 경우 조건 에이전트의 출력 0에 연결된 **LLM** 노드를 추가합니다. 이는 "AI 관련" 시나리오입니다.

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

*   **Messages**: 시스템 메시지를 추가합니다:

    ```
    Given the user question and history, construct a short string that can be used for searching vector database. Only generate the query, no meta comments, no explanation

    Example:
    Question: what are the events happening today?
    Query: today's event

    Example:
    Question: how about the address?
    Query: business address of the shop

    Question: {{ question }}
    Query:
    ```
* **Update Flow State**: 키 "query"를 `{{ output }}`으로 설정합니다. 이렇게 하면 "query" 값이 이 LLM 노드의 출력으로 업데이트됩니다.

이 노드는 사용자의 자연어 질문을 벡터 데이터베이스를 위한 최적화된 검색 쿼리로 변환합니다.

### 5단계: 벡터 데이터베이스 리트리버 구성

**Retriever** 노드를 추가하고 "Generate Query" LLM에 연결합니다.

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **Knowledge (Document Stores)**: 미리 구성된 문서 저장소를 선택합니다(예: "ai paper").
* **Retriever Query**: `{{ $flow.state.query }}` (공유 상태에서 "query" 값을 사용합니다)

이 노드는 최적화된 쿼리를 사용하여 벡터 데이터베이스를 검색하고 관련 문서를 반환합니다.

### 6단계: 문서 관련성 확인 추가

Retriever에 연결된 다른 **Condition Agent** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (11) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **Instructions**: "문서가 사용자 질문과 관련이 있는지 결정하세요. 사용자 질문은 \{{ question \}}"
* **Input**: `{{ retrieverAgentflow_0 }}` (5단계에서 검색된 문서를 참조합니다)
* **Scenarios**:
  * 시나리오 1: "Relevant"
  * 시나리오 2: "Irrelevant"

이는 검색된 문서가 실제로 사용자의 질문과 관련된 정보를 포함하는지 평가합니다.

### 7단계: 최종 응답 생성기 생성

관련 문서의 경우 관련성 검사자의 출력 0에 연결된 **LLM** 노드를 추가합니다. 이는 "Relevant" 시나리오와 일치할 때입니다.

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1) (1).png" alt="" width="373"><figcaption></figcaption></figure>

#### 구성:

*   **Input Message**:

    ```
    Given the question: {{ question }}
    And the findings: {{ retrieverAgentflow_0 }}
    Output the final response
    ```

이 노드는 사용자의 질문과 관련 검색 문서를 결합하여 최종 답변을 만듭니다.

### 8단계: 자체 수정 구현

관련이 없는 문서의 경우 관련성 검사자의 출력 1에 연결된 **LLM** 노드를 추가합니다. 이는 두 번째 시나리오인 "Irrelevant"입니다.

<figure><img src="../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (14) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **Messages**: 시스템 메시지를 추가합니다: "You are a helpful assistant that can transform the query to produce a better question."
*   **Input Message**:

    ```
    Look at the input and try to reason about the underlying semantic intent / meaning.
    Here is the initial question: {{ $flow.state.query }}
    Formulate an improved question:
    ```
* **Update Flow State**: 키 "query"를 `{{ output }}`으로 설정합니다.

<figure><img src="../.gitbook/assets/image (15) (1) (1) (1) (1).png" alt="" width="520"><figcaption></figcaption></figure>

이 노드는 초기 쿼리가 관련 결과를 반환하지 않은 이유를 분석하고 개선된 버전을 생성합니다.

### 9단계: 루프백 메커니즘 추가

"Regenerate Question" LLM에 연결된 **Loop** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (16) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **Loop Back To**: "retrieverAgentflow\_0-Retriever Vector DB" 선택
* **Max Loop Count**: 5로 설정 (무한 루프 방지)

이는 초기 결과가 만족스럽지 않을 때 개선된 쿼리로 재시도할 수 있는 피드백 루프를 만듭니다.

## 완전한 흐름 구조

{% file src="../.gitbook/assets/Agentic RAG V2.json" %}

## 요약

1. Start → 쿼리 유효성 확인
2. 쿼리 유효성 확인(AI 관련) → 쿼리 생성
3. 쿼리 유효성 확인(일반) → 일반 답변
4. 쿼리 생성 → Retriever Vector DB
5. Retriever Vector DB → 문서 관련성 확인
6. 문서 관련성 확인(관련) → 응답 생성
7. 문서 관련성 확인(관련 없음) → 질문 재생성
8. 질문 재생성 → Retriever로 다시 루프

## 흐름 테스트

다양한 유형의 질문으로 흐름을 테스트합니다:

* AI 관련 쿼리: "What are the latest developments in machine learning?"
* 일반 쿼리: "What's the weather like today?"
* 개선이 필요할 수 있는 복잡한 쿼리: "How does that new technique work?"

<figure><img src="../.gitbook/assets/image (17) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

이 에이전트형 RAG는 단순하고 복잡한 쿼리를 모두 처리하면서 반복적 개선을 통해 높은 정확도를 유지할 수 있는 문서 기반 질문 답변 시스템을 제공합니다.
