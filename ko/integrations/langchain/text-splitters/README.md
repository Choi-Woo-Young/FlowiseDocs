---
description: LangChain Text Splitter Node
---

# Text Splitters

***

**긴 텍스트를 다루고자 할 때는 해당 텍스트를 청크(chunk)로 나누는 것이 필요합니다.**\
간단해 보이지만, 여기에는 많은 잠재적 복잡성이 존재합니다. 이상적으로는 의미적으로 관련된 텍스트 조각들을 함께 유지하고 싶을 것입니다. "의미적으로 관련된"이 무엇을 의미하는지는 텍스트의 유형에 따라 달라질 수 있습니다. 이 노트북은 이를 수행하는 여러 가지 방법을 보여줍니다.

**상위 수준에서 text splitter는 다음과 같이 작동합니다:**

1. 텍스트를 작고 의미적으로 의미 있는 청크(주로 문장)로 나눕니다.
2. 이러한 작은 청크들을 특정 크기(어떤 함수로 측정됨)에 도달할 때까지 더 큰 청크로 결합하기 시작합니다.
3. 그 크기에 도달하면 해당 청크를 자체적인 텍스트 조각으로 만들고, 약간의 중첩(청크 간 컨텍스트를 유지하기 위해)을 두고 새로운 텍스트 청크를 생성하기 시작합니다.

**즉, text splitter를 커스터마이징할 수 있는 두 가지 다른 축이 있습니다:**

1. 텍스트를 나누는 방법
2. 청크 크기를 측정하는 방법

### Text Splitter Node:

* [Character Text Splitter](character-text-splitter.md)
* [Code Text Splitter](code-text-splitter.md)
* [Html-To-Markdown Text Splitter](html-to-markdown-text-splitter.md)
* [Markdown Text Splitter](markdown-text-splitter.md)
* [Recursive Character Text Splitter](recursive-character-text-splitter.md)
* [Token Text Splitter](token-text-splitter.md)
