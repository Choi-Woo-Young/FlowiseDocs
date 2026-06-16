# Cloud Migration

이 가이드는 Cloud V1에서 V2로 마이그레이션하는 데 도움을 주기 위한 것입니다.

Cloud V1에서 apps의 URL은 <mark style="color:blue;">**https://\<your-instance-name>.app.flowiseai.com**</mark>처럼 보입니다.

Cloud V2에서 apps의 URL은 <mark style="color:blue;">**https://cloud.flowiseai.com**</mark>입니다.

Cloud V2는 왜일까요? 우리는 처음부터 cloud를 재작성했으며, 5배의 속도 향상, 여러 workspaces를 가질 수 있는 능력, 조직 members, 그리고 가장 중요하게는 [production-ready architecture](../configuration/running-in-production.md)로 높은 확장성을 갖추고 있습니다.

1. [https://flowiseai.com/auth/login](https://flowiseai.com/auth/login)을 통해 Cloud V1에 로그인합니다.
2. 대시보드의 오른쪽 상단 모서리에서:

<figure><img src="../.gitbook/assets/image (8) (2).png" alt=""><figcaption></figcaption></figure>

3. **Select Version, then update to the latest version.**

<figure><img src="../.gitbook/assets/migration-guide/cloud-migration/3.png" alt="" width="563"><figcaption></figcaption></figure>

4. Select Export를 선택하고, 내보낼 데이터를 선택합니다:

<figure><img src="../.gitbook/assets/image (20) (2).png" alt="" width="563"><figcaption></figcaption></figure>

5. 내보낸 JSON 파일을 저장합니다.
6. Cloud V2 [https://cloud.flowiseai.com](https://cloud.flowiseai.com/)로 이동합니다.
7. Cloud V2 계정은 Cloud V1의 기존 계정과 동기화되지 않으므로 다시 등록하거나 Google/Github으로 로그인해야 합니다.

<figure><img src="../.gitbook/assets/image (37).png" alt="" width="563"><figcaption></figcaption></figure>

8. 로그인하면 대시보드 오른쪽 상단 모서리에서 Import를 클릭하고 내보낸 JSON 파일을 업로드합니다.

<figure><img src="../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

9. 새 사용자는 기본적으로 2개의 flows와 assistants (각각)에 대한 제한이 있는 **Free Plan**에 있습니다. 내보낸 데이터가 그 이상이면 내보낸 JSON 파일을 가져오면 오류가 발생합니다. 이것이 우리가 무제한 flows & assistants를 가진 **Starter Plan**에 <mark style="color:orange;">**첫 달 무료**</mark>를 제공하는 이유입니다!

<figure><img src="../.gitbook/assets/image (55).png" alt=""><figcaption></figcaption></figure>

10. **Get Started** 버튼을 클릭하고 선호하는 payment method를 추가합니다:

<figure><img src="../.gitbook/assets/image (67).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (80).png" alt=""><figcaption></figcaption></figure>

11. Payment method를 추가한 후 Flowise로 돌아가서 선택한 plan에서 Get Started를 클릭하고 Confirm Change를 클릭합니다:

<figure><img src="../.gitbook/assets/image (95).png" alt="" width="563"><figcaption></figcaption></figure>

12. 모든 것이 순조롭게 진행되면 무제한 flows & assistants를 가진 Starter Plan에 있어야 합니다! 만세 :tada: 이전에 free plan 제한으로 인해 실패한 경우 JSON 파일을 다시 가져오기 시도해 보십시오.

{% hint style="success" %}
내보낸 데이터의 모든 ID는 동일하게 유지되므로 API의 ID를 업데이트할 걱정을 할 필요가 없으며 [https://cloud.flowiseai.com/api/v1/prediction/69fb1055-ghj324-ghj-0a4ytrerf](https://cloud.flowiseai.com/api/v1/prediction/69fb1055-ghj324-ghj-0a4ytrerf)와 같은 URL을 업데이트하면 됩니다.
{% endhint %}

{% hint style="warning" %}
자격증명은 내보내지지 않습니다. 새 자격증명을 만들고 flows 및 assistants에서 사용해야 합니다.
{% endhint %}

13. 모든 것이 예상대로 작동함을 확인한 후 Cloud V1 subscription을 취소할 수 있습니다.
14. 왼쪽 side panel에서 Account Settings를 클릭하고 아래로 스크롤하면 **Cancel Previous Subscription**를 볼 수 있습니다:

<figure><img src="../.gitbook/assets/image (135).png" alt=""><figcaption></figcaption></figure>

15. Cloud V1에 가입할 때 사용했던 이전 이메일을 입력하고 **Send Instructions**를 누릅니다.
16. 그러면 Cloud V1 subscription을 취소할 이메일을 받게 됩니다:

<figure><img src="../.gitbook/assets/image (136).png" alt="" width="563"><figcaption></figcaption></figure>

17. **Manage Subscription** 버튼을 클릭하면 Cloud V1 subscription을 취소할 수 있는 portal로 이동합니다. Cloud V1 app은 다음 결제 주기에 종료됩니다.

<figure><img src="../.gitbook/assets/image (137).png" alt=""><figcaption></figcaption></figure>

마이그레이션 과정에서 발생한 불편함을 진심으로 사과드립니다. 도움이 필요하면 support@flowiseai.com으로 언제든지 문의해 주세요.
