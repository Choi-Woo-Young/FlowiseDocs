# ChatOpenAI

## 필수 요구사항

1. [OpenAI](https://openai.com/) 계정
2. [API 키](https://platform.openai.com/api-keys) 생성

## 설정

1. **Chat Models** > **ChatOpenAI** 노드를 드래그합니다

<figure><img src="../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

2. **Connect Credential** > **Create New**를 클릭합니다

<figure><img src="../../../.gitbook/assets/image_openAI (1).png" alt="" width="278"><figcaption></figcaption></figure>

2. **ChatOpenAI** 자격증명을 입력합니다

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

4. 완료되었습니다, Flowise에서 **ChatOpenAI 노드**를 사용할 수 있습니다

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## 사용자 정의 기본 URL 및 헤더

Flowise는 Chat OpenAI용 사용자 정의 기본 URL 및 헤더를 사용할 수 있도록 지원합니다. 사용자는 OpenRouter, TogetherAI 등 OpenAI API 호환성을 지원하는 통합을 쉽게 사용할 수 있습니다.

### TogetherAI

1. TogetherAI의 공식 [문서](https://docs.together.ai/docs/openai-api-compatibility#nodejs)를 참조하세요
2. TogetherAI API 키로 새 자격증명을 생성합니다
3. ChatOpenAI 노드에서 **Additional Parameters**를 클릭합니다.
4. Base Path를 변경합니다:

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

### Open Router

1. OpenRouter의 공식 [문서](https://openrouter.ai/docs#quick-start)를 참조하세요
2. OpenRouter API 키로 새 자격증명을 생성합니다
3. ChatOpenAI 노드에서 Additional Parameters를 클릭합니다
4. Base Path 및 Base Options를 변경합니다:

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## 사용자 정의 모델

ChatOpenAI 노드에서 지원하지 않는 모델의 경우 ChatOpenAI Custom을 사용할 수 있습니다. 이를 통해 사용자는 `mistralai/Mixtral-8x7B-Instruct-v0.1`와 같은 모델 이름을 입력할 수 있습니다

<figure><img src="../../../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

## 이미지 업로드

LLM이 이미지를 업로드하고 분석할 수 있도록 허용할 수도 있습니다. 내부적으로 Flowise는 [OpenAI Vison](https://platform.openai.com/docs/guides/vision) 모델을 사용하여 이미지를 처리합니다. LLMChain, Conversation Chain, ReAct Agent 및 Conversational Agent에서만 작동합니다.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="332"><figcaption></figcaption></figure>

채팅 인터페이스에서 이제 새로운 이미지 업로드 버튼이 보입니다:

<figure><img src="../../../.gitbook/assets/Untitled (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>
