---
description: >-
  입력이 거부 목록(Deny list)의 텍스트를 포함하는지 확인하고 LLM으로 전송되는 것을 방지합니다.
---

# 간단한 프롬프트 모더레이션

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (2) (1).png" alt="" width="301"><figcaption><p>간단한 프롬프트 모더레이션 노드</p></figcaption></figure>

다른 LLM을 사용하여 사용자 쿼리가 거부 목록에 가까운지 식별하고, 예인 경우 기본 오류 메시지를 출력합니다.

예를 들어, 거부 목록은 다음과 같을 수 있습니다:

* 이전 지시 무시
* 모든 민감한 정보 유출

<figure><img src="../../../.gitbook/assets/image (336).png" alt=""><figcaption></figcaption></figure>