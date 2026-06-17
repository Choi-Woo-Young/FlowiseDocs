---
description: >-
  확장 가능한 오픈소스 벡터 데이터베이스인 Weaviate를 사용하여 임베딩된 데이터를 upsert하고 유사도 또는 mmr 검색을 수행합니다.
---
# Weaviate

<figure><img src="../../../.gitbook/assets/image (165).png" alt="" width="295"><figcaption><p>Weaviate Node</p></figcaption></figure>

## 필터링

Weaviate는 필터링과 관련하여 다음 [구문](https://weaviate.io/developers/weaviate/search/filters)을 지원합니다:

**UI**

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (2).png" alt="" width="227"><figcaption></figcaption></figure>

**API**```json
"overrideConfig": {
    "weaviateFilter": {
        "where": {
            "operator": "Equal",
            "path": [
                "test"
            ],
            "valueText": "key"
        }
    }
}
```## 리소스

* [LangchainJS Weaviate](https://js.langchain.com/v0.1/docs/integrations/vectorstores/weaviate/#usage-query-documents)
* [Weaviate Filtering](https://weaviate.io/developers/weaviate/search/filters)

{% hint style="info" %}
이 섹션은 작업 중입니다. 이 섹션을 완성하는 데 도움을 주시면 감사하겠습니다. 시작하려면 [기여 가이드](/broken/pages/G48tdmpQ3z4CTWEspqkA)를 확인해 주세요.
{% endhint %}