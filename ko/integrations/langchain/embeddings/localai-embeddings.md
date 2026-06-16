# LocalAI Embeddings

## LocalAI Setup

[**LocalAI** ](https://github.com/go-skynet/LocalAI)는 로컬 inferencing을 위해 OpenAI API 사양과 호환되는 drop-in replacement REST API입니다. 이를 통해 consumer grade hardware에서 로컬로 또는 on-prem에서 LLMs 등을 실행할 수 있으며, ggml 형식과 호환되는 여러 모델 family를 지원합니다.

Flowise에서 LocalAI Embeddings를 사용하려면 아래 단계를 따르세요:

1. ```bash
   git clone https://github.com/go-skynet/LocalAI
   ```
2. <pre class="language-bash"><code class="lang-bash"><strong>cd LocalAI
   </strong></code></pre>
3. LocalAI는 모델을 다운로드/설치하기 위한 [API endpoint](https://localai.io/api-endpoints/index.html#applying-a-model---modelsapply)를 제공합니다. 이 예제에서는 BERT Embeddings 모델을 사용할 것입니다:

<figure><img src="../../../.gitbook/assets/image (27) (1).png" alt=""><figcaption></figcaption></figure>

4. `/models` 폴더에서 다운로드된 모델을 확인할 수 있어야 합니다:

<figure><img src="../../../.gitbook/assets/image (23) (1) (2).png" alt=""><figcaption></figcaption></figure>

5. 이제 embeddings를 테스트할 수 있습니다:

```bash
curl http://localhost:8080/v1/embeddings -H "Content-Type: application/json" -d '{
    "input": "Test",
    "model": "text-embedding-ada-002"
  }'
```

6. 응답은 다음과 같이 보여야 합니다:

<figure><img src="../../../.gitbook/assets/image (29).png" alt="" width="375"><figcaption></figcaption></figure>

## Flowise Setup

canvas에 새 LocalAIEmbeddings component를 드래그 앤 드롭:

<figure><img src="../../../.gitbook/assets/image (21) (1) (2).png" alt=""><figcaption></figcaption></figure>

필드 작성:

* **Base Path**: LocalAI의 base url 예: [http://localhost:8080/v1](http://localhost:8080/v1)
* **Model Name**: 사용하려는 모델입니다. LocalAI 디렉토리의 `/models` 폴더 내에 있어야 합니다. 예: `text-embedding-ada-002`

완료되었습니다! 자세한 정보는 LocalAI [문서](https://localai.io/models/index.html#embeddings-bert)를 참조하세요.
