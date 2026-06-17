# Chroma

## 사전 요구사항

Chroma 서버가 필요합니다. 다음 중 하나를 수행할 수 있습니다:

1. Chroma CLI를 설치하고 `chroma run`을 사용하여 서버를 실행합니다.
2. [Chroma Cloud](https://trychroma.com/home)에 가입합니다.
3. [Docker](https://docs.trychroma.com/guides/deploy/docker)에서 자신의 Chroma 인스턴스를 배포합니다.

## 설정

| Input           | Description                                                                                                                                        | Default               | Cloud |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----- |
| Document        | [Document Loader](../document-loaders/) 노드와 연결할 수 있습니다.                                                                           |                       |       |
| Embeddings      | [Embeddings](../embeddings/) 노드와 연결할 수 있습니다.                                                                                      |                       |       |
| Collection Name | Chroma collection 이름입니다. 명명 규칙에 대해서는 [여기](https://docs.trychroma.com/usage-guide#creating-inspecting-and-deleting-collections)를 참조하세요. |                       |       |
| Chroma URL      | Chroma 인스턴스의 URL을 지정합니다.                                                                                                            | http://localhost:8000 | https://api.trychroma.com:8000 |

Chroma Cloud의 경우 tenant ID를 얻고 데이터베이스 및 API 키를 생성해야 합니다.

<figure><img src="../../../.gitbook/assets/image (6) (1) (1) (1) (1) (2) (1).png" alt="" width="238"><figcaption></figcaption></figure>

### 추가사항

Flowise와 Chroma를 모두 Docker에서 실행하는 경우 추가 단계가 필요합니다.

1. 먼저 Chroma Docker를 실행합니다.

```bash
docker compose up -d --build
```

2. Flowise에서 `docker-compose.yml`을 엽니다.

```bash
cd Flowise && cd docker
```

3. 파일을 다음과 같이 수정합니다:

```sh
version: '3.1'

services:
    flowise:
        image: flowiseai/flowise
        restart: always
        environment:
            - PORT=${PORT}
            - DEBUG=${DEBUG}
            - DATABASE_PATH=${DATABASE_PATH}
            - SECRETKEY_PATH=${SECRETKEY_PATH}
            - FLOWISE_SECRETKEY_OVERWRITE=${FLOWISE_SECRETKEY_OVERWRITE}
            - LOG_PATH=${LOG_PATH}
            - LOG_LEVEL=${LOG_LEVEL}
            - EXECUTION_MODE=${EXECUTION_MODE}
        ports:
            - '${PORT}:${PORT}'
        volumes:
            - ~/.flowise:/root/.flowise
        networks:
            - flowise_net
        command: /bin/sh -c "sleep 3; flowise start"
networks:
    flowise_net:
        name: chroma_net
        external: true
```

4. Flowise Docker 이미지를 실행합니다.

```bash
docker compose up -d
```

5. Chroma URL에서 Windows 및 MacOS 운영 체제의 경우 [http://host.docker.internal:8000](http://host.docker.internal:8000/)을 지정합니다. Linux 기반 시스템의 경우 host.docker.internal을 사용할 수 없으므로 기본 Docker 게이트웨이를 사용해야 합니다: [http://172.17.0.1:8000](http://172.17.0.1:8000/)

<figure><img src="../../../.gitbook/assets/image (5) (5).png" alt="" width="256"><figcaption></figcaption></figure>

## 리소스

* [LangChain JS Chroma](https://js.langchain.com/docs/modules/indexes/vector_stores/integrations/chroma)
* [Chroma Getting Started](https://docs.trychroma.com/getting-started)
