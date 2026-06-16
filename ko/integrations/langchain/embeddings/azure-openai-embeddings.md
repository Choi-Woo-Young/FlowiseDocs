# Azure OpenAI Embeddings

## 사전 요구사항

1. Azure에 [로그인](https://portal.azure.com/)하거나 [가입](https://azure.microsoft.com/en-us/free/)
2. [Azure OpenAI 생성](https://portal.azure.com/#create/Microsoft.CognitiveServicesOpenAI)하고 약 10 영업일 동안 승인 대기
3. API 키는 **Azure OpenAI** > **name\_azure\_openai** 클릭 > **Click here to manage keys** 클릭에서 확인 가능

<figure><img src="../../../.gitbook/assets/azure/azure-general/1.png" alt=""><figcaption></figcaption></figure>

## 설정

### Azure OpenAI Embeddings

1. **Go to Azure OpenaAI Studio** 클릭

<figure><img src="../../../.gitbook/assets/azure/azure-general/2.png" alt=""><figcaption></figcaption></figure>

2. **Deployments** 클릭

<figure><img src="../../../.gitbook/assets/azure/azure-general/3.png" alt=""><figcaption></figcaption></figure>

3. **Create new deployment** 클릭

<figure><img src="../../../.gitbook/assets/azure/azure-general/4.png" alt=""><figcaption></figcaption></figure>

4. 아래와 같이 선택하고 **Create** 클릭

<figure><img src="../../../.gitbook/assets/azure/azure-openai-embeddings/1.png" alt="" width="559"><figcaption></figcaption></figure>

5. **Azure OpenAI Embeddings** 생성 완료

* Deployment name: `text-embedding-ada-002`
* Instance name: `top right conner`

<figure><img src="../../../.gitbook/assets/azure/azure-openai-embeddings/2.png" alt=""><figcaption></figcaption></figure>

### Flowise

1. **Embeddings** > **Azure OpenAI Embeddings** 노드 드래그

<figure><img src="../../../.gitbook/assets/azure/azure-openai-embeddings/3.png" alt="" width="563"><figcaption></figcaption></figure>

2. **Connect Credential** > **Create New** 클릭

<figure><img src="../../../.gitbook/assets/azure/azure-openai-embeddings/4.png" alt="" width="386"><figcaption></figcaption></figure>

3. 각 세부 정보(API Key, Instance & Deployment name, [API Version](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference#chat-completions))를 **Azure OpenAI Embeddings** 자격증명에 복사 및 붙여넣기

<figure><img src="../../../.gitbook/assets/azure/azure-openai-embeddings/5.png" alt="" width="554"><figcaption></figcaption></figure>

4. 완료, Flowise에서 **Azure OpenAI Embeddings 노드**를 생성했습니다.

<figure><img src="../../../.gitbook/assets/azure/azure-general/5.png" alt=""><figcaption></figcaption></figure>

## 리소스

* [LangChain JS Azure OpenAI Embeddings](https://js.langchain.com/docs/modules/data\_connection/text\_embedding/integrations/azure\_openai)
* [Azure OpenAI Service REST API reference](https://learn.microsoft.com/en-us/azure/ai-services/openai/reference)
