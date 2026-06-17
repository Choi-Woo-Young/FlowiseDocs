---
description: >-
  Meta의 Faiss 라이브러리를 사용하여 임베딩된 데이터를 upsert하고 유사도 검색을 수행합니다.
---

# Faiss

Faiss는 조밀 벡터의 효율적인 유사도 검색 및 클러스터링을 위한 라이브러리입니다. 클라우드 Vector Store와 달리 Faiss는 로컬 머신에서 실행되며 파일 시스템에 데이터를 저장합니다.

<figure><img src="../../../.gitbook/assets/image (158).png" alt="" width="307"><figcaption><p>Faiss Node</p></figcaption></figure>

## 사전 요구사항

### 방법 1: NPM/Source 설치
로컬 설치의 경우 머신이 C++ 모듈을 컴파일할 수 있는지 확인합니다.
* **Linux:** `build-essential`을 설치합니다.
* **MacOS:** `xcode-select --install`을 실행하여 Clang/C++ 도구를 획득합니다.
* **Windows:** Visual Studio Build Tools 및 Python을 설치합니다.

### 방법 2: Docker
Docker를 사용하여 Flowise를 실행 중이면 Faiss를 바로 사용할 수 있습니다.

## 설정

### 입력

| Input | Description |
| :--- | :--- |
| **Document** | Document Loader 카테고리에서 모든 노드를 연결합니다. |
| **Embeddings** | Embeddings 카테고리에서 모든 노드를 연결합니다. |

### 매개변수

* **Base Path:** Index 파일(`faiss.index`과 `docstore.json`)이 저장될 폴더 경로입니다.
    * 비워둔 경우 데이터가 RAM에 저장되며 Flowise가 다시 시작되면 손실됩니다.
    * **Docker 경로 예시:** `/root/.flowise/faiss`
    * > **참고:** 컨테이너 재시작 시 데이터 손실을 방지하기 위해 경로가 `docker-compose.yml` 파일의 volume으로 매핑되어 있는지 확인합니다.
    * **로컬 경로 예시:** `C:\Users\YourName\flowise_data`

## 구성 및 수집

1.  캔버스에 새 **Faiss** 노드를 추가합니다.
2.  **Faiss** 노드의 **Base Path** 필드에 폴더 경로를 입력합니다.
3.  Document Loader와 Embeddings 노드를 **Faiss** 노드에 연결합니다.
4.  **Upsert Vector Database**를 클릭하여 문서를 처리합니다.

## 확인

데이터가 upsert되었는지 확인하려면 **Base Path** 필드에서 지정한 폴더로 이동합니다. `faiss.index`와 `docstore.json` 파일이 보여야 합니다.

## 리소스
* [LangChain JS Faiss 문서](https://docs.langchain.com/oss/javascript/integrations/vectorstores/faiss)
