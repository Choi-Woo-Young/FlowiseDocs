---
description: Airtable 테이블의 쿼리에 답변하는 데 사용되는 Agent입니다.
---

# Airtable Agent

<figure><img src="../../../.gitbook/assets/image_airtable.png" alt="" width="271"><figcaption><p>Airtable Agent Node</p></figcaption></figure>

## Airtable Agent 기능

Airtable Agent는 Flowise AI와 Airtable 테이블 간의 상호작용을 촉진하도록 설계되었으며, 사용자가 대화 방식으로 Airtable 데이터를 쿼리할 수 있게 합니다. 이 agent를 사용하면 사용자는 Airtable 베이스의 내용에 대해 질문하고 저장된 데이터에 기반한 관련 응답을 받을 수 있습니다. 이는 특정 정보를 신속하게 추출하거나, 워크플로우를 자동화하거나, Airtable에 저장된 데이터로부터 요약을 생성하는 데 특히 유용할 수 있습니다.

예를 들어 Airtable Agent는 다음과 같은 질문에 답변하는 데 사용될 수 있습니다:

* "내 프로젝트 추적 테이블에서 아직 완료되지 않은 작업은 몇 개입니까?"
* "CRM에 나열된 클라이언트의 연락처 정보는 무엇입니까?"
* "지난 주에 추가된 모든 기록의 요약을 주십시오."

이 기능은 사용자가 Airtable 인터페이스를 탐색할 필요 없이 Airtable 베이스에서 인사이트를 얻을 수 있도록 도와주며, 데이터를 원활하고 대화식으로 관리하고 분석하기가 더 쉬워집니다.

## 입력 항목

Airtable Agent가 효과적으로 작동하려면 다음 입력이 필요합니다:

* **Language Model**: 쿼리 처리에 사용될 언어 모델입니다. 이 입력은 필수이며 agent가 제공하는 응답의 품질과 정확도를 결정하는 데 도움이 됩니다.
* **Input Moderation**: 콘텐츠 조정을 활성화하는 선택적 입력입니다. 이는 쿼리가 적절하며 불쾌하거나 해로운 콘텐츠를 포함하지 않도록 보장하는 데 도움이 됩니다.
* **Connect Credential**: Airtable에 연결하기 위한 필수 입력입니다. 사용자는 Airtable 데이터에 접근할 수 있는 권한을 가진 적절한 자격증명을 선택해야 합니다.
* **Base ID**: 연결할 Airtable 베이스의 ID입니다. 이는 필수 필드이며 Airtable API 문서 또는 베이스 설정에서 찾을 수 있습니다. 테이블 URL이 `https://airtable.com/app11RobdGoX0YNsC/tblJdmvbrgizbYlCO/viw9UrP77idOCE4ee`처럼 보이면 `app11RobdGoX0YNsC`가 Base ID입니다. 이는 쿼리할 데이터를 포함하는 Airtable 베이스를 지정하는 데 사용됩니다.
* **Table ID**: Airtable 베이스 내 특정 테이블의 ID입니다. 이것도 필수 필드이며 agent가 데이터 검색을 위해 올바른 테이블을 대상으로 하는 데 도움이 됩니다. 예제 URL `https://airtable.com/app11RobdGoX0YNsC/tblJdmvbrgizbYlCO/viw9UrP77idOCE4ee`에서 `tblJdmvbrgizbYlCO`가 Table ID입니다.
* **Additional Parameters**: agent의 동작을 사용자 정의하는 데 사용할 수 있는 선택적 매개변수입니다. 이러한 매개변수는 특정 사용 사례에 따라 구성할 수 있습니다.
  * **Return All**: 이 옵션을 사용하면 지정된 테이블의 모든 기록을 반환할 수 있습니다. 활성화되면 모든 기록이 검색되고, 그렇지 않으면 제한된 수의 기록만 반환됩니다.
  * **Limit**: **Return All**이 활성화되지 않은 경우 반환할 기록의 최대 수를 지정합니다. 기본값은 `100`입니다.

**참고**: 이 섹션은 진행 중입니다. 이 섹션을 완성하는 데 도움을 주실 수 있다면 감사하겠습니다. 시작하려면 [Contribution Guide](/broken/pages/G48tdmpQ3z4CTWEspqkA)를 확인해 주십시오.
