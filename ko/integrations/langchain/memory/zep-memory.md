# Zep 메모리

[Zep](https://github.com/getzep/zep)는 LLM 애플리케이션을 위한 장기 메모리 저장소입니다. LLM 앱/챗봇 이력을 저장, 요약, 임베드, 인덱싱 및 보강하며, 간단하고 낮은 지연 시간의 API를 통해 이를 노출합니다.

## Zep를 Render에 배포하는 가이드

[Render](https://render.com/), [Flyio](https://fly.io/)와 같은 클라우드 서비스에 Zep을 쉽게 배포할 수 있습니다. 로컬에서 테스트하는 것을 선호한다면 [빠른 시작 가이드](https://github.com/getzep/zep#quick-start)를 따라 Docker 컨테이너를 실행할 수도 있습니다.

이 예제에서는 Render에 배포하겠습니다.

1. [Zep Repo](https://github.com/getzep/zep#quick-start)로 이동하여 **Deploy to Render**를 클릭합니다.
2. Render의 Blueprint 페이지로 이동하고 **Create New Resources**를 클릭합니다.

<figure><img src="../../../.gitbook/assets/image (21) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. 배포가 완료되면 대시보드에 3개의 애플리케이션이 생성된 것을 볼 수 있습니다.

<figure><img src="../../../.gitbook/assets/image (1) (2).png" alt=""><figcaption></figcaption></figure>

4. **zep**이라고 이름이 붙은 첫 번째를 클릭하고 배포된 URL을 복사합니다.

<figure><img src="../../../.gitbook/assets/image (38) (1).png" alt=""><figcaption></figcaption></figure>

## Zep를 Digital Ocean에 배포하는 가이드 (Docker를 통해)

1. 저장소 클론

```bash
git clone https://github.com/getzep/zep.git
cd zep
nano .env

```

2. .env 파일에 OpenAI API 키 추가

```bash
ZEP_OPENAI_API_KEY=

```

```bash
docker compose up -d --build
```

3. 포트 8000에 대한 방화벽 접근 허용

```bash
sudo ufw allow from any to any port 8000 proto tcp
ufw status numbered
```

Digital Ocean에서 대시보드와 별도로 방화벽을 사용하는 경우, 포트 8000도 거기에 추가되었는지 확인하세요.

## Flowise UI에서 사용

1. Flowise 애플리케이션으로 돌아가 새 캔버스를 만들거나 마켓플레이스의 템플릿 중 하나를 사용합니다. 이 예제에서는 **Simple Conversational Chain**을 사용하겠습니다.

<figure><img src="../../../.gitbook/assets/Untitled (3) (1).png" alt=""><figcaption></figcaption></figure>

2. **Buffer Memory**를 **Zep Memory**로 바꿉니다. 그런 다음 **Base URL**을 위에서 복사한 Zep URL로 바꿉니다.

<figure><img src="../../../.gitbook/assets/Untitled (5).png" alt=""><figcaption></figcaption></figure>

3. 챗플로우를 저장하고 테스트하여 대화가 기억되는지 확인합니다.

<figure><img src="../../../.gitbook/assets/image (27).png" alt=""><figcaption></figcaption></figure>

4. 이제 대화 기록을 지워보면 이제 이전 대화를 기억할 수 없음을 알 수 있습니다.

<figure><img src="../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Zep 인증

Zep는 JWT 인증을 사용하여 인스턴스를 보호할 수 있게 해줍니다. [여기](https://github.com/getzep/zepcli/releases)의 `zepcli` 명령줄 유틸리티를 사용합니다.

#### 1. 시크릿과 JWT 토큰 생성 <a href="#id-1-generate-a-secret-and-the-jwt-token" id="id-1-generate-a-secret-and-the-jwt-token"></a>

ZepCLI를 다운로드한 후:

Linux 또는 MacOS에서

```
./zepcli -i
```

Windows에서

```
zepcli.exe -i
```

먼저 SECRET 토큰을 받게 됩니다:

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

그 다음 JWT 토큰을 받게 됩니다:

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### 2. 인증 환경 변수 구성 <a href="#id-2-configure-auth-environment-variables" id="id-2-configure-auth-environment-variables"></a>

Zep 서버 환경에서 다음 환경 변수를 설정합니다:

```
ZEP_AUTH_REQUIRED=true
ZEP_AUTH_SECRET=<the secret you generated above>
```

#### 3. Flowise에서 자격 증명 구성 <a href="#id-2-configure-auth-environment-variables" id="id-2-configure-auth-environment-variables"></a>

Zep의 새로운 자격 증명을 추가하고 API Key 필드에 JWT 토큰을 입력합니다:

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 4. Zep 노드에서 생성된 자격 증명 사용 <a href="#id-2-configure-auth-environment-variables" id="id-2-configure-auth-environment-variables"></a>

Zep 노드의 Connect Credential에서 방금 생성한 자격 증명을 선택합니다. 그게 다입니다!

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>