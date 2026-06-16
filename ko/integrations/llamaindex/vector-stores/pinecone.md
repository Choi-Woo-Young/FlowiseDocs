---
description: >-
  Upsert embedded data and perform similarity search upon query using Pinecone,
  a leading fully managed hosted vector database.
---

# Pinecone

## 전제 조건

1. Register an account for [Pinecone](https://app.pinecone.io/)
2. Click **Create index**

<figure><img src="../../../.gitbook/assets/pinecone_1.png" alt=""><figcaption></figcaption></figure>

3. Fill in required fields:
   * **인덱스 Name**, name of the index to be created. (e.g. "flowise-test")
   * **Dimensions**, size of the vectors to be inserted in the index. (e.g. 1536)

<figure><img src="../../../.gitbook/assets/pinecone_2.png" alt="" width="527"><figcaption></figcaption></figure>

4. Click **Create 인덱스**

## 설정

1. Get/Create your **API 키**

<figure><img src="../../../.gitbook/assets/pinecone_3.png" alt=""><figcaption></figcaption></figure>

2. 추가 a new **Pinecone** node to canvas and fill in the parameters:
   * Pinecone 인덱스
   * Pinecone namespace (optional)

<figure><img src="../../../.gitbook/assets/pinecone_llamaindex.png" alt="" width="301"><figcaption><p>Pinecone 노드</p></figcaption></figure>

3. Create new Pinecone credential -> Fill in **API 키**

<figure><img src="../../../.gitbook/assets/pinecone_5.png" alt="" width="563"><figcaption></figcaption></figure>

4. 추가 additional nodes to canvas and start the upsert process
   *   **Document** can be connected with any node under [**Document Loader**](../../langchain/document-loaders/) category

       <div data-gb-custom-block data-tag="hint" data-style="info" class="hint hint-info"><p>Document loaders and text splitters for LlamaIndex are not yet available, but using one of the ones available under LangChain will still allow querying with LlamaIndex as normal.</p></div>

\- \*\*Embeddings\*\* can be connected with any node under \[\*\*Embeddings\*\* ]\(../embeddings/)category

<figure><img src="../../../.gitbook/assets/pinecone_llama_chatflow.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/pinecone_llama_upsert.png" alt=""><figcaption></figcaption></figure>

5. Verify on [Pinecone dashboard](https://app.pinecone.io) that data has been successfully upserted:

<figure><img src="../../../.gitbook/assets/pinecone_8.png" alt=""><figcaption></figcaption></figure>
