# SingleStore

## 설정

1. [SingleStore](https://www.singlestore.com/)에서 계정을 등록합니다
2. 포털에 로그인합니다. 왼쪽 사이드 패널에서 **CLOUD** -> **Create new workspace group**을 클릭합니다. 그런 다음 **Create Workspace** 버튼을 클릭합니다.

<figure><img src="../../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

3. cloud provider와 데이터 region을 선택한 다음 **Next**를 클릭합니다:

<figure><img src="../../../.gitbook/assets/image (57).png" alt=""><figcaption></figcaption></figure>

4. 검토한 후 **Create Workspace**를 클릭합니다:

<figure><img src="../../../.gitbook/assets/image (58).png" alt=""><figcaption></figcaption></figure>

5. 이제 생성된 workspace를 확인할 수 있습니다:

<figure><img src="../../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

6. 데이터베이스 생성을 진행합니다

<figure><img src="../../../.gitbook/assets/image (65).png" alt="" width="485"><figcaption></figcaption></figure>

7. 생성된 데이터베이스가 workspace에 연결된 것을 확인할 수 있습니다:

<figure><img src="../../../.gitbook/assets/image (66).png" alt=""><figcaption></figcaption></figure>

8. workspace 드롭다운에서 Connect를 클릭합니다 -> Connect Directly:

<figure><img src="../../../.gitbook/assets/image (61).png" alt="" width="418"><figcaption></figcaption></figure>

9. 새 비밀번호를 지정하거나 기본 생성된 비밀번호를 사용할 수 있습니다. 그런 다음 Continue를 클릭합니다:

<figure><img src="../../../.gitbook/assets/image (62).png" alt="" width="485"><figcaption></figcaption></figure>

10. 탭에서 **Your App**으로 전환한 다음 드롭다운에서 **Node.js**를 선택합니다. 나중에 Flowise에서 필요하므로 `Username`, `Host`, `Password`를 기록/저장해 두세요.

<figure><img src="../../../.gitbook/assets/image (63).png" alt="" width="563"><figcaption></figcaption></figure>

11. Flowise canvas로 돌아가서 SingleStore node를 드래그 앤 드롭합니다. Credentials 드롭다운에서 **Create New**를 클릭합니다:

<figure><img src="../../../.gitbook/assets/image (4) (1) (2) (1) (1).png" alt="" width="271"><figcaption></figcaption></figure>

11. 위에서 얻은 Username과 Password를 입력합니다:

<figure><img src="../../../.gitbook/assets/image (64).png" alt="" width="563"><figcaption></figcaption></figure>

13. 그런 다음 Host와 Database Name을 지정합니다:

<figure><img src="../../../.gitbook/assets/image (5) (1) (2).png" alt="" width="272"><figcaption></figcaption></figure>

13. 이제 SingleStore로 데이터 upsert를 시작할 수 있습니다:

<figure><img src="../../../.gitbook/assets/image (6) (1) (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (7) (1) (2).png" alt=""><figcaption></figcaption></figure>

14. SingleStore 포털로 돌아가서 데이터베이스로 이동하면 upsert된 모든 데이터를 확인할 수 있습니다:

<figure><img src="../../../.gitbook/assets/image (70).png" alt=""><figcaption></figcaption></figure>