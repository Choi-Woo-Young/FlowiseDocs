---
description: LangChain Text Splitter 노드
---

# Text Splitters

***

**긴 텍스트 부분을 다루고 싶을 때는 해당 텍스트를 청크로 분할해야 합니다.**\
간단하게 들리지만 여기에는 많은 복잡성이 있을 수 있습니다. 이상적으로는 의미론적으로 관련된 텍스트 부분을 함께 유지하고 싶습니다. "의미론적으로 관련된"의 의미는 텍스트의 유형에 따라 달라질 수 있습니다. 이 노트북은 그렇게 하는 여러 방법을 보여줍니다.

**높은 수준에서 텍스트 분할기는 다음과 같이 작동합니다:**

1. 텍스트를 작고 의미론적으로 의미 있는 청크 (종종 문장)로 분할합니다.
2. 특정 크기에 도달할 때까지 이러한 작은 청크를 더 큰 청크로 결합하기 시작합니다 (일부 함수로 측정됨).
3. 해당 크기에 도달하면 해당 청크를 텍스트의 자체 부분으로 만든 다음 일부 겹침이 있는 새 텍스트 청크 만들기를 시작합니다 (청크 간 컨텍스트를 유지하기 위해).

**이는 Text Splitter를 사용자 정의할 수 있는 두 가지 축이 있음을 의미합니다:**

1. 텍스트를 분할하는 방식
2. 청크 크기를 측정하는 방식

### Text Splitter 노드:

* [Character Text Splitter](character-text-splitter.md)
* [Code Text Splitter](code-text-splitter.md)
* [Html-To-Markdown Text Splitter](html-to-markdown-text-splitter.md)
* [Markdown Text Splitter](markdown-text-splitter.md)
* [Recursive Character Text Splitter](recursive-character-text-splitter.md)
* [Token Text Splitter](token-text-splitter.md)
