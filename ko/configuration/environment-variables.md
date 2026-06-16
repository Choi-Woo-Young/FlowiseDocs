---
description: Flowise의 환경 변수 구성 방법 알아보기
---

# 환경 변수

Flowise는 인스턴스를 구성하기 위해 다양한 환경 변수를 지원합니다. `packages/server` 폴더 내의 `.env` 파일에서 다음 변수들을 지정할 수 있습니다. [.env.example](https://github.com/FlowiseAI/Flowise/blob/main/packages/server/.env.example) 파일을 참조하세요.

<table><thead><tr><th width="233">변수</th><th width="219">설명</th><th width="104">타입</th><th>기본값</th></tr></thead><tbody><tr><td>PORT</td><td>Flowise가 실행되는 HTTP 포트</td><td>Number</td><td>3000</td></tr><tr><td>FLOWISE_FILE_SIZE_LIMIT</td><td>업로드 시 최대 파일 크기</td><td>String</td><td><code>50mb</code></td></tr><tr><td>NUMBER_OF_PROXIES</td><td>레이트 리미트 프록시</td><td>Number</td><td></td></tr><tr><td>CORS_ORIGINS</td><td>모든 교차 출처 HTTP 호출에 대해 허용된 출처</td><td>String</td><td></td></tr><tr><td>IFRAME_ORIGINS</td><td>iframe src 임베딩에 대해 허용된 출처</td><td>String</td><td></td></tr><tr><td>SHOW_COMMUNITY_NODES</td><td>커뮤니티에서 생성한 노드 표시</td><td>Boolean: <code>true</code> 또는 <code>false</code></td><td></td></tr><tr><td>DISABLED_NODES</td><td>비활성화할 노드 이름의 쉼표로 구분된 목록</td><td>String</td><td></td></tr></tbody></table>

## 데이터베이스의 경우

| 변수           | 설명                                                      | 타입                                       | 기본값                  |
| ------------------ | ---------------------------------------------------------------- | ------------------------------------------ | ------------------------ |
| DATABASE_TYPE     | flowise 데이터를 저장할 데이터베이스 유형                       | Enum String: `sqlite`, `mysql`, `postgres` | `sqlite`                 |
| DATABASE_PATH     | 데이터베이스가 저장되는 위치 (DATABASE_TYPE이 sqlite일 때) | String                                     | `your-home-dir/.flowise` |
| DATABASE_HOST     | 호스트 URL 또는 IP 주소 (DATABASE_TYPE이 sqlite가 아닐 때)       | String                                     |                          |
| DATABASE_PORT     | 데이터베이스 포트 (DATABASE_TYPE이 sqlite가 아닐 때)                | String                                     |                          |
| DATABASE_USER     | 데이터베이스 사용자명 (DATABASE_TYPE이 sqlite가 아닐 때)            | String                                     |                          |
| DATABASE_PASSWORD | 데이터베이스 비밀번호 (DATABASE_TYPE이 sqlite가 아닐 때)            | String                                     |                          |
| DATABASE_NAME     | 데이터베이스 이름 (DATABASE_TYPE이 sqlite가 아닐 때)                | String                                     |                          |
| DATABASE_SSL      | 데이터베이스 SSL이 필요함 (DATABASE_TYPE이 sqlite가 아닐 때)     | Boolean: `true` 또는 `false`                 | `false`                  |

## 저장소의 경우

Flowise는 기본적으로 다음 파일들을 로컬 경로 폴더에 저장합니다.

* [문서 로더](../integrations/langchain/document-loaders/)/문서 저장소에 업로드된 파일
* 채팅에서 업로드된 이미지/오디오
* 어시스턴트의 이미지/파일
* [벡터 업서트 API](/broken/pages/F2AfRpI7qYixNiBWpmIe#vector-upsert-api)의 파일

사용자는 `STORAGE_TYPE`을 지정하여 AWS S3, Google Cloud Storage 또는 로컬 경로를 사용할 수 있습니다.

| 변수                               | 설명                                                                      | 타입                              | 기본값                          |
| -------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------- | -------------------------------- |
| STORAGE_TYPE                          | 업로드된 파일의 저장소 유형. 기본값은 `local`                           | Enum String: `s3`, `gcs`, `local` | `local`                          |
| BLOB_STORAGE_PATH                    | `STORAGE_TYPE`이 `local`일 때 업로드된 파일이 저장되는 로컬 폴더 경로 | String                            | `your-home-dir/.flowise/storage` |
| S3_STORAGE_BUCKET_NAME              | `STORAGE_TYPE`이 `s3`일 때 업로드된 파일을 보유할 버킷 이름               | String                            |                                  |
| S3_STORAGE_ACCESS_KEY_ID           | AWS 액세스 키                                                                   | String                            |                                  |
| S3_STORAGE_SECRET_ACCESS_KEY       | AWS 시크릿 키                                                                   | String                            |                                  |
| S3_STORAGE_REGION                    | S3 버킷의 지역                                                             | String                            |                                  |
| S3_ENDPOINT_URL                      | 커스텀 S3 엔드포인트 (선택사항)                                                    | String                            |                                  |
| S3_FORCE_PATH_STYLE                 | S3 경로 스타일 강제 (선택사항)                                                   | Boolean                           | false                            |
| GOOGLE_CLOUD_STORAGE_CREDENTIAL     | Google Cloud 서비스 계정 키                                                 | String                            |                                  |
| GOOGLE_CLOUD_STORAGE_PROJ_ID       | Google Cloud 프로젝트 ID                                                          | String                            |                                  |
| GOOGLE_CLOUD_STORAGE_BUCKET_NAME   | Google Cloud Storage 버킷 이름                                                 | String                            |                                  |
| GOOGLE_CLOUD_UNIFORM_BUCKET_ACCESS | 액세스 유형                                                                   | Boolean                           | true                             |

## 디버깅 및 로그의 경우

| 변수   | 설명                         | 타입                                             |                                |
| ---------- | ----------------------------------- | ------------------------------------------------ | ------------------------------ |
| DEBUG      | 컴포넌트에서 로그 출력          | Boolean                                          |                                |
| LOG_PATH  | 로그 파일이 저장되는 위치 | String                                           | `Flowise/packages/server/logs` |
| LOG_LEVEL | 다양한 로그 레벨            | Enum String: `error`, `info`, `verbose`, `debug` | `info`                         |

`DEBUG`: true로 설정하면 터미널/콘솔에 로그를 출력합니다:

<figure><img src="../.gitbook/assets/image (3) (3) (1).png" alt=""><figcaption></figcaption></figure>

`LOG_LEVEL`: 로거가 저장될 로그 레벨. `error`, `info`, `verbose` 또는 `debug`일 수 있습니다. 기본값은 `info`이며, `logger.info`만 로그 파일에 저장됩니다. 완전한 세부 정보를 원하면 `debug`로 설정하세요.

<figure><img src="../.gitbook/assets/image (2) (4).png" alt=""><figcaption><p><strong>server-requests.log.jsonl - Flowise로 전송되는 모든 요청을 기록합니다</strong></p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p><strong>server.log - Flowise의 일반 작업을 기록합니다</strong></p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (5) (4).png" alt=""><figcaption><p><strong>server-error.log - 스택 추적과 함께 오류를 기록합니다</strong></p></figcaption></figure>

### S3로 로그 스트리밍

`STORAGE_TYPE` 환경 변수가 `s3`로 설정되면 로그가 자동으로 스트리밍되고 S3에 저장됩니다. 새 로그 파일은 매시간 생성되어 더 쉬운 디버깅을 가능하게 합니다.

### GCS로 로그 스트리밍

`STORAGE_TYPE` 환경 변수가 `gcs`로 설정되면 로그가 자동으로 Google [Cloud Logging](https://cloud.google.com/logging?hl=en)으로 스트리밍됩니다.

## 자격증명의 경우

Flowise는 암호화 키를 사용하여 제3자 API 키를 암호화된 자격증명으로 저장합니다.

기본적으로 애플리케이션 시작 시 임의의 암호화 키가 생성되어 파일 경로에 저장됩니다. 이 암호화 키는 chatflow 내에서 사용되는 자격증명을 복호화하기 위해 매번 검색됩니다. 예를 들어 OpenAI API 키, Pinecone API 키 등입니다.

대신 AWS Secret Manager를 사용하여 암호화 키를 저장하도록 구성할 수 있습니다.

| 변수                      | 설명                                           | 타입                        | 기본값                   |
| ----------------------------- | ----------------------------------------------------- | --------------------------- | ------------------------- |
| SECRETKEY_STORAGE_TYPE      | 암호화 키를 저장하는 방법                       | Enum String: `local`, `aws` | `local`                   |
| SECRETKEY_PATH               | 암호화 키가 저장되는 로컬 파일 경로         | String                      | `Flowise/packages/server` |
| FLOWISE_SECRETKEY_OVERWRITE | 기존 키 대신 사용할 암호화 키 | String                      |                           |
| SECRETKEY_AWS_ACCESS_KEY   |                                                       | String                      |                           |
| SECRETKEY_AWS_SECRET_KEY   |                                                       | String                      |                           |
| SECRETKEY_AWS_REGION        |                                                       | String                      |                           |

어떤 이유로든 암호화 키가 다시 생성되거나 저장된 경로가 변경되면 - <mark style="color:red;">자격증명을 복호화할 수 없습니다</mark>와 같은 오류가 발생할 수 있습니다.

이를 피하려면 `FLOWISE_SECRETKEY_OVERWRITE`로 자신의 암호화 키를 설정할 수 있습니다. 그러면 같은 암호화 키가 매번 사용됩니다. 형식에는 제한이 없습니다. 원하는 텍스트로 설정할 수 있거나 `FLOWISE_PASSWORD`와 동일하게 설정할 수 있습니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
UI에서 반환되는 Credential API Key는 설정한 원본 Api Key와 같은 길이가 아닙니다. 이것은 네트워크 스푸핑을 방지하는 가짜 접두사 문자열입니다. 따라서 Api Key를 UI로 반환하지 않습니다. 그러나 올바른 Api Key는 chatflow와의 상호작용 중에 검색되고 사용됩니다.
{% endhint %}

## 모델의 경우

경우에 따라 기존 Chat Model 및 LLM 노드에서 커스텀 모델을 사용하거나 특정 모델에만 액세스를 제한할 수 있습니다.

기본적으로 Flowise는 [여기](https://github.com/FlowiseAI/Flowise/blob/main/packages/components/models.json)에서 모델 목록을 가져옵니다. 그러나 사용자는 자신의 `models.json` 파일을 만들고 파일 경로를 지정할 수 있습니다:

<table><thead><tr><th width="164">변수</th><th width="196">설명</th><th width="78">타입</th><th>기본값</th></tr></thead><tbody><tr><td>MODEL_LIST_CONFIG_JSON</td><td>`models.json` 구성 파일에서 모델 목록을 로드할 링크</td><td>String</td><td><a href="https://raw.githubusercontent.com/FlowiseAI/Flowise/main/packages/components/models.json">https://raw.githubusercontent.com/FlowiseAI/Flowise/main/packages/components/models.json</a></td></tr></tbody></table>

## 내장 및 외부 종속성의 경우

Flowise 내의 특정 노드/기능은 사용자가 Javascript 코드를 실행할 수 있도록 합니다. 보안상의 이유로 기본적으로는 특정 종속성만 허용합니다. 다음 환경 변수를 설정하여 내장 및 외부 모듈에 대한 제한을 해제할 수 있습니다:

<table><thead><tr><th>변수</th><th width="300.4444580078125">설명</th><th></th></tr></thead><tbody><tr><td>TOOL_FUNCTION_BUILTIN_DEP</td><td>사용할 NodeJS 내장 모듈</td><td>String</td></tr><tr><td>TOOL_FUNCTION_EXTERNAL_DEP</td><td>사용할 외부 모듈 </td><td>String</td></tr><tr><td>ALLOW_BUILTIN_DEP</td><td>`cheerio`, `typeorm` 같은 프로젝트 종속성을 사용할 수 있도록 허용</td><td>Boolean</td></tr></tbody></table>

{% code title=".env" %}
```bash
# 모든 내장 모듈의 사용을 허용합니다
TOOL_FUNCTION_BUILTIN_DEP=*

# fs만의 사용을 허용합니다
TOOL_FUNCTION_BUILTIN_DEP=fs

# crypto와 fs만의 사용을 허용합니다
TOOL_FUNCTION_BUILTIN_DEP=crypto,fs

# 외부 npm 모듈의 사용을 허용합니다.
TOOL_FUNCTION_EXTERNAL_DEP=cheerio,typeorm

ALLOW_BUILTIN_DEP=true
```
{% endcode %}

### 내장 종속성 사용

{% hint style="warning" %}
Puppeteer와 같은 일부 내장 종속성은 잠재적인 보안 취약점을 유발할 수 있습니다. 사용하기 전에 이러한 위험을 신중하게 분석하고 평가하는 것이 좋습니다.
{% endhint %}

### NodeVM 실행 오류: VMError: 모듈을 찾을 수 없음

기본적으로 허용되지 않는 라이브러리를 사용하는 경우 다음 중 하나를 수행할 수 있습니다:

1. 모든 프로젝트 [라이브러리/종속성](https://github.com/FlowiseAI/Flowise/blob/main/packages/components/src/utils.ts#L52) 허용: `ALLOW_BUILTIN_DEP=true`
2. (권장) 특정 라이브러리/종속성만 허용: `TOOL_FUNCTION_EXTERNAL_DEP=cheerio,typeorm`

## 보안 구성

<table><thead><tr><th width="246.4444580078125">변수</th><th width="180.4444580078125">설명</th><th width="192.666748046875">옵션</th><th>기본값</th></tr></thead><tbody><tr><td><code>HTTP_DENY_LIST</code></td><td>MCP 서버에서 지정된 URL 또는 도메인으로의 HTTP 요청을 차단합니다</td><td>쉼표로 구분된 URL/도메인</td><td><em>(empty)</em></td></tr><tr><td><code>CUSTOM_MCP_SECURITY_CHECK</code></td><td>Custom MCP 구성에 대한 포괄적인 보안 검증을 활성화합니다</td><td><code>true</code> | <code>false</code></td><td><code>true</code></td></tr><tr><td><code>CUSTOM_MCP_PROTOCOL</code></td><td>Custom MCP 통신을 위한 기본 프로토콜을 설정합니다</td><td><code>stdio</code> | <code>sse</code></td><td><code>stdio</code></td></tr></tbody></table>

#### `CUSTOM_MCP_SECURITY_CHECK=true`

기본적으로 활성화되어 있습니다. 활성화되면 다음 보안 검증을 적용합니다:

* **명령 허용 목록**: 안전한 명령만 허용합니다 (`node`, `npx`, `python`, `python3`, `docker`)
* **인수 검증**: 위험한 파일 경로, 디렉토리 트래버설 및 실행 파일을 차단합니다
* **주입 방지**: 셸 메타문자 및 명령 체이닝을 방지합니다
* **환경 보호**: 중요한 환경 변수 (PATH, LD_LIBRARY_PATH) 수정을 차단합니다

#### `CUSTOM_MCP_PROTOCOL`

* **`stdio`**: 직접 프로세스 통신 (기본값, 명령 실행 필요)
* **`sse`**: HTTP를 통한 Server-Sent Events (프로덕션 권장, 더 안전함)

### 권장되는 프로덕션 설정

```bash
# 보안 검증 활성화 (기본값)
CUSTOM_MCP_SECURITY_CHECK=true

# 보안성을 위해 SSE 프로토콜 사용
CUSTOM_MCP_PROTOCOL=sse

# 위험한 도메인 차단 (예시)
HTTP_DENY_LIST=localhost,127.0.0.1,internal.company.com

# 기본적으로 위험한 도메인 목록을 차단하지만 false로 설정하여 비활성화할 수 있습니다
HTTP_SECURITY_CHECK=true

# 경로 트래버설 공격을 방지하기 위해 제공된 파일 및 폴더 경로에 대한 검사를 활성화합니다
PATH_TRAVERSAL_SAFETY=true
```

{% hint style="warning" %}
**경고**: `CUSTOM_MCP_SECURITY_CHECK`를 비활성화하면 임의의 명령 실행을 허용하며 프로덕션 환경에서 심각한 보안 위험을 초래합니다.

`HTTP_SECURITY_CHECK`는 위험한 도메인의 하드코딩된 목록을 차단하는 기본 제공 보안 기능을 활성화합니다. 기본적으로 `true`이며 `false`로 설정하여 비활성화할 수 있습니다.

`HTTP_DENY_LIST`를 사용하면 차단할 도메인의 추가 커스텀 목록을 지정할 수 있습니다. 이 목록은 기본적으로 비어 있습니다.

`PATH_TRAVERSAL_SAFETY`는 파일 및 폴더 경로에 대한 경로 트래버설 공격을 방지하기 위한 기본 제공 보안 기능을 활성화합니다. 기본적으로 `true`이며 `false`로 설정하여 비활성화할 수 있습니다.
{% endhint %}

## 환경 변수를 설정하는 방법의 예

### NPM

npx를 사용하여 Flowise를 실행할 때 이러한 모든 변수를 설정할 수 있습니다. 예를 들어:

```
npx flowise start --PORT=3000 --DEBUG=true
```

### Docker

```
docker run -d -p 5678:5678 flowise \
 -e DATABASE_TYPE=postgresdb \
 -e DATABASE_PORT=<POSTGRES_PORT> \
 -e DATABASE_HOST=<POSTGRES_HOST> \
 -e DATABASE_NAME=<POSTGRES_DATABASE_NAME> \
 -e DATABASE_USER=<POSTGRES_USER> \
 -e DATABASE_PASSWORD=<POSTGRES_PASSWORD> \
```

### Docker Compose

`.env` 파일에서 이러한 모든 변수를 `docker` 폴더 내에 설정할 수 있습니다. [.env.example](https://github.com/FlowiseAI/Flowise/blob/main/docker/.env.example) 파일을 참조하세요.
