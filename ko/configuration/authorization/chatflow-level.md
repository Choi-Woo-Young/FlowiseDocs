---
description: Flowise 인스턴스에 대한 Chatflow 수준 접근 제어를 설정하는 방법을 알아봅니다
---

# Flows

***

Chatflow / Agentflow를 구성하고 나면, 기본적으로 해당 플로우는 누구나 접근할 수 있는 공개 상태입니다. Chatflow ID에 접근할 수 있는 사람은 누구나 Embed 또는 API를 통해 예측(prediction)을 실행할 수 있습니다.

특정 사용자에게만 접근과 상호작용을 허용하고 싶은 경우, 해당 Chatflow에 API 키를 할당하여 이를 구현할 수 있습니다.

## API 키

대시보드에서 API Keys 섹션으로 이동하면 생성된 DefaultKey를 확인할 수 있습니다. 키를 추가하거나 삭제할 수도 있습니다.

<figure><img src="../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Chatflow

Chatflow로 이동하면, 이제 해당 Chatflow를 보호하는 데 사용할 API 키를 선택할 수 있습니다.

<figure><img src="../../.gitbook/assets/image (16) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

API 키를 할당한 후에는, HTTP 호출 시 Authorization 헤더에 지정된 올바른 API 키를 제공해야만 Chatflow API에 접근할 수 있습니다.

__CODE_BLOCK_0__

POSTMAN을 사용하여 API를 호출하는 예시입니다.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
