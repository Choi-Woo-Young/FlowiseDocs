---
description: >-
  관리형 클라우드 mongodb 데이터베이스인 MongoDB Atlas를 사용하여 임베딩된 데이터를 upsert하고 쿼리 시 유사도 또는 mmr
  검색을 수행합니다.
---
# MongoDB Atlas

<figure><img src="../../../.gitbook/assets/image (161).png" alt="" width="308"><figcaption><p>MongoDB Atlas Node</p></figcaption></figure>

### Cluster 구성[​](https://js.langchain.com/docs/integrations/vectorstores/mongodb_atlas/#initial-cluster-configuration) <a href="#initial-cluster-configuration" id="initial-cluster-configuration"></a>

MongoDB Atlas cluster를 설정하려면 [MongoDB Atlas ](https://www.mongodb.com/)웹사이트로 이동하여 계정이 없는 경우 가입하세요. 메시지가 표시되면 cluster를 생성하고 이름을 지정하세요. 이 cluster는 Database 섹션 아래에 나타납니다. 그런 다음 "**Browse Collections**"를 선택하여 새 collection을 생성하거나 제공된 샘플 데이터 중 하나를 사용하세요.

{% hint style="warning" %}
생성하는 cluster가 7.0 버전 이상인지 확인하세요.
{% endhint %}

### Index 생성

cluster를 설정한 후, 다음 단계는 검색하려는 collection 필드에 대한 Index를 생성하는 것입니다.

1. **Atlas Search** 탭으로 이동하여 **Create Search Index**를 클릭하세요.
2. **Atlas Vector Search - JSON Editor**를 선택하고, 적절한 database와 collection을 선택한 다음, 다음 내용을 텍스트 상자에 붙여넣으세요:```json
{
  "fields": [
    {
      "numDimensions": 1536,
      "path": "embedding",
      "similarity": "euclidean",
      "type": "vector"
    }
  ]
}
````numDimensions` 속성이 사용 중인 embeddings의 차원 수와 일치하는지 확인하세요. 예를 들어, Cohere embeddings는 일반적으로 1024 차원을 가지며, OpenAI embeddings는 기본적으로 1536 차원을 가집니다.

**참고:** Vector Store는 다음과 같은 특정 기본값을 기대합니다:

* Index 이름은 `default`
* Collection 필드 이름은 `embedding`
* 원시 텍스트 필드 이름은 `text`

위 예시에서 보여준 것처럼, Index 및 Collection 스키마와 일치하는 필드 이름으로 Vector Store를 초기화하세요.

이 작업이 완료되면 Index 빌드를 진행하세요.

{% hint style="info" %}
이 섹션은 작업 중입니다. 이 섹션을 완성하는 데 도움을 주시면 감사하겠습니다. 시작하려면 [기여 가이드](/broken/pages/G48tdmpQ3z4CTWEspqkA)를 확인하세요.
{% endhint %}

### Flowise 구성

MongoDB Atlas Vector Store를 드래그 앤 드롭하고 새 Credential을 추가하세요. MongoDB Atlas dashboard에서 제공된 연결 문자열을 사용하세요:

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

나머지 필드를 채우세요:

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (2) (1).png" alt="" width="252"><figcaption></figcaption></figure>

추가 매개변수(Additional Parameters)에서 더 자세한 내용을 구성할 수도 있습니다:

<figure><img src="../../../.gitbook/assets/image (164).png" alt="" width="518"><figcaption></figcaption></figure>