---
description: Custom Retriever는 사용자가 LLM에 전달할 컨텍스트의 형식을 지정할 수 있게 해줍니다.
---

# Custom Retriever

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (2) (1).png" alt="" width="298"><figcaption></figcaption></figure>

기본적으로 벡터 저장소에서 컨텍스트를 검색할 때 다음과 같은 형식으로 나타납니다:

```json
[ 
    {
        "pageContent": "This is an example",
        "metadata": {
            "source": "example.pdf"
        }
    },
    {
        "pageContent": "This is example 2",
        "metadata": {
            "source": "example2.txt"
        }
    }
]
```

배열의 **pageContent**는 문자열로 함께 연결되어 완성을 위해 LLM으로 다시 전달됩니다.

그러나 경우에 따라 source, link 등과 같이 LLM에 더 많은 정보를 제공하기 위해 metadata의 정보를 포함하고 싶을 수 있습니다. 이것이 **Custom Retriever**가 나오는 부분입니다. LLM으로 반환할 형식을 지정할 수 있습니다.

예를 들어 다음과 같은 형식을 사용하면:

```javascript
{{context}}
Source: {{metadata.source}}
```

다음과 같은 결합된 문자열이 생성됩니다:

```
This is an example
Source: example.pdf

This is example 2
Source: example2.txt
```

이는 LLM으로 다시 전송됩니다. LLM이 이제 답변의 출처를 가지고 있으므로 프롬프트를 사용하여 LLM에 답변 뒤에 인용을 붙여 답변을 반환하도록 지시할 수 있습니다.