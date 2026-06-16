# 회사 프록시 뒤에서 Flowise 실행하기

조직 네트워크 내부와 같이 프록시가 필요한 환경에서 Flowise를 실행하는 경우, 선택한 프록시를 통해 모든 백엔드 요청을 라우팅하도록 Flowise를 구성할 수 있습니다. 이 기능은 `global-agent` 패키지로 구동됩니다.

[https://github.com/gajus/global-agent](https://github.com/gajus/global-agent)

## 설정

회사 프록시 뒤에서 Flowise를 실행하려면 2개의 환경 변수가 필요합니다.

| Variable                   | Purpose                                                                          | Required |
| -------------------------- | -------------------------------------------------------------------------------- | -------- |
| `GLOBAL_AGENT_HTTP_PROXY`  | 모든 서버 HTTP 요청을 프록시로 보낼 위치                                  | Yes      |
| `GLOBAL_AGENT_HTTPS_PROXY` | 모든 서버 HTTPS 요청을 프록시로 보낼 위치                                 | No       |
| `GLOBAL_AGENT_NO_PROXY`    | 프록시 처리에서 제외해야 하는 URL 패턴. 예: `*.foo.com,baz.com` | No       |

## 아웃바운드 허용 목록(Allow-list)

엔터프라이즈 플랜의 경우 라이선스 확인을 위해 여러 아웃바운드 연결을 허용해야 합니다. 자세한 내용은 support@flowiseai.com으로 문의하세요.
