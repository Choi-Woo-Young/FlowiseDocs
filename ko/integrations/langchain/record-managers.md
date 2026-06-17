---
description: LangChain Record Manager 노드
---

# Record Manager

***

Record Manager는 인덱싱된 문서를 추적하여 [Vector Store](vector-stores/)에서 중복된 벡터 임베딩을 방지합니다.

문서 청크를 업서트할 때, 각 청크는 [SHA-1](https://github.com/emn178/js-sha1) 알고리즘을 사용하여 해시됩니다. 이 해시들은 Record Manager에 저장됩니다. 기존 해시가 있으면 임베딩 및 업서트 프로세스를 건너뜁니다.

경우에 따라 인덱싱 중인 새 문서와 동일한 소스에서 파생된 기존 문서를 삭제하고 싶을 수 있습니다. 이를 위해 Record Manager에는 3가지 정리 모드가 있습니다:

{% tabs %}
{% tab title="Incremental" %}
여러 문서를 업서트할 때 현재 업서트 프로세스의 일부가 아닌 기존 문서의 삭제를 방지하려면 **Incremental** 정리 모드를 사용하세요.

1. `Incremental` 정리 모드와 `source`를 SourceId Key로 하는 Record Manager가 있다고 가정해봅시다.

<div align="left"><figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="264"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="410"><figcaption></figcaption></figure></div>

2. 그리고 다음 2개의 문서를 가집시다:

| Text | Metadata         |
| ---- | ---------------- |
| Cat  | `{source:"cat"}` |
| Dog  | `{source:"dog"}` |

<div align="left"><figure><img src="../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="202"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (2).png" alt="" width="231"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure></div>

3. 업서트 후, 업서트된 2개의 문서를 볼 수 있습니다:

<figure><img src="../../.gitbook/assets/image (9) (1) (1) (1) (1) (2).png" alt="" width="433"><figcaption></figcaption></figure>

4. 이제 **Dog** 문서를 삭제하고 **Cat**을 **Cats**로 업데이트하면 다음을 볼 수 있습니다:

<figure><img src="../../.gitbook/assets/image (13) (2) (2).png" alt="" width="425"><figcaption></figcaption></figure>

* 원본 **Cat** 문서가 삭제됩니다
* **Cats**라는 새 문서가 추가됩니다
* **Dog** 문서는 건드리지 않습니다
* Vector Store의 남은 벡터 임베딩은 **Cats**와 **Dog**입니다

<figure><img src="../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1).png" alt="" width="448"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Full" %}
여러 문서를 업서트할 때 **Full** 정리 모드는 현재 업서트 프로세스의 일부가 아닌 모든 벡터 임베딩을 자동으로 삭제합니다.

1. `Full` 정리 모드의 Record Manager를 만들어봅시다. Full 정리 모드에는 SourceId Key가 필요하지 않습니다.

<div align="left"><figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="264"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (17) (1) (1) (1) (2).png" alt="" width="407"><figcaption></figcaption></figure></div>

2. 그리고 다음 2개의 문서를 가집시다:

| Text | Metadata         |
| ---- | ---------------- |
| Cat  | `{source:"cat"}` |
| Dog  | `{source:"dog"}` |

<div align="left"><figure><img src="../../.gitbook/assets/image (11) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="202"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (2).png" alt="" width="231"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure></div>

3. 업서트 후, 업서트된 2개의 문서를 볼 수 있습니다:

<figure><img src="../../.gitbook/assets/image (9) (1) (1) (1) (1) (2).png" alt="" width="433"><figcaption></figcaption></figure>

4. 이제 **Dog** 문서를 삭제하고 **Cat**을 **Cats**로 업데이트하면 다음을 볼 수 있습니다:

<figure><img src="../../.gitbook/assets/image (18) (1) (1) (1) (2).png" alt="" width="430"><figcaption></figcaption></figure>

* 원본 **Cat** 문서가 삭제됩니다
* **Cats**라는 새 문서가 추가됩니다
* **Dog** 문서가 삭제됩니다
* Vector Store의 남은 벡터 임베딩은 **Cats**뿐입니다

<figure><img src="../../.gitbook/assets/image (19) (1) (1) (1).png" alt="" width="527"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="None" %}
정리가 수행되지 않습니다
{% endtab %}
{% endtabs %}

현재 사용 가능한 Record Manager 노드는 다음과 같습니다:

* SQLite
* MySQL
* PostgresQL

## 리소스

* [LangChain Indexing - 작동 방식](https://js.langchain.com/docs/how_to/indexing/#how-it-works)