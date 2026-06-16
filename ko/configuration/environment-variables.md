---
description: Flowise의 환경 변수를 구성하는 방법을 알아봅니다
---

# 환경 변수

Flowise는 인스턴스를 구성하기 위한 다양한 환경 변수를 지원합니다. `packages/server` 폴더 안의 `.env` 파일에서 다음 변수들을 지정할 수 있습니다. [.env.example](https://github.com/FlowiseAI/Flowise/blob/main/packages/server/.env.example) 파일을 참고하세요.

<table><thead><tr><th width="233">Variable</th><th width="219">Description</th><th width="104">Type</th><th>Default</th></tr></thead><tbody><tr><td>PORT</td><td>Flowise가 실행되는 HTTP 포트</td><td>Number</td><td>3000</td></tr><tr><td>FLOWISE_FILE_SIZE_LIMIT</td><td>업로드 시 최대 파일 크기</td><td>String</td><td><code>50mb</code></td></tr><tr><td>NUMBER_OF_PROXIES</td><td>Rate Limit 프록시</td><td>Number</td><td></td></tr><tr><td>CORS_ORIGINS</td><td>모든 교차 출처(cross-origin) HTTP 호출에 허용되는 출처</td><td>String</td><td></td></tr><tr><td>IFRAME_ORIGINS</td><td>iframe src 임베딩에 허용되는 출처</td><td>String</td><td></td></tr><tr><td>SHOW_COMMUNITY_NODES</td><td>커뮤니티가 생성한 Node를 표시</td><td>Boolean: <code>true</code> or <code>false</code></td><td></td></tr><tr><td>DISABLED_NODES</td><td>비활성화할 Node 이름의 쉼표로 구분된 목록</td><td>String</td><td></td></tr></tbody></table>

## 데이터베이스

| Variable           | Description                                                      | Type                                       | Default                  |
| ------------------ | ---------------------------------------------------------------- | ------------------------------------------ | ------------------------ |
| DATABASE\_TYPE     | Flowise 데이터를 저장할 데이터베이스 유형                       | Enum String: `sqlite`, `mysql`, `postgres` | `sqlite`                 |
| DATABASE\_PATH     | 데이터베이스가 저장되는 위치 (DATABASE\_TYPE이 sqlite일 때) | String                                     | `your-home-dir/.flowise` |
| DATABASE\_HOST     | 호스트 URL 또는 IP 주소 (DATABASE\_TYPE이 sqlite가 아닐 때)       | String                                     |                          |
| DATABASE\_PORT     | 데이터베이스 포트 (DATABASE\_TYPE이 sqlite가 아닐 때)                | String                                     |                          |
| DATABASE\_USER     | 데이터베이스 사용자명 (DATABASE\_TYPE이 sqlite가 아닐 때)            | String                                     |                          |
| DATABASE\_PASSWORD | 데이터베이스 비밀번호 (DATABASE\_TYPE이 sqlite가 아닐 때)            | String                                     |                          |
| DATABASE\_NAME     | 데이터베이스 이름 (DATABASE\_TYPE이 sqlite가 아닐 때)                | String                                     |                          |
| DATABASE\_SSL      | 데이터베이스 SSL 필요 여부 (DATABASE\_TYPE이 sqlite가 아닐 때)     | Boolean: `true` or `false`                 | `false`                  |

## 스토리지

Flowise는 기본적으로 다음 파일들을 로컬 경로 폴더 아래에 저장합니다.

* [Document Loaders](../integrations/langchain/document-loaders/)/Document Store에서 업로드된 파일
* 채팅에서 업로드된 이미지/오디오
* Assistant의 이미지/파일
* [Vector Upsert API](/broken/pages/F2AfRpI7qYixNiBWpmIe#vector-upsert-api)의 파일

사용자는 `STORAGE_TYPE`을 지정하여 AWS S3, Google Cloud Storage 또는 로컬 경로를 사용할 수 있습니다.

| Variable                               | Description                                                                      | Type                              | Default                          |
| -------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------- | -------------------------------- |
| STORAGE\_TYPE                          | 업로드된 파일의 스토리지 유형. 기본값은 `local`                           | Enum String: `s3`, `gcs`, `local` | `local`                          |
| BLOB\_STORAGE\_PATH                    | `STORAGE_TYPE`이 `local`일 때 업로드된 파일이 저장되는 로컬 폴더 경로 | String                            | `your-home-dir/.flowise/storage` |
| S3\_STORAGE\_BUCKET\_NAME              | `STORAGE_TYPE`이 `s3`일 때 업로드된 파일을 보관할 버킷 이름               | String                            |                                  |
| S3\_STORAGE\_ACCESS\_KEY\_ID           | AWS Access Key                                                                   | String                            |                                  |
| S3\_STORAGE\_SECRET\_ACCESS\_KEY       | AWS Secret Key                                                                   | String                            |                                  |
| S3\_STORAGE\_REGION                    | S3 버킷의 리전                                                             | String                            |                                  |
| S3\_ENDPOINT\_URL                      | 사용자 지정 S3 엔드포인트 (선택 사항)                                                    | String                            |                                  |
| S3\_FORCE\_PATH\_STYLE                 | S3 경로 스타일 강제 적용 (선택 사항)                                                   | Boolean                           | false                            |
| GOOGLE\_CLOUD\_STORAGE\_CREDENTIAL     | Google Cloud 서비스 계정 키                                                 | String                            |                                  |
| GOOGLE\_CLOUD\_STORAGE\_PROJ\_ID       | Google Cloud 프로젝트 ID                                                          | String                            |                                  |
| GOOGLE\_CLOUD\_STORAGE\_BUCKET\_NAME   | Google Cloud Storage 버킷 이름                                                 | String                            |                                  |
| GOOGLE\_CLOUD\_UNIFORM\_BUCKET\_ACCESS | 액세스 유형                                                                   | Boolean                           | true                             |

## 디버깅 및 로그

| Variable   | Description                         | Type                                             |                                |
| ---------- | ----------------------------------- | ------------------------------------------------ | ------------------------------ |
| DEBUG      | 컴포넌트의 로그를 출력          | Boolean                                          |                                |
| LOG\_PATH  | 로그 파일이 저장되는 위치 | String                                           | `Flowise/packages/server/logs` |
| LOG\_LEVEL | 다양한 로그 레벨            | Enum String: `error`, `info`, `verbose`, `debug` | `info`                         |

`DEBUG`: true로 설정하면 로그를 터미널/콘솔에 출력합니다.

<figure><img src="../.gitbook/assets/image (3) (3) (1).png" alt=""><figcaption></figcaption></figure>

`LOG_LEVEL`: 저장할 로거의 다양한 로그 레벨입니다. `error`, `info`, `verbose` 또는 `debug`로 설정할 수 있습니다. 기본값은 `info`이며, `logger.info`만 로그 파일에 저장됩니다. 전체 세부 정보를 보려면 `debug`로 설정하세요.

<figure><img src="../.gitbook/assets/image (2) (4).png" alt=""><figcaption><p><strong>server-requests.log.jsonl - Flowise로 전송된 모든 요청을 기록합니다</strong></p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p><strong>server.log - Flowise의 일반적인 작업을 기록합니다</strong></p></figcaption></figure>

<figure><img src="../.gitbook/assets/image (5) (4).png" alt=""><figcaption><p><strong>server-error.log - 스택 트레이스와 함께 오류를 기록합니다</strong></p></figcaption></figure>

### S3 로그 스트리밍

`STORAGE_TYPE` 환경 변수가 `s3`로 설정되면 로그가 자동으로 S3에 스트리밍되어 저장됩니다. 새 로그 파일은 매시간 생성되어 더 쉬운 디버깅이 가능합니다.

### GCS 로그 스트리밍

`STORAGE_TYPE` 환경 변수가 `gcs`로 설정되면 로그가 자동으로 Google [Cloud Logging](https://cloud.google.com/logging?hl=en)으로 스트리밍됩니다.

## 자격 증명(Credentials)

Flowise는 암호화 키를 사용하여 서드파티 API 키를 암호화된 자격 증명으로 저장합니다.

기본적으로 애플리케이션을 시작할 때 임의의 암호화 키가 생성되어 파일 경로 아래에 저장됩니다. 이 암호화 키는 chatflow 내에서 사용되는 자격 증명을 복호화하기 위해 매번 검색됩니다. 예를 들어 OpenAI API 키, Pinecone API 키 등이 있습니다.

대신 AWS Secret Manager를 사용하여 암호화 키를 저장하도록 구성할 수 있습니다.

| Variable                      | Description                                           | Type                        | Default                   |
| ----------------------------- | ----------------------------------------------------- | --------------------------- | ------------------------- |
| SECRETKEY\_STORAGE\_TYPE      | 암호화 키를 저장하는 방식                       | Enum String: `local`, `aws` | `local`                   |
| SECRETKEY\_PATH               | 암호화 키가 저장되는 로컬 파일 경로         | String                      | `Flowise/packages/server` |
| FLOWISE\_SECRETKEY\_OVERWRITE | 기존 키 대신 사용할 암호화 키 | String                      |                           |
| SECRETKEY\_AWS\_ACCESS\_KEY   |                                                       | String                      |                           |
| SECRETKEY\_AWS\_SECRET\_KEY   |                                                       | String                      |                           |
| SECRETKEY\_AWS\_REGION        |                                                       | String                      |                           |

어떤 이유로 인해 때때로 암호화 키가 재생성되거나 저장된 경로가 변경되어 - <mark style="color:red;">Credentials could not be decrypted.</mark> 와 같은 오류가 발생할 수 있습니다.

이를 방지하려면 `FLOWISE_SECRETKEY_OVERWRITE`로 자체 암호화 키를 설정하여 매번 동일한 암호화 키가 사용되도록 할 수 있습니다. 형식에는 제한이 없으며, 원하는 임의의 텍스트로 설정하거나 `FLOWISE_PASSWORD`와 동일하게 설정할 수 있습니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
UI에서 반환되는 자격 증명 API 키는 설정한 원래 API 키와 길이가 다릅니다. 이는 네트워크 스푸핑을 방지하는 가짜 접두사 문자열이며, 그렇기 때문에 API 키를 UI로 다시 반환하지 않습니다. 하지만 chatflow와 상호작용하는 동안에는 올바른 API 키가 검색되어 사용됩니다.
{% endhint %}

## 모델(Models)

경우에 따라 기존 Chat Model 및 LLM Node에서 사용자 지정 모델을 사용하거나 특정 모델로만 접근을 제한하고 싶을 수 있습니다.

기본적으로 Flowise는 [여기](https://github.com/FlowiseAI/Flowise/blob/main/packages/components/models.json)에서 모델 목록을 가져옵니다. 하지만 사용자는 자신만의 `models.json` 파일을 생성하고 해당 파일 경로를 지정할 수 있습니다.

<table><thead><tr><th width="164">Variable</th><th width="196">Description</th><th width="78">Type</th><th>Default</th></tr></thead><tbody><tr><td>MODEL_LIST_CONFIG_JSON</td><td><code>models.json</code> 설정 파일에서 모델 목록을 로드할 링크</td><td>String</td><td><a href="https://raw.githubusercontent.com/FlowiseAI/Flowise/main/packages/components/models.json">https://raw.githubusercontent.com/FlowiseAI/Flowise/main/packages/components/models.json</a></td></tr></tbody></table>

## 내장 및 외부 의존성

Flowise 내에는 사용자가 Javascript 코드를 실행할 수 있는 특정 Node/기능이 있습니다. 보안상의 이유로 기본적으로는 특정 의존성만 허용됩니다. 다음 환경 변수를 설정하여 내장 및 외부 모듈에 대한 제한을 해제할 수 있습니다.

<table><thead><tr><th>Variable</th><th width="300.4444580078125">Description</th><th></th></tr></thead><tbody><tr><td>TOOL_FUNCTION_BUILTIN_DEP</td><td>사용할 NodeJS 내장 모듈</td><td>String</td></tr><tr><td>TOOL_FUNCTION_EXTERNAL_DEP</td><td>사용할 외부 모듈 </td><td>String</td></tr><tr><td>ALLOW_BUILTIN_DEP</td><td><code>cheerio</code>, <code>typeorm</code>과 같은 프로젝트 의존성 사용 허용</td><td>Boolean</td></tr></tbody></table>

{% code title=".env" %}
```bash
# Allows usage of all builtin modules
TOOL_FUNCTION_BUILTIN_DEP=*

# Allows usage of only fs
TOOL_FUNCTION_BUILTIN_DEP=fs

# Allows usage of only crypto and fs
TOOL_FUNCTION_BUILTIN_DEP=crypto,fs

# Allow usage of external npm modules.
TOOL_FUNCTION_EXTERNAL_DEP=cheerio,typeorm

ALLOW_BUILTIN_DEP=true
```
{% endcode %}

### 내장 의존성 사용

{% hint style="warning" %}
Puppeteer와 같은 일부 내장 의존성은 잠재적인 보안 취약점을 야기할 수 있습니다. 사용하기 전에 이러한 위험을 신중하게 분석하고 평가하는 것이 좋습니다.
{% endhint %}

### NodeVM 실행 오류: VMError: Cannot find module

기본적으로 허용되지 않는 라이브러리를 사용하는 경우 다음 중 하나를 수행할 수 있습니다.

1. 모든 프로젝트의 [라이브러리/의존성](https://github.com/FlowiseAI/Flowise/blob/main/packages/components/src/utils.ts#L52)을 허용: `ALLOW_BUILTIN_DEP=true`
2. (권장) 특정 라이브러리/의존성을 명시적으로 허용: `TOOL_FUNCTION_EXTERNAL_DEP=cheerio,typeorm`

## 보안 설정

<table><thead><tr><th width="246.4444580078125">Variable</th><th width="180.4444580078125">Description</th><th width="192.666748046875">Options</th><th>Default</th></tr></thead><tbody><tr><td><code>HTTP_DENY_LIST</code></td><td>MCP 서버에서 지정된 URL 또는 도메인으로의 HTTP 요청을 차단</td><td>쉼표로 구분된 URL/도메인</td><td><em>(비어 있음)</em></td></tr><tr><td><code>CUSTOM_MCP_SECURITY_CHECK</code></td><td>Custom MCP 구성에 대한 포괄적인 보안 검증을 활성화</td><td><code>true</code> | <code>false</code></td><td><code>true</code></td></tr><tr><td><code>CUSTOM_MCP_PROTOCOL</code></td><td>Custom MCP 통신의 기본 프로토콜을 설정</td><td><code>stdio</code> | <code>sse</code></td><td><code>stdio</code></td></tr></tbody></table>

#### `CUSTOM_MCP_SECURITY_CHECK=true`

기본적으로 활성화되어 있습니다. 활성화되면 다음과 같은 보안 검증을 적용합니다.

* **명령 허용 목록(Command Allowlist)**: 안전한 명령(`node`, `npx`, `python`, `python3`, `docker`)만 허용합니다
* **인수 검증(Argument Validation)**: 위험한 파일 경로, 디렉터리 탐색(directory traversal) 및 실행 파일을 차단합니다
* **인젝션 방지(Injection Prevention)**: 셸 메타문자 및 명령 체이닝을 방지합니다
* **환경 보호(Environment Protection)**: 중요한 환경 변수(PATH, LD\_LIBRARY\_PATH)의 수정을 차단합니다

#### `CUSTOM_MCP_PROTOCOL`

* **`stdio`**: 직접 프로세스 통신 (기본값, 명령 실행 필요)
* **`sse`**: HTTP를 통한 Server-Sent Events (프로덕션에 권장, 더 안전함)

### 권장 프로덕션 설정

```bash
# Enable security validation (default)
CUSTOM_MCP_SECURITY_CHECK=true

# Use SSE protocol for better security
CUSTOM_MCP_PROTOCOL=sse

# Block dangerous domains (example)
HTTP_DENY_LIST=localhost,127.0.0.1,internal.company.com

# Blocks a hardcoded list of dangerous domains by default, but can be set to false to disable
HTTP_SECURITY_CHECK=true

# Enables checks on provided file and folder paths to prevent path traversal attacks
PATH_TRAVERSAL_SAFETY=true
```

{% hint style="warning" %}
**경고**: `CUSTOM_MCP_SECURITY_CHECK`를 비활성화하면 임의의 명령 실행이 허용되어 프로덕션 환경에서 심각한 보안 위험을 초래합니다.

`HTTP_SECURITY_CHECK`는 하드코딩된 위험 도메인 목록을 차단하는 내장 보안 기능을 활성화합니다. 기본값은 `true`이며 `false`로 설정하여 비활성화할 수 있습니다.

`HTTP_DENY_LIST`를 사용하면 차단할 추가적인 사용자 지정 도메인 목록을 지정할 수 있습니다. 이 목록은 기본적으로 비어 있습니다.

`PATH_TRAVERSAL_SAFETY`는 파일 및 폴더 경로에 대한 경로 탐색(path traversal) 공격을 방지하는 내장 보안 기능을 활성화합니다. 기본값은 `true`이며 `false`로 설정하여 비활성화할 수 있습니다.
{% endhint %}

## 환경 변수를 설정하는 방법의 예시

### NPM

npx를 사용하여 Flowise를 실행할 때 이 모든 변수를 설정할 수 있습니다. 예를 들면 다음과 같습니다.

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

`docker` 폴더 안의 `.env` 파일에서 이 모든 변수를 설정할 수 있습니다. [.env.example](https://github.com/FlowiseAI/Flowise/blob/main/docker/.env.example) 파일을 참고하세요.
