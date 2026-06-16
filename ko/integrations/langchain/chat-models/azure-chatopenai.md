# ChatOpenAI

## 사전 준비 (Prerequisite)

1. [OpenAI](https://openai.com/) 계정
2. [API key](https://platform.openai.com/api-keys) 생성

## 설정 (Setup)

1. **Chat Models** > **ChatOpenAI** node를 드래그합니다

<figure><img src="../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

2. **Connect Credential** > **Create New**를 클릭합니다

<figure><img src="../../../.gitbook/assets/image_openAI (1).png" alt="" width="278"><figcaption></figcaption></figure>

2. **ChatOpenAI** credential을 입력합니다

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

4. 짜잔 [🎉](https://emojipedia.org/party-popper/), 이제 Flowise에서 **ChatOpenAI node**를 사용할 수 있습니다

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## 커스텀 base URL 및 header

Flowise는 Chat OpenAI에 대한 커스텀 base URL 및 header 사용을 지원합니다. 사용자는 OpenAI API 호환성을 지원하는 OpenRouter, TogetherAI 등의 통합을 쉽게 사용할 수 있습니다.

### TogetherAI

1. TogetherAI의 공식 [문서](https://docs.together.ai/docs/openai-api-compatibility#nodejs)를 참조하세요
2. TogetherAI API key로 새 credential을 생성합니다
3. ChatOpenAI node에서 **Additional Parameters**를 클릭합니다.
4. Base Path를 변경합니다:

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

### Open Router

1. OpenRouter의 공식 [문서](https://openrouter.ai/docs#quick-start)를 참조하세요
2. OpenRouter API key로 새 credential을 생성합니다
3. ChatOpenAI node에서 Additional Parameters를 클릭합니다
4. Base Path와 Base Options를 변경합니다:

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## 커스텀 모델 (Custom Model)

ChatOpenAI node에서 지원되지 않는 모델의 경우 ChatOpenAI Custom을 사용할 수 있습니다. 이를 통해 사용자는 `mistralai/Mixtral-8x7B-Instruct-v0.1`과 같은 모델 이름을 입력할 수 있습니다.

<figure><img src="../../../.gitbook/assets/image (84).png" alt=""><figcaption></figcaption></figure>

## 이미지 업로드 (Image Upload)

LLM이 이미지를 업로드하고 분석하도록 허용할 수도 있습니다. 내부적으로 Flowise는 [OpenAI Vison ](https://platform.openai.com/docs/guides/vision)모델을 사용하여 이미지를 처리합니다. LLMChain, Conversation Chain, ReAct Agent, Conversational Agent에서만 작동합니다.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="332"><figcaption></figcaption></figure>

이제 채팅 인터페이스에서 새로운 이미지 업로드 버튼을 볼 수 있습니다:

<figure><img src="../../../.gitbook/assets/Untitled (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>
