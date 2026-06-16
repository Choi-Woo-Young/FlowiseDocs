---
description: Flowise가 LiteLLM Proxy와 통합되는 방법을 알아봅니다.
---

# LiteLLM Proxy

Flowise와 함께 [LiteLLM Proxy](https://docs.litellm.ai/docs/simple_proxy)를 사용하여:

- Azure OpenAI/LLM endpoints 로드 밸런싱
- OpenAI Format에서 100+ LLMs 호출
- Virtual Keys를 사용하여 예산, 속도 제한 설정 및 사용량 추적

## LiteLLM Proxy를 Flowise와 함께 사용하는 방법

### Step 1: LiteLLM config.yaml 파일에 LLM Models를 정의합니다.

LiteLLM은 모든 모델이 정의된 config가 필요합니다 - 이 파일을 `litellm_config.yaml`이라고 부를 것입니다.

[litellm config 설정 방법에 대한 상세 문서 - 여기](https://docs.litellm.ai/docs/proxy/configs)

```yaml
model_list:
  - model_name: gpt-4
    litellm_params:
      model: azure/chatgpt-v-2
      api_base: https://openai-gpt-4-test-v-1.openai.azure.com/
      api_version: "2023-05-15"
      api_key: 
  - model_name: gpt-4
    litellm_params:
      model: azure/gpt-4
      api_key: 
      api_base: https://openai-gpt-4-test-v-2.openai.azure.com/
  - model_name: gpt-4
    litellm_params:
      model: azure/gpt-4
      api_key: 
      api_base: https://openai-gpt-4-test-v-2.openai.azure.com/
```


### Step 2. litellm proxy 시작

```shell
docker run \
    -v $(pwd)/litellm_config.yaml:/app/config.yaml \
    -p 4000:4000 \
    ghcr.io/berriai/litellm:main-latest \
    --config /app/config.yaml --detailed_debug
```

성공하면, proxy가 `http://localhost:4000/`에서 실행됩니다.

### Step 3: Flowise에서 LiteLLM Proxy를 사용합니다.

Flowise에서, **표준 OpenAI nodes (Azure OpenAI nodes가 아닌)를 지정합니다** -- 이는 **chat models, embeddings, llms -- 모든 것**에 적용됩니다.

- `BasePath`를 LiteLLM Proxy URL (`http://localhost:4000` 로컬에서 실행할 때)로 설정합니다.
- 다음 headers `Authorization: Bearer <your-litellm-master-key>`를 설정합니다.

