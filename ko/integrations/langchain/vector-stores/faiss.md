---

description: >-
  Upsert embedded data and perform similarity search using the FAISS library from Meta.

---


# FAISS

FAISS is a library for efficient similarity search and clustering of dense vectors. Unlike cloud 벡터 저장소, FAISS runs locally on your machine and saves data to your file system.

<figure><img src="../../../.gitbook/assets/image (158).png" alt="" width="307"><figcaption><p>FAISS Node</p></figcaption></figure>

## 사전 요구사항

### Method 1: NPM/Source 설치
For local installations, ensure your machine can compile C++ modules.
* **Linux:** Install `build-essential`.
* **MacOS:** Run `xcode-select --install` to get Clang/C++ 도구.
* **Windows:** Install Visual Studio Build 도구 and Python.

### Method 2: Docker
If you are running Flowise using Docker, FAISS is ready to use.

## 설정

### Inputs

| Input | Description |
| :--- | :--- |
| **Document** | Connect any node from the Document Loader category. |
| **Embeddings** | Connect any node from the Embeddings category. |

### 매개변수

* **Base Path:** The folder path where the index files (`FAISS.index` and `docstore.json`) will be saved.
    * If left blank, data is stored in RAM and will be lost when Flowise restarts.
    * **Docker Path 예시:** `/root/.flowise/FAISS`
    * > **Note:** Ensure the path is mapped to a volume in your `docker-compose.yml` file to prevent data loss upon container restart.
    * **Local Path 예시:** `C:\Users\YourName\flowise_data`

## 설정 and Ingestion

1.  Add a new **FAISS** node on the canvas.
2.  Enter a folder path in the **FAISS** node’s **Base Path** field.
3.  Connect your Document Loader and Embeddings nodes to the **FAISS** node.
4.  Click **Upsert Vector Database** to process your documents.

## Verify

To verify your data has been upserted, navigate to the folder you specified in the **Base Path** field. You should see files `FAISS.index` and `docstore.json`.

## Resources
* [LangChain JS FAISS Documentation](https://docs.langchain.com/oss/javascript/integrations/vectorstores/faiss)
