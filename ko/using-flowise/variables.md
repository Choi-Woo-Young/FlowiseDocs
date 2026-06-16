---
description: Flowise에서 변수를 사용하는 방법 배우기
---

# 변수

***

Flowise는 사용자가 노드에서 사용할 수 있는 변수를 생성할 수 있도록 합니다. 변수는 정적 또는 런타임일 수 있습니다.

### 정적

정적 변수는 지정된 값으로 저장되며 그대로 검색됩니다.

<figure><img src="../.gitbook/assets/image (13) (1) (1) (1) (1) (1).png" alt="" width="542"><figcaption></figcaption></figure>

### 런타임

변수의 값은 `process.env`를 사용하여 **.env** 파일에서 가져옵니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="537"><figcaption></figcaption></figure>

### API를 통한 변수 재정의 또는 설정

변수 값을 재정의하려면 우측 상단 버튼에서 명시적으로 활성화해야 합니다.

**설정** -> **구성** -> **보안** 탭:

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

기존 변수가 있으면 API에서 제공된 변수 값이 기존 값을 재정의합니다.

```json
{
    "question": "hello",
    "overrideConfig": {
        "vars": {
            "var": "some-override-value"
        }
    }
}
```

### 변수 사용

변수는 Flowise의 노드에서 사용할 수 있습니다. 예를 들어, **`character`**라는 변수가 생성되었습니다.

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>

다음 노드의 함수에서 변수를 **`$vars.<variable-name>`** 형식으로 사용할 수 있습니다.

* [Custom Tool](../integrations/langchain/tools/custom-tool.md)
* [Custom Function](../integrations/utilities/custom-js-function.md)
* [Custom Loader](../integrations/langchain/document-loaders/custom-document-loader.md)
* [If Else](../integrations/utilities/if-else.md)
* Custom MCP

<figure><img src="../.gitbook/assets/image (105).png" alt="" width="283"><figcaption></figcaption></figure>

또한 사용자는 다음 형식으로 모든 노드의 텍스트 입력에서 변수를 사용할 수 있습니다.

**`{{$vars.<variable-name>}}`**

예를 들어, Agent 시스템 메시지에서:

<figure><img src="../.gitbook/assets/image (1) (1) (1) (2) (1).png" alt="" width="508"><figcaption></figcaption></figure>

Prompt Template에서:

<figure><img src="../.gitbook/assets/image (157).png" alt=""><figcaption></figcaption></figure>

## 리소스

* [함수에 변수 전달](../integrations/langchain/tools/custom-tool.md#pass-variables-to-function)
