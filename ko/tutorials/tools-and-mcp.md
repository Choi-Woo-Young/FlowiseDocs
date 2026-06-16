# 도구 및 MCP

이전 [**API와 상호 작용**](interacting-with-api.md) 튜토리얼에서 LLM이 외부 API를 호출하는 방법을 살펴봤습니다. 사용자 경험을 강화하기 위해 Flowise는 미리 만들어진 도구 목록을 제공합니다. 사용 가능한 통합의 전체 목록은 [**도구**](../integrations/langchain/tools/) 섹션을 참조하세요.

필요한 도구가 아직 사용 가능하지 않은 경우 요구사항을 충족하도록 **사용자 정의 도구**를 만들 수 있습니다.

## 사용자 정의 도구

동일한 [이벤트 관리 서버](interacting-with-api.md#prerequisite)를 사용하고 `/events` POST 요청을 호출할 수 있는 사용자 정의 도구를 만듭니다.

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

* **도구명:** `create_event`
* **도구 설명:** `새 이벤트를 만들고 싶을 때 사용합니다.`
* **입력 스키마:** LLM이 올바른 JSON 본문을 자동으로 생성하는 방법을 알 수 있도록 해주는 API 요청 본문의 JSON 스키마입니다. 예를 들어:
* **JavaScript 함수**: 이 도구가 호출되면 실행할 실제 함수입니다.

```javascript
const fetch = require('node-fetch');
const url = 'http://localhost:5566/events';
const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name: $name,
      location: $location,
      date: $date
    })
};
try {
    const response = await fetch(url, options);
    const text = await response.text();
    return text;
} catch (error) {
    console.error(error);
    return '';
}
```

### 함수 사용 방법:

* Flowise에서 가져온 모든 라이브러리를 사용할 수 있습니다.
* 입력 스키마에 지정된 속성을 `$` 접두사가 있는 변수로 사용할 수 있습니다:
  * 입력 스키마의 속성 = `name`
  * 함수에서 사용할 변수 = `$name`
* 기본 플로우 구성을 가져올 수 있습니다:
  * `$flow.sessionId`
  * `$flow.chatId`
  * `$flow.chatflowId`
  * `$flow.input`
  * `$flow.state`
* 사용자 정의 변수 가져오기: `$vars.<variable-name>`
* 함수 끝에 문자열 값을 반환해야 합니다.

### 에이전트에서 사용자 정의 도구 사용

사용자 정의 도구가 생성되면 에이전트 노드에서 사용할 수 있습니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="341"><figcaption></figcaption></figure>

도구 드롭다운에서 사용자 정의 도구를 선택합니다. 사용자 정의 도구의 출력을 직접 반환하려면 **직접 반환**을 켜켤 수도 있습니다.

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="392"><figcaption></figcaption></figure>

### 도구 노드에서 사용자 정의 도구 사용

결정된 워크플로우 시나리오에서 도구 노드로도 사용할 수 있습니다.
이 경우 **도구 입력 인수를 명시적으로 정의하고 값으로 채워야 합니다.** LLM이 값을 자동으로 결정하지 않기 때문입니다.

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## MCP

MCP ([모델 컨텍스트 프로토콜](https://modelcontextprotocol.io/introduction))은 AI 모델을 다양한 데이터 소스 및 도구에 연결하는 표준화된 방법을 제공합니다. 즉, Flowise 내장 도구나 사용자 정의 도구에 의존하는 대신 다른 사람이 만든 MCP 서버를 사용할 수 있습니다. MCP는 널리 업계 표준으로 간주되며 일반적으로 공식 제공자가 지원하고 유지보수합니다. 예를 들어, GitHub MCP는 GitHub 팀에서 개발하고 유지보수하며, 유사한 지원이 Atlassian Jira, Brave Search 등에도 제공됩니다. 지원되는 서버 목록은 [여기](https://modelcontextprotocol.io/examples)에서 찾을 수 있습니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="413"><figcaption></figcaption></figure>

## 사용자 정의 MCP

미리 만들어진 MCP 도구 외에도 가장 강력한 기능은 사용자가 자신의 선택에 따라 모든 MCP 서버에 연결할 수 있는 **사용자 정의 MCP**입니다.

MCP는 클라이언트-서버 아키텍처를 따르며 여기서:

* **호스트**는 LLM 애플리케이션(Flowise 같은)이 연결을 시작합니다.
* **클라이언트**는 호스트 애플리케이션 내(사용자 정의 MCP와 같은) 서버와의 1:1 연결을 유지합니다.
* **서버**는 클라이언트(예: [서버](https://modelcontextprotocol.io/examples))에 컨텍스트, 도구 및 프롬프트를 제공합니다.

클라이언트와 서버 간의 실제 통신을 처리하기 위해 MCP는 여러 전송 메커니즘을 지원합니다:

1. **Stdio 전송**
   * 표준 입출력 스트림을 통한 통신
   * 로컬 프로세스에 이상적
2. **스트리밍 가능 HTTP 전송**
   * 선택적 Server-Sent Events를 사용한 HTTP
   * 클라이언트-서버 메시지의 경우 HTTP POST

### Stdio

Stdio 전송은 표준 입력 및 출력 스트림을 통한 통신을 활성화합니다. 이는 로컬 통합 및 명령줄 도구에 특히 유용합니다.

Flowise가 클라우드 서비스에 배포된 경우가 아니라 로컬에서만 사용하세요. 이는 `npx` 같은 명령을 실행하면 MCP 서버 패키지(예: `@modelcontextprotocol/server-sequential-thinking`)가 로컬에 설치되며 오래 걸릴 수 있기 때문입니다.

데스크톱 애플리케이션(Claude Desktop, VS Code 등)에 더 적합합니다.

#### **NPX 명령**

```json
{
  "command": "npx",
  "args": [
    "-y",
    "@modelcontextprotocol/server-sequential-thinking"
  ]
}
```

<figure><img src="../.gitbook/assets/image (16) (1) (1).png" alt="" width="419"><figcaption></figcaption></figure>

Windows의 경우 [이 가이드](https://gist.github.com/feveromo/7a340d7795fca1ccd535a5802b976e1f)를 참조하세요.

#### **Docker 명령**

Docker 명령은 Flowise를 실행 중인 시스템이 Docker에 접근할 수 있을 때 적합합니다. 그러나 Docker 접근이 제한되거나 사용 불가능한 클라우드 서비스 배포에는 적합하지 않습니다.

```json
{
  "command": "docker",
  "args": [
    "run",
    "-i",
    "--rm",
    "mcp/sequentialthinking"
  ]
}
```

<figure><img src="../.gitbook/assets/image (312).png" alt="" width="416"><figcaption></figcaption></figure>

Docker는 MCP 서버 목록을 제공합니다. [여기](https://hub.docker.com/catalogs/mcp)에서 찾을 수 있습니다. 작동 방식은 다음과 같습니다:

1. Docker가 실행 중인지 확인합니다.
2. MCP 서버 구성을 찾아 **사용자 정의 MCP**에 추가합니다. 예: [https://hub.docker.com/r/mcp/sequentialthinking](https://hub.docker.com/r/mcp/sequentialthinking)
3. **사용 가능한 작업**을 새로 고칩니다. 이미지를 로컬에서 찾을 수 없으면 Docker가 자동으로 최신 이미지를 가져옵니다. 이미지를 가져온 후 사용 가능한 작업 목록이 표시됩니다.

```
로컬에서 'mcp/sequentialthinking:latest' 이미지를 찾을 수 없습니다.
latest: mcp/sequentialthinking에서 가져오는 중
f18232174bc9: 이미 존재
cb2bde55f71f: Pull complete
9d0e0719fbe0: Pull complete
6f063dbd7a5d: Pull complete
93a0fbe48c24: Pull complete
e2e59f8d7891: Pull complete
96ec0bda7033: Pull complete
4f4fb700ef54: Pull complete
d0900e07408c: Pull complete
Digest: sha256:cd3174b2ecf37738654cf7671fb1b719a225c40a78274817da00c4241f465e5f
Status: mcp/sequentialthinking:latest를 위해 새 이미지 다운로드됨
Sequential Thinking MCP Server running on stdio
```

#### 사용 시기

* 명령줄 도구 구축
* 로컬 통합 구현
* 간단한 프로세스 통신 필요
* 셸 스크립트와 함께 작동

### 스트리밍 가능 HTTP (권장)

GitHub Remote MCP를 예로 사용합니다. [원격 GitHub MCP 서버](https://github.com/github/github-mcp-server)의 장점은 로컬에 설치하거나 실행할 필요가 없다는 것입니다. 새 업데이트가 자동으로 적용됩니다.

#### 단계 1: Github PAT를 위한 변수 만들기

MCP 서버에 접근하려면 Github에서 Personal Access Token을 만들어야 합니다. [가이드](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)를 참조하세요. PAT를 만든 후 토큰을 저장할 변수를 만듭니다. 이 변수는 사용자 정의 MCP에서 사용됩니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="508"><figcaption></figcaption></figure>

#### 단계 2: 사용자 정의 MCP 만들기

에이전트 노드를 만들고 새 사용자 정의 MCP 도구를 추가합니다. 스트리밍 가능 HTTP의 경우 URL과 다른 필요한 헤더만 추가하면 됩니다. [변수](../using-flowise/variables.md)를 `{{ }}` 이중 중괄호와 `$vars.<variableName>` 접두사를 사용하여 MCP 서버 구성에서 사용할 수 있습니다.

```json
{
  "url": "https://api.githubcopilot.com/mcp/",
  "headers": {
    "Authorization": "Bearer {{$vars.githubPAT}}",
  }
}
```

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="414"><figcaption></figcaption></figure>

#### 단계 3: 작업 선택

MCP 서버 구성이 올바르게 작동하면 **사용 가능한 작업**을 새로 고치면 Flowise가 MCP 서버에서 사용 가능한 모든 작업을 자동으로 가져옵니다.

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1).png" alt="" width="359"><figcaption></figcaption></figure>

#### 예제 상호 작용:

> 가장 최근 이슈를 주세요.

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

에이전트는 MCP에서 적절한 작업을 식별하고 사용자의 쿼리에 답하는 데 사용할 수 있습니다.

#### 사용 시기

스트리밍 가능 HTTP를 사용하는 경우:

* 웹 기반 통합 구축
* HTTP를 통한 클라이언트-서버 통신 필요
* 상태 있는 세션 필요
* 여러 동시 클라이언트 지원
* 재개 가능한 연결 구현

## 비디오 튜토리얼

{% embed url="https://youtu.be/7FClI-QM3tk?si=zBNEShd3NlcrOBrO" %}
