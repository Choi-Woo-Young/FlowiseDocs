# 에이전트를 도구로 사용

이 튜토리얼에서는 다른 흐름을 부모 에이전트의 도구로 활용하는 방법을 살펴봅니다. 이 방식을 사용하면 특정 작업을 전문화된 자식 에이전트에게 위임할 수 있는 부모 에이전트를 만들 수 있습니다.

## 개요

1. 부모 에이전트를 통해 사용자 입력을 받습니다.
2. 에이전트는 문서 저장소에서 데이터를 검색하거나 Agentflow 도구를 호출하기로 결정합니다.

<figure><img src="../.gitbook/assets/image (295).png" alt="" width="375"><figcaption></figcaption></figure>

### 1단계: Start 노드 설정

캔버스에 **Start** 노드를 추가하여 시작합니다. 이 노드는 에이전트 시스템의 진입점 역할을 합니다.

### 2단계: 부모 에이전트 생성

**Agent** 노드를 추가하고 Start 노드에 연결합니다.

### 3단계: 에이전트 도구 구성

이 흐름의 핵심 기능은 다른 에이전트를 도구로 구성하는 것입니다. 부모 에이전트의 **Tools** 섹션에서:

<figure><img src="../.gitbook/assets/image (296).png" alt="" width="354"><figcaption></figcaption></figure>

#### 도구 구성:

* **Tool**: "**Agent As Tool**" 선택

#### 에이전트 도구 설정:

* **Selected Agentflow**: 자식 agentflow 선택
* **Name**: agentflow의 이름
* **Description**: 이 agentflow가 유용할 때를 설명합니다. 예:

```
Useful for searching user availability, scheduling meetings and email related query
```

{% hint style="warning" %}
도구의 이름과 설명은 매우 중요합니다! 명확하고 도구의 목적을 정확하게 설명해야 합니다. [모범 사례](https://platform.openai.com/docs/guides/function-calling?api-mode=chat#best-practices-for-defining-functions) 가이드를 참고하세요.
{% endhint %}

### 4단계: 지식 출처 추가

**Knowledge (Document Stores)** 섹션을 구성하여 부모 에이전트가 관련 정보에 액세스할 수 있도록 합니다. 이는 [RAG](rag.md) 튜토리얼과 동일합니다.

<figure><img src="../.gitbook/assets/image (297).png" alt="" width="518"><figcaption></figcaption></figure>

#### 문서 저장소 구성:

* **Document Store**: 미리 구성된 문서 저장소를 선택합니다(예: "AI-Paper").
* **Describe Knowledge**: 지식이 무엇에 관한 것인지 설명합니다.

***

## 상호 작용 예시

#### 샘플 쿼리 및 예상 동작:

**스케줄링 쿼리:**

* 사용자: "Can you check my availability for next Tuesday?"
* 흐름: 부모 에이전트 → personal\_assistant 도구 → 전문화된 스케줄링 응답

<figure><img src="../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

**기술 쿼리:**

* 사용자: "What is AIGC and how does it work?"
* 흐름: 부모 에이전트 → AI-Paper 지식 베이스 → 출처가 있는 기술 설명

<figure><img src="../.gitbook/assets/image (300).png" alt="" width="563"><figcaption></figcaption></figure>

**일반 쿼리:**

* 사용자: "Hello how are you?"
* 흐름: 부모 에이전트 → 직접 응답 (도구 불필요)

**복잡한 쿼리:**

* 사용자: "Schedule a meeting about AIGC implementation next Tuesday, extract key insights and the talking points"
* 흐름: 부모 에이전트 → personal\_assistant 도구 및 AI-Paper 지식 → 조율된 응답

<figure><img src="../.gitbook/assets/image (302).png" alt="" width="563"><figcaption></figcaption></figure>

***

## 모범 사례

#### 설계 지침:

1. **명확한 도구 설명**: 도구의 이름과 설명을 구체적이고 실행 가능하게 만듭니다.
2. **적절한 위임**: 부모 에이전트가 효과적으로 위임할 수 있도록 하는 더 나은 시스템 프롬프트

#### 일반적인 사용 사례:

* **고객 서비스**: 청구, 기술 지원, 일반 문의를 위한 전문화된 도구가 있는 부모 에이전트
* **연구 보조**: 다양한 연구 영역(법률, 기술, 시장 조사)을 위한 도구가 있는 부모
* **프로젝트 관리**: 스케줄링, 리소스 할당, 진행 상황 추적을 위한 도구가 있는 부모
* **콘텐츠 작성**: 작성, 편집, 연구, 서식 지정을 위한 도구가 있는 부모
