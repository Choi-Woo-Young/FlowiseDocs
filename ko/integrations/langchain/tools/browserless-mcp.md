---
description: MCP Server for Browserless - 페이지 스크래핑, 스크린샷 촬영, PDF 생성 등
---

# Browserless MCP

**Browserless MCP** 노드는 Model Context Protocol (MCP)을 통해 Flowise 에이전트를 [Browserless](https://browserless.io)에 연결합니다. 웹 스크래핑, 스크린샷 촬영, PDF 생성 등의 브라우저 자동화 기능을 제공하며, 헤드리스 브라우저 인프라를 직접 관리할 필요가 없습니다.

---

## 1. 사전 요구사항

Browserless MCP 노드를 사용하기 전에 다음이 필요합니다:

- **Browserless 계정**: [browserless.io](https://browserless.io)에서 무료로 가입하세요.
- **API Token**: Browserless 대시보드에서 토큰을 발급받으세요.

---

## 2. 자격 증명 설정

1. Flowise에서 사이드바의 **Credentials**로 이동하세요.
2. **Add Credential**을 클릭하고 **Browserless API**를 검색하세요.
3. 다음 필드를 입력하세요:

| Field | Description |
| :---- | :---- |
| **API Token** | 대시보드에서 얻은 Browserless API 토큰 |

4. **Save**를 클릭하세요.

---

## 3. Browserless MCP 노드 추가

1. Flowise 캔버스에서 chatflow를 열세요.
2. **Agent** 노드를 추가하세요 (예: Tool Agent).
3. **Tools (MCP)** 카테고리에서 **Browserless MCP** 노드를 캔버스로 드래그하세요.
4. Browserless MCP 노드의 출력을 Agent 노드의 **Tools** 입력에 연결하세요.
5. 노드를 구성하세요 (다음 섹션 참조).

---

## 4. 노드 구성

| Parameter | Type | Required | Description |
| :---- | :---- | :---- | :---- |
| **Connect Credential** | Credential selector | Yes | 2단계에서 생성한 Browserless API 자격 증명을 선택하세요. |
| **Available Actions** | Multi-select (async) | Yes | 자격 증명을 연결한 후 **refresh** 아이콘을 클릭하여 Browserless MCP 서버에서 사용 가능한 작업 목록을 로드하세요. 에이전트에 노출할 특정 작업을 선택하세요. |

---

## 5. 작업 선택

유효한 자격 증명을 제공한 후, **Available Actions** 옆의 **refresh** 아이콘을 클릭하세요. 노드는 Browserless MCP 서버에 연결되어 사용 가능한 모든 도구를 검색합니다.

각 작업은 다음과 함께 나열됩니다:

- **Name:** 도구 식별자
- **Description:** 도구의 기능

에이전트가 필요한 작업만 선택하세요. 더 적은 도구는 LLM이 더 나은 결정을 내리고 토큰 사용을 줄이는 데 도움이 됩니다.

---

## 6. 사용 가능한 기능

Browserless MCP 서버는 다음을 포함한 다양한 브라우저 자동화 도구를 제공합니다:

- **Web scraping** — 웹 페이지에서 콘텐츠 추출
- **Screenshots** — 페이지 스크린샷 캡처
- **PDF generation** — 웹 페이지에서 PDF 생성
- **Browser automation** — 프로그래밍 방식으로 페이지와 상호 작용

사용 가능한 모든 작업 목록은 **Available Actions** 드롭다운을 새로 고칠 때 MCP 서버에서 동적으로 로드됩니다.

---

## 7. 외부 참고 자료

| Resource | Link |
| :---- | :---- |
| Browserless MCP Server Docs | [docs.browserless.io/mcp/browserless-mcp-server](https://docs.browserless.io/mcp/browserless-mcp-server) |
| Browserless Documentation | [docs.browserless.io](https://docs.browserless.io) |
| Browserless Website | [browserless.io](https://browserless.io) |