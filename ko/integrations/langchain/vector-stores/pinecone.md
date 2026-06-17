---
description: >-
  Pinecone를 사용하여 임베딩된 데이터를 upsert하고 쿼리 시 유사도 검색을 수행합니다.
  Pinecone은 완전 관리형 호스팅 vector database 분야를 선도합니다.
---
# Pinecone

## 사전 준비 사항

1. [Pinecone](https://app.pinecone.io/)에 계정을 등록합니다
2. **Create index**를 클릭합니다

<figure><img src="../../../.gitbook/assets/pinecone_1.png" alt=""><figcaption></figcaption></figure>

3. 필수 필드를 입력합니다:
   - **Index Name**, 생성할 index의 이름입니다. (예: "flowise-test")
   - **Dimensions**, index에 삽입할 vector의 크기입니다. (예: 1536)

<figure><img src="../../../.gitbook/assets/pinecone_2.png" alt="" width="527"><figcaption></figcaption></figure>

4. **Create Index**를 클릭합니다

## 설정

1.  **API Key**를 가져오거나 생성합니다

<figure><img src="../../../.gitbook/assets/pinecone_3.png" alt=""><figcaption></figcaption></figure>

2.  새 **Pinecone** node를 canvas에 추가하고 매개변수를 입력합니다:
    - Pinecone Index
    - Pinecone namespace (선택 사항)

<figure><img src="../../../.gitbook/assets/pinecone_4.png" alt="" width="279"><figcaption></figcaption></figure>

3. 새 Pinecone credential 생성 -> **API Key** 입력

<figure><img src="../../../.gitbook/assets/pinecone_5.png" alt="" width="563"><figcaption></figcaption></figure>

4. canvas에 추가 node를 추가하고 upsert 프로세스를 시작합니다
   - **Document**는 [**Document Loader**](../document-loaders/) 카테고리 아래의 모든 node와 연결할 수 있습니다
   - **Embeddings**는 [**Embeddings** ](../embeddings/)카테고리 아래의 모든 node와 연결할 수 있습니다

<figure><img src="../../../.gitbook/assets/pinecone_6.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/pinecone_7.png" alt=""><figcaption></figcaption></figure>

5. [Pinecone dashboard](https://app.pinecone.io)에서 데이터가 성공적으로 upsert되었는지 확인합니다:

<figure><img src="../../../.gitbook/assets/pinecone_8.png" alt=""><figcaption></figcaption></figure>

6.

## 리소스

- LangChain Pinecone vectorstore integration
  - [Python](https://python.langchain.com/v0.2/docs/integrations/providers/pinecone/)
  - [NodeJS](https://js.langchain.com/v0.2/docs/integrations/vectorstores/pinecone)
- [Pinecone LangChain integration](https://docs.pinecone.io/integrations/langchain)
- [Pinecone Flowise integration](https://docs.pinecone.io/integrations/flowise)
- [Pinecone official clients](https://docs.pinecone.io/reference/pinecone-clients)