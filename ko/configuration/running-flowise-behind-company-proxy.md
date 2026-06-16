# 회사 프록시 뒤에서 Flowise 실행

조직 네트워크 내와 같이 프록시가 필요한 환경에서 Flowise를 실행하는 경우, 선택한 프록시를 통해 모든 백엔드 요청을 라우팅하도록 Flowise를 구성할 수 있습니다. 이 기능은 `global-agent` 패키지에 의해 제공됩니다.

[https://github.com/gajus/global-agent](https://github.com/gajus/global-agent)

## 구성

회사 프록시 뒤에서 Flowise를 실행하기 위해 필요한 2가지 환경 변수가 있습니다:

| 변수                       | 목적                                                                                | 필수 |
| -------------------------- | ----------------------------------------------------------------------------------- | ---- |
| `GLOBAL_AGENT_HTTP_PROXY`  | 모든 서버 HTTP 요청을 프록시할 위치                                                 | 예   |
| `GLOBAL_AGENT_HTTPS_PROXY` | 모든 서버 HTTPS 요청을 프록시할 위치                                                | 아니오 |
| `GLOBAL_AGENT_NO_PROXY`    | 프록시에서 제외해야 할 URL 패턴. 예: `*.foo.com,baz.com`                            | 아니오 |

## 아웃바운드 화이트리스트

엔터프라이즈 플랜의 경우 라이센스 확인을 위해 여러 아웃바운드 연결을 허용해야 합니다. 자세한 정보는 support@flowiseai.com으로 문의하세요.
