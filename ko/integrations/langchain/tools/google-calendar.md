# Google Calendar

## Flowise에서 자격증명 생성

1. 새로운 Google Calendar OAuth2 자격증명 추가
2. 자격증명의 이름을 입력합니다.
3. OAuth Redirect URL을 복사합니다.
4. 다음 필드를 채워야 합니다:
   * Client ID
   * Client Secret

<figure><img src="../../../.gitbook/assets/image (266).png" alt="" width="422"><figcaption></figcaption></figure>

## Google 프로젝트 생성/사용

1. [**Google Cloud**](https://console.cloud.google.com/) 계정에 로그인합니다.
2. [**Google Cloud Console > APIs & Services**](https://console.cloud.google.com/apis/credentials)로 이동하고 왼쪽 상단의 드롭다운에서 사용하려는 프로젝트를 선택합니다 (또는 새 프로젝트를 생성하고 선택합니다).
3. 아직 구성하지 않았다면 **OAuth 동의 화면**을 설정합니다.

<figure><img src="../../../.gitbook/assets/image (256).png" alt="" width="563"><figcaption></figcaption></figure>

4. **자격증명**으로 이동한 후 **+ CREATE CREDENTIALS > OAuth client ID**를 클릭합니다.

<figure><img src="../../../.gitbook/assets/image (257).png" alt="" width="563"><figcaption></figcaption></figure>

5. **Application type** 드롭다운에서 **Web application**을 선택합니다.
6. **Authorized redirect URIs** 아래에서 **+ ADD URI**를 클릭하고 앞서 복사한 OAuth Redirect URL을 붙여넣습니다.
7. **Create**을 클릭합니다.

<figure><img src="../../../.gitbook/assets/image (258).png" alt="" width="407"><figcaption></figcaption></figure>

8. Client ID와 Client Secret을 복사합니다:

<figure><img src="../../../.gitbook/assets/image (259).png" alt="" width="489"><figcaption></figcaption></figure>

9. **Enabled APIs & Services**에서 **+ ENABLE APIS AND SERVICES**를 클릭합니다.
10. **Google Calendar API**를 검색하고 활성화합니다.

<figure><img src="../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

11. **자격증명**으로 돌아가서 **OAuth 2.0 Client IDs** 아래에서 새로 생성한 자격증명을 클릭하고 상세 페이지에서 **Client ID**와 **Client Secret**을 찾을 수 있습니다.

## Flowise에서 설정 완료

1. 앞서 복사한 모든 값을 입력합니다. 그런 다음 "**Authenticate**"를 클릭합니다:

<figure><img src="../../../.gitbook/assets/image (267).png" alt="" width="440"><figcaption></figcaption></figure>

2. Google 로그인 창이 팝업됩니다:

<figure><img src="../../../.gitbook/assets/image (261).png" alt="" width="448"><figcaption></figcaption></figure>

3. 권한을 승인합니다:

<figure><img src="../../../.gitbook/assets/image (263).png" alt="" width="373"><figcaption></figcaption></figure>

4. 팝업 창이 자동으로 닫히고 자격증명이 저장되어 사용할 준비가 됩니다.

## Agent Tool로 사용

여러 작업을 선택하여 Agent가 적절한 작업을 지능적으로 선택하도록 할 수 있습니다.\
매개변수를 비워둘 수 있으므로 Agent가 값을 자체적으로 결정할 수 있습니다. 하지만 사용자가 값을 제공하면 Agent의 선택을 재정의합니다.

<figure><img src="../../../.gitbook/assets/image (268).png" alt=""><figcaption></figcaption></figure>

## Tool Node로 사용

결정된 워크플로 시나리오에서 Tool Node로도 사용할 수 있습니다. 예를 들어 다음 단계로 진행하기 전에 초안 메시지 목록을 검색합니다.\
이 모드에서는 **Tool Input Arguments를 명시적으로 정의하고 값으로 채워야 합니다**.\
[**Agent Tool로 사용**](google-calendar.md#use-as-agent-tool) 옵션과 달리 입력을 자동으로 결정하는 Agent가 없습니다. 사용자는 고정 값을 입력하거나 이중 중괄호 `{{ }}`로 묶인 변수를 사용하여 필드를 수동으로 채워야 합니다.

<figure><img src="../../../.gitbook/assets/image (269).png" alt=""><figcaption></figcaption></figure>
