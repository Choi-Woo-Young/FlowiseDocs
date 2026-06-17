# Azure ChatOpenAI

## 필수 요구사항

1. Azure에 [로그인](https://portal.azure.com/)하거나 [가입](https://azure.microsoft.com/en-us/free/)합니다
2. [Azure OpenAI를 만들고](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI) 약 10 영업일 동안 승인을 기다립니다
3. API 키는 **Azure OpenAI** > **name\_azure\_openai** 클릭 > **Click here to manage keys** 클릭에서 사용할 수 있습니다

<figure><img src="../../../.gitbook/assets/azure/azure-general/1.png" alt=""><figcaption></figcaption></figure>

## 설정

### Azure ChatOpenAI

1. **Go to Azure OpenaAI Studio**를 클릭합니다

<figure><img src="../../../.gitbook/assets/azure/azure-general/2.png" alt=""><figcaption></figcaption></figure>

2. **Deployments**를 클릭합니다

<figure><img src="../../../.gitbook/assets/azure/azure-general/3.png" alt=""><figcaption></figcaption></figure>

3. **Create new deployment**를 클릭합니다

<figure><img src="../../../.gitbook/assets/azure/azure-general/4.png" alt=""><figcaption></figcaption></figure>

4. 아래와 같이 선택하고 **Create**를 클릭합니다

<figure><img src="../../../.gitbook/assets/azure/azure-chatopenai/1.png" alt="" width="558"><figcaption></figcaption></figure>

5. **Azure ChatOpenAI** 생성 완료

* Deployment name: `gpt-35-turbo`
* Instance name: `top right conner`

<figure><img src="../../../.gitbook/assets/azure/azure-chatopenai/2.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/azure/azure-general/2.png" alt=""><figcaption></figcaption></figure>

### Flowise

1. **Chat Models** > **Azure ChatOpenAI** 노드를 드래그합니다

<figure><img src="../../../.gitbook/assets/azure/azure-chatopenai/3.png" alt="" width="563"><figcaption></figcaption></figure>

2. **Connect Credential** > **Create New**를 클릭합니다

<figure><img src="../../../.gitbook/assets/azure/azure-chatopenai/4.png" alt="" width="421"><figcaption></figcaption></figure>

3. 각 세부 정보 (API Key, Instance & Deployment name, [API Version](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#chat-completions))를 **Azure ChatOpenAI** 자격증명에 복사하여 붙여넣습니다

<figure><img src="../../../.gitbook/assets/azure/azure-chatopenai/5.png" alt="" width="563"><figcaption></figcaption></figure>

4. 완료되었습니다, Flowise에서 **Azure ChatOpenAI 노드**를 만들었습니다

<figure><img src="../../../.gitbook/assets/azure/azure-general/5.png" alt=""><figcaption></figcaption></figure>

## 리소스

* [LangChain JS Azure ChatOpenAI](https://js.langchain.com/docs/modules/model\_io/models/chat/integrations/azure)
* [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
