# Mem0 Memory

[Mem0](https://github.com/mem0ai/mem0) ("mem-zero"로 발음)는 AI 어시스턴트와 에이전트에 지능형 메모리 레이어를 추가하여 개인화된 AI 상호작용을 가능하게 합니다. 사용자 선호도를 기억하고, 개별 요구에 적응하며, 시간이 지나면서 지속적으로 개선됩니다. 이는 고객 지원 챗봇, AI 어시스턴트, 자율형 AI 에이전트 등의 애플리케이션에 이상적입니다.

Mem0은 포괄적인 메모리 관리 기능 모음을 제공하여 다양한 AI 기반 애플리케이션에 원활하게 통합될 수 있습니다.

---

## Flowise와 함께 Mem0 사용하기

Mem0을 Flowise와 통합하려면 다음 단계를 따르세요:

### 1. Flowise 설정하기

1. Flowise 애플리케이션을 열고 새 캔버스를 생성하거나 Flowise 마켓플레이스에서 템플릿을 선택합니다.
2. 이 예제에서는 **Conversation Chain** 템플릿을 사용합니다.
3. 기본 **Buffer Memory**를 **Mem0 Memory**로 교체합니다.

<figure><img src="../../../.gitbook/assets/mem0/flowise-flow.png" alt="Flowise Memory Integration"><figcaption>Mem0과의 Flowise 통합</figcaption></figure>

### 2. Mem0 API 키 획득하기

1. [Mem0 API 키 대시보드](https://app.mem0.ai/dashboard/api-keys)로 이동합니다.
2. Mem0 API 키를 생성하거나 기존 키를 복사합니다.

<figure><img src="../../../.gitbook/assets/mem0/api-key.png" alt="Mem0 API Key"><figcaption>Mem0에서 API 키 검색</figcaption></figure>

### 3. Flowise에서 Mem0 자격증명 구성하기

1. Mem0 자격증명 섹션에 **Mem0 API Key**를 입력합니다.

<figure><img src="../../../.gitbook/assets/mem0/creds.png" alt="Mem0 Credentials"><figcaption>API 자격증명 구성</figcaption></figure>

### 4. Chatflow 저장 및 테스트하기

1. Flowise 구성을 저장합니다.
2. 테스트 채팅을 실행하고 일부 정보를 저장합니다.

<figure><img src="../../../.gitbook/assets/mem0/flowise-chat-1.png" alt="Flowise Test Chat"><figcaption>메모리 저장 테스트</figcaption></figure>

### 5. Mem0 대시보드에서 저장된 메모리 확인하기

1. [Mem0 대시보드](https://app.mem0.ai/dashboard/requests)를 방문하여 저장된 메모리를 검토합니다.

<figure><img src="../../../.gitbook/assets/mem0/flowise-memory.png" alt="Mem0 Stored Memories"><figcaption>저장된 메모리 검토</figcaption></figure>

### 6. 메모리 보존 확인하기

1. Flowise에서 채팅 기록을 지웁니다.
2. 이전에 저장된 정보를 기반으로 질문을 하여 보존을 확인합니다.

<figure><img src="../../../.gitbook/assets/mem0/flowise-chat-2.png" alt="Testing Memory Retention"><figcaption>메모리 지속성 확인</figcaption></figure>

---

## 추가 설정

Mem0는 다양한 사용자 정의 옵션을 제공합니다:

<figure><img src="../../../.gitbook/assets/mem0/settings.png" alt="Mem0 Settings"><figcaption>Mem0 구성 옵션</figcaption></figure>

1. **Search Only Mode**: 새로운 메모리를 생성하지 않고 메모리 검색을 활성화합니다. 채팅 기록은 수동으로 지워질 때까지 유지됩니다.
2. **Mem0 Entities**: `user_id`, `run_id`, `app_id`, `agent_id`와 같은 식별자를 활용하여 세분화된 메모리 제어를 수행합니다.
3. **Project ID**: 메모리 저장소를 특정 프로젝트에 할당합니다. [Mem0 Projects](https://app.mem0.ai/settings/projects/overview)를 통해 프로젝트를 관리합니다.
4. **Organization ID**: 메모리 저장소를 특정 조직에 할당합니다. [Mem0 Organizations](https://app.mem0.ai/settings/organizations/overview)를 통해 조직을 관리합니다.

---

## Mem0 플랫폼 구성

[Mem0 Project Settings](https://app.mem0.ai/dashboard/project-settings)에서 추가 구성을 사용할 수 있습니다:

1. **Custom Instructions**: 메모리 추출을 개선하기 위해 프로젝트 레벨의 지침을 정의합니다. 예: 학술 세부 정보만 추출합니다.
2. **Expiration Date**: 저장된 메모리에 대한 만료 기간을 설정하여 필요할 때 자동 데이터 삭제를 허용합니다.

<figure><img src="../../../.gitbook/assets/mem0/mem0-settings.png" alt="Mem0 Project Settings"><figcaption>프로젝트 레벨 설정 사용자 정의</figcaption></figure>

---

## Flowise에서 Mem0 자격증명 구성하기

Flowise에 자격증명을 추가하려면:

1. 자격증명 설정으로 이동합니다.
2. Mem0에 대한 새 자격증명 항목을 추가합니다.
3. [Mem0 API Key](https://app.mem0.ai/dashboard/api-keys)를 API Key 필드에 붙여넣습니다.

<figure><img src="../../../.gitbook/assets/mem0/api-key.png" alt="Adding API Key in Flowise"><figcaption>Flowise에서 API 키 입력</figcaption></figure>

---

이러한 구성을 통해 Flowise 설정이 Mem0과 원활하게 통합되어 향상된 메모리 보존 및 개인화된 AI 상호작용을 제공합니다.