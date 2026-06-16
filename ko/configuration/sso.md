# SSO

{% hint style="info" %}
SSO는 Enterprise 플랜에서만 사용 가능합니다
{% endhint %}

Flowise는 사용자가 애플리케이션에 액세스하기 위해 _SSO_(Single Sign-On)를 사용할 수 있도록 하는 [OIDC](https://openid.net/)를 지원합니다. 현재 [조직 관리자](../using-flowise/workspaces.md#setting-up-admin-account)만 SSO 설정을 구성할 수 있습니다.

## Microsoft

1. In the Azure portal, search for Microsoft Entra ID:

<figure><img src="../.gitbook/assets/image (193).png" alt=""><figcaption></figcaption></figure>

2. From the left hand bar, click App Registrations, then New Registration:

<figure><img src="../.gitbook/assets/image (194).png" alt=""><figcaption></figcaption></figure>

3. Enter an app name, and select Single Tenant:

<figure><img src="../.gitbook/assets/image (195).png" alt=""><figcaption></figcaption></figure>

4. After an app is created, note down the Application (client) ID and Directory (tenant) ID:

<figure><img src="../.gitbook/assets/image (196).png" alt=""><figcaption></figcaption></figure>

5. On the left side bar, click Certificates & secrets -> New client secret -> Add:

<figure><img src="../.gitbook/assets/image (198).png" alt=""><figcaption></figcaption></figure>

6. After the secret has been created, copy the Value, <mark style="color:red;">not</mark> the Secret ID:

<figure><img src="../.gitbook/assets/image (199).png" alt=""><figcaption></figcaption></figure>

7. On the left side bar, click Authentication -> Add a platform -> Web:

<figure><img src="../.gitbook/assets/image (201).png" alt=""><figcaption></figcaption></figure>

8. Fill in the redirect URIs. This will need to be changed depending on how you are hosting it: `http[s]://[your-flowise-instance.com]/api/v1/azure/callback`:

<figure><img src="../.gitbook/assets/image (218).png" alt="" width="514"><figcaption></figcaption></figure>

9. You should be able to see the new Redirect URI created:

<figure><img src="../.gitbook/assets/image (219).png" alt=""><figcaption></figcaption></figure>

10. Back to Flowise app, login as Organization Admin. Navigate to SSO Config from left side bar. Fill in the Azure Tenant ID and Client ID from Step 4, and Client Secret from Step 6. Click Test Configuration to see if the connection can be established successfully:

<figure><img src="../.gitbook/assets/image (220).png" alt="" width="563"><figcaption></figcaption></figure>

11. Lastly, enable and save it:

<figure><img src="../.gitbook/assets/image (221).png" alt="" width="563"><figcaption></figcaption></figure>

12. Before users can sign in using SSO, they have to be invited first. Refer to [Inviting users for SSO sign in](sso.md#inviting-users-for-sso-sign-in) for step by step guide. Invited users must also be part of the Directory Users in Azure.

<figure><img src="../.gitbook/assets/image (2) (1) (2).png" alt=""><figcaption></figcaption></figure>

## Google

To enable Sign In With Google on your website, you first need to set up your Google API client ID. To do so, complete the following steps:

1. Open the **Credentials** page of the [Google APIs console](https://console.developers.google.com/apis).
2. Click **Create credentials** > **OAuth client ID**

<figure><img src="../.gitbook/assets/image (224).png" alt="" width="563"><figcaption></figcaption></figure>

3\. Select **Web Application**:

<figure><img src="../.gitbook/assets/image (225).png" alt="" width="504"><figcaption></figcaption></figure>

4\. Fill in the redirect URIs. This will need to be changed depending on how you are hosting it: `http[s]://[your-flowise-instance.com]/api/v1/google/callback`:

<figure><img src="../.gitbook/assets/image (226).png" alt="" width="563"><figcaption></figcaption></figure>

5\. After creating, grab the client ID and secret:

<figure><img src="../.gitbook/assets/image (227).png" alt=""><figcaption></figcaption></figure>

6\. Back to Flowise app, add the Client ID and secret. Test the connection and Save it.

<figure><img src="../.gitbook/assets/image (228).png" alt="" width="563"><figcaption></figcaption></figure>

## Auth0

1. Register an account on [Auth0](https://auth0.com/), then create a new Application

<figure><img src="../.gitbook/assets/image (229).png" alt=""><figcaption></figcaption></figure>

2. Select **Regular Web Application**:

<figure><img src="../.gitbook/assets/image (230).png" alt=""><figcaption></figcaption></figure>

3. Configure the fields such as Name, Description. Take notes of the **Domain**, **Client ID**, and **Client Secret**.

<figure><img src="../.gitbook/assets/image (231).png" alt=""><figcaption></figcaption></figure>

4\. Fill in the Application URIs. This will need to be changed depending on how you are hosting it: `http[s]://[your-flowise-instance.com]/api/v1/auth0/callback`:

<figure><img src="../.gitbook/assets/image (232).png" alt=""><figcaption></figcaption></figure>

5. In the API’s tab, ensure that Auth0 Management API is enabled with the following permissions
   * read:users
   * read:client\_grants

<figure><img src="../.gitbook/assets/image (233).png" alt=""><figcaption></figcaption></figure>

6\. Back to Flowise App, fill in the Domain, Client ID and Secret. Test and Save the configuration.

<figure><img src="../.gitbook/assets/image (234).png" alt="" width="563"><figcaption></figcaption></figure>

## SSO 로그인을 위한 사용자 초대

새 사용자가 로그인할 수 있으려면 Flowise 애플리케이션에 새 사용자를 초대해야 합니다. 이는 초대된 사용자의 역할/워크스페이스 레코드를 유지하는 데 필수적입니다. 환경 변수 설정에 대해서는 [사용자 초대](../using-flowise/workspaces.md#invite-user) 섹션을 참조하세요.

초대된 사용자는 로그인 초대 링크를 받을 것입니다:

<figure><img src="../.gitbook/assets/image (222).png" alt="" width="449"><figcaption></figcaption></figure>

버튼을 클릭하면 초대된 사용자가 직접 Flowise SSO 로그인 화면으로 이동합니다:

<figure><img src="../.gitbook/assets/image (210).png" alt="" width="400"><figcaption></figcaption></figure>

또는 Flowise 앱으로 이동하여 SSO로 로그인합니다:

<figure><img src="../.gitbook/assets/image (211).png" alt="" width="437"><figcaption></figcaption></figure>
