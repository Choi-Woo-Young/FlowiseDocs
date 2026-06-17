# IBM Watsonx

## 필수 요구사항

1. [IBM Watsonx](https://www.ibm.com/watsonx)에서 계정을 등록합니다
2. 새 프로젝트를 만듭니다:

<figure><img src="../../../.gitbook/assets/image (238).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (239).png" alt=""><figcaption></figcaption></figure>

3. 프로젝트가 생성된 후 메인 대시보드로 돌아가서 **Explore foundation models**를 클릭합니다:

<figure><img src="../../../.gitbook/assets/image (240).png" alt=""><figcaption></figcaption></figure>

4. 사용하려는 모델을 선택하고 Prompt Lab에서 엽니다:

<figure><img src="../../../.gitbook/assets/image (241).png" alt=""><figcaption></figcaption></figure>

5. 오른쪽 상단 모서리에서 View Code를 클릭합니다:

<figure><img src="../../../.gitbook/assets/image (242).png" alt=""><figcaption></figcaption></figure>

6. `model_id` 및 `version` 매개변수를 기록해둡니다. 이 경우 `ibm/granite-3-8b-instruct`이고 버전은 `2023-05-29`입니다.
7. 왼쪽 네비게이션 바를 클릭하고 Developer access를 클릭합니다

<figure><img src="../../../.gitbook/assets/image (243).png" alt="" width="308"><figcaption></figcaption></figure>

8. `watsonx.ai URL`, `Project ID`를 기록해두고 IBM Cloud Console에서 새 API 키를 만듭니다.
9. 이 시점에서 다음 정보를 가지고 있어야 합니다:
   * Watsonx.ai URL
   * Project ID
   * API Key
   * Model's version
   * Model's ID

## 설정

1. **Chat Models** > **ChatIBMWatsonx** 노드를 드래그합니다

<figure><img src="../../../.gitbook/assets/image (244).png" alt="" width="306"><figcaption></figcaption></figure>

2. Model을 이전 Model ID로 채웁니다. Create New Credential을 클릭하고 모든 세부 정보를 입력합니다.

<figure><img src="../../../.gitbook/assets/image (245).png" alt="" width="419"><figcaption></figcaption></figure>

2. 완료되었습니다, 이제 Flowise에서 **ChatIBMWatsonx 노드**를 사용할 수 있습니다!

<figure><img src="../../../.gitbook/assets/image (246).png" alt=""><figcaption></figcaption></figure>
