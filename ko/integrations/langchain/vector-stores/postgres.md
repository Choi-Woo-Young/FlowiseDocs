---
description: >-
  pgvector를 사용하여 Postgres에 embedding된 데이터를 upsert하고 query 시 유사도 검색을 수행합니다.
---
# Postgres

<figure><img src="../../../.gitbook/assets/image (163).png" alt="" width="292"><figcaption><p>Postgres Node</p></figcaption></figure>

인스턴스 설정 방식에 따라 Postgres에 연결하는 여러 가지 방법이 있습니다. 아래는 pgvector 팀이 제공하는 사전 빌드된 Docker 이미지를 사용한 로컬 구성 예시입니다.

아래 내용으로 `docker-compose.yml`이라는 이름의 파일을 생성하세요:```yaml
# Run this command to start the database:
# docker-compose up --build
version: "3"
services:
  db:
    hostname: 127.0.0.1
    image: pgvector/pgvector:pg16
    ports:
      - 5432:5432
    restart: always
    environment:
      - POSTGRES_DB=api
      - POSTGRES_USER=myuser
      - POSTGRES_PASSWORD=ChangeMe
    volumes:
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
````docker compose up`을 실행하여 Postgres 컨테이너를 시작합니다.

구성된 사용자 및 비밀번호로 새 credential을 생성합니다:

<figure><img src="../../../.gitbook/assets/image (50).png" alt="" width="526"><figcaption></figcaption></figure>

`docker-compose.yml`에 구성된 값으로 node의 필드를 채웁니다. 예를 들어:

* Host: **localhost**
* Database: **api**
* Port: **5432**

짜잔! 이제 Postgres Vector를 사용할 준비가 성공적으로 완료되었습니다.

### 문제 해결

Flowise와 Postgres가 모두 Docker에서 실행 중인 경우, 다음 오류가 표시될 수 있습니다: <mark style="color:red;">**AggregateError**</mark>.

Host 값을 `localhost`에서 `host.docker.internal`로 변경해 보세요.

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>