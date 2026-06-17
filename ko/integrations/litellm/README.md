---
description: Flowise가 LiteLLM Proxy와 통합되는 방식을 알아봅니다
---

# LiteLLM Proxy

Flowise와 [LiteLLM Proxy](https://docs.litellm.ai/docs/simple_proxy)를 사용하여:

- Azure OpenAI/LLM 엔드포인트 부하 분산
- OpenAI 형식의 100개 이상의 LLM 호출
- Virtual Keys를 사용하여 예산, 속도 제한 및 사용 추적

## Flowise에서 LiteLLM Proxy 사용하기

### 단계 1: LiteLLM config.yaml 파일에서 LLM 모델 정의

LiteLLM는 모든 모델이 정의된 설정 파일이 필요합니다. 이 파일을 `litellm_config.yaml`이라고 합니다.

[litellm 설정 방법에 대한 자세한 설명서](https://docs.litellm.ai/docs/proxy/configs)

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


### 단계 2. litellm 프록시 시작

```shell
docker run \
    -v $(pwd)/litellm_config.yaml:/app/config.yaml \
    -p 4000:4000 \
    ghcr.io/berriai/litellm:main-latest \
    --config /app/config.yaml --detailed_debug
```

성공하면 프록시가 `http://localhost:4000/`에서 실행됩니다.

### 단계 3: Flowise에서 LiteLLM Proxy 사용

Flowise에서 **표준 OpenAI 노드(Azure OpenAI 노드 아님)** 를 지정합니다. 이는 **채팅 모델, 임베딩, llm -- 모든 것**에 적용됩니다.

- `BasePath`를 LiteLLM Proxy URL(`http://localhost:4000` (로컬 실행 시))로 설정
- `Authorization: Bearer <your-litellm-master-key>` 헤더 설정

