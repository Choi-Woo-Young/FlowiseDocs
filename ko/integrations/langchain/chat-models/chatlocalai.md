# ChatLocalAI

## LocalAI 설정

[**LocalAI**](https://github.com/go-skynet/LocalAI)는 로컬 추론을 위해 OpenAI API 사양과 호환되는 드롭인 교체 REST API입니다. 이를 통해 LLM(그리고 그 이상)을 로컬 또는 온프레미스에서 소비자 등급 하드웨어로 실행할 수 있으며, ggml 형식과 호환되는 여러 모델 제품군을 지원합니다.

Flowise 내에서 ChatLocalAI를 사용하려면 다음 단계를 따르세요:

1. ```bash
   git clone https://github.com/go-skynet/LocalAI
   ```
2. <pre class="language-bash"><code class="lang-bash"><strong>cd LocalAI
   </strong></code></pre>
3. ```bash
   # copy your models to models/
   cp your-model.bin models/
   ```

예를 들어:

[gpt4all.io](https://gpt4all.io/index.html)에서 모델 중 하나를 다운로드합니다

```bash
# Download gpt4all-j to models/
wget https://gpt4all.io/models/ggml-gpt4all-j.bin -O models/ggml-gpt4all-j
```

`/models` 폴더에서 다운로드한 모델을 볼 수 있어야 합니다:

<figure><img src="../../../.gitbook/assets/image (22) (1) (1).png" alt=""><figcaption></figcaption></figure>

지원되는 모델 목록은 [여기](https://localai.io/model-compatibility/index.html)를 참조하세요.

4. ```bash
   docker compose up -d --pull always
   ```
5. 이제 API는 localhost:8080에서 액세스할 수 있습니다

```bash
# Test API
curl http://localhost:8080/v1/models
# {"object":"list","data":[{"id":"ggml-gpt4all-j.bin","object":"model"}]}
```

## Flowise 설정

새 ChatLocalAI 구성 요소를 캔버스로 드래그 앤 드롭합니다:

<figure><img src="../../../.gitbook/assets/image (39).png" alt=""><figcaption></figcaption></figure>

필드를 채웁니다:

* **Base Path**: [http://localhost:8080/v1](http://localhost:8080/v1)과 같은 LocalAI의 기본 url
* **Model Name**: 사용할 모델입니다. LocalAI 디렉토리의 `/models` 폴더 내에 있어야 합니다. 예: `ggml-gpt4all-j.bin`

{% hint style="info" %}
Flowise와 LocalAI 모두를 Docker에서 실행 중인 경우 기본 경로를 [http://host.docker.internal:8080/v1](http://host.docker.internal:8080/v1)로 변경해야 할 수 있습니다. Linux 기반 시스템의 경우 host.docker.internal을 사용할 수 없으므로 기본 Docker 게이트웨이를 사용해야 합니다: [http://172.17.0.1:8080/v1](http://172.17.0.1:8080/v1)
{% endhint %}

완료되었습니다! 자세한 내용은 LocalAI [문서](https://localai.io/basics/getting_started/index.html)를 참조하세요.

Flowise에서 LocalAI를 사용하는 방법을 시청합니다

{% embed url="https://youtu.be/0B0oIs8NS9k" %}
