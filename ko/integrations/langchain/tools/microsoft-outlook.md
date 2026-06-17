# Microsoft Outlook

## 사전 필수 사항

Azure Active Directory 사용자에게 할당된 유효한 Microsoft 365 라이선스. 참조: [https://learn.microsoft.com/en-us/answers/questions/761931/microsoft-graph-api-throws-the-mailbox-is-either-i](https://learn.microsoft.com/en-us/answers/questions/761931/microsoft-graph-api-throws-the-mailbox-is-either-i)

## Flowise에서 자격증명 생성

1. 새로운 Microsoft Outlook OAuth2 자격증명 추가
2. 자격증명의 이름을 입력합니다.
3. OAuth Redirect URL을 복사합니다.
4. 다음 필드를 채워야 합니다:
   * Authorization URL
   * Access Token URL
   * Client ID
   * Client Secret

<figure><img src="../../../.gitbook/assets/image (175).png" alt="" width="437"><figcaption></figcaption></figure>

## Azure 애플리케이션 생성 <a href="#h_8276f6aa94" id="h_8276f6aa94"></a>

1. 기존 [Azure](https://login.microsoftonline.com/) 계정에 로그인하거나 아직 가입하지 않았다면 [가입](https://signup.live.com/signup)합니다
2. **App registrations**을 검색합니다.
3. 그런 다음 [App registrations](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/CreateApplicationBlade/quickStartType~/null/isMSAApp~/false)에서 새 Azure 애플리케이션을 등록합니다.

<figure><img src="../../../.gitbook/assets/image (192).png" alt="" width="304"><figcaption></figcaption></figure>

4. "Redirect URI (optional)" 아래에서 "Web"을 선택하고 앞서 복사한 "OAuth Redirect URL"을 붙여넣습니다.

<figure><img src="../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>

5. 애플리케이션을 생성한 후 **Certificates & secrets** > **Client secrets**로 이동하고 "**New client secret**" 버튼을 클릭하여 Client Secret을 생성합니다. 나중에 사용할 Secret을 복사합니다.

<figure><img src="../../../.gitbook/assets/image (200).png" alt=""><figcaption></figcaption></figure>

6. **Overview**로 이동한 후 "**Endpoints**"를 클릭합니다. "**OAuth 2.0 authorization endpoint (v2)**"와 "**OAuth 2.0 token endpoint (v2)**"의 끝점을 복사합니다.

<figure><img src="../../../.gitbook/assets/image (202).png" alt=""><figcaption></figcaption></figure>

7. Endpoints 팝업을 닫고 **Application (client) ID**를 복사합니다:

<figure><img src="../../../.gitbook/assets/image (203).png" alt="" width="563"><figcaption></figcaption></figure>

## Flowise에서 설정 완료

1. 앞서 복사한 모든 값을 입력합니다. 그런 다음 "**Authenticate**"를 클릭합니다:

<figure><img src="../../../.gitbook/assets/image (204).png" alt="" width="440"><figcaption></figcaption></figure>

2. Microsoft 창이 팝업되고 계정을 선택합니다.

{% hint style="warning" %}
계정 사용자는 유효한 Microsoft 365 라이선스를 가져야 합니다
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (205).png" alt="" width="459"><figcaption></figcaption></figure>

3. 필요한 권한을 부여합니다:

<figure><img src="../../../.gitbook/assets/image (206).png" alt="" width="454"><figcaption></figcaption></figure>

4. 팝업이 자동으로 닫히고 자격증명이 저장됩니다.

## Agent Tool로 사용

여러 작업을 선택하여 Agent가 적절한 작업을 지능적으로 선택하도록 할 수 있습니다.\
매개변수를 비워둘 수 있으므로 Agent가 값을 자체적으로 결정할 수 있습니다. 하지만 사용자가 값을 제공하면 Agent의 선택을 재정의합니다.

<figure><img src="../../../.gitbook/assets/image (207).png" alt=""><figcaption></figcaption></figure>

## Tool Node로 사용

결정된 워크플로 시나리오에서 Tool Node로도 사용할 수 있습니다. 예를 들어 다음 단계로 진행하기 전에 Outlook 메시지 목록을 검색합니다.\
이 모드에서는 **Tool Input Arguments를 명시적으로 정의하고 값으로 채워야 합니다**.\
[**Agent Tool로 사용**](microsoft-outlook.md#use-as-agent-tool) 옵션과 달리 입력을 자동으로 결정하는 Agent가 없습니다. 사용자는 고정 값을 입력하거나 이중 중괄호 `{{ }}`로 묶인 변수를 사용하여 필드를 수동으로 채워야 합니다.

<figure><img src="../../../.gitbook/assets/image (208).png" alt=""><figcaption></figcaption></figure>

