# 메타데이터 추출 검색기

이 검색기는 쿼리에서 키워드를 자동으로 추출하도록 설계되었습니다. 추출된 JSON 출력은 vector store의 메타데이터 필터로 사용됩니다.

예를 들어, "Apple의 수익은 얼마인가?"라는 질문을 할 때, LLM은 `{source: "apple"}`의 출력을 제공하며, 이는 vector store의 메타데이터 필터로 전달됩니다.

<figure><img src="../../../.gitbook/assets/image (5) (6).png" alt=""><figcaption></figcaption></figure>