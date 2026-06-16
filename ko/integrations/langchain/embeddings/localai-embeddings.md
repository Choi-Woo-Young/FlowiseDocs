# LocalAI Embeddings

## LocalAI 설정

[**LocalAI**](https://github.com/go-skynet/LocalAI)는 로컬 추론을 위한 OpenAI API 사양과 호환되는 드롭인 리플레이스먼트 REST API입니다. 소비자 급 하드웨어에서 LLM(그뿐만 아니라)을 로컬 또는 온프레미스로 실행할 수 있으며, ggml 형식과 호환되는 여러 모델 제품군을 지원합니다.

Flowise 내에서 LocalAI Embeddings를 사용하려면 아래 단계를 따르세요.

1. ```bash
   git clone https://github.com/go-skynet/LocalAI
   ```
2. <pre class="language-bash"><code class="lang-bash"><strong>cd LocalAI
   </strong></code></pre>
3. LocalAI는 모델을 다운로드/설치하기 위한 [API 엔드포인트](https://localai.io/api-endpoints/index.html#applying-a-model---modelsapply)를 제공합니다. 이 예에서는 BERT Embeddings 모델을 사용하겠습니다.

<figure><img src="../../../.gitbook/assets/image (27) (1).png" alt=""><figcaption></figcaption></figure>

4. `/models` 폴더에서 다운로드된 모델을 확인할 수 있습니다.

<figure><img src="../../../.gitbook/assets/image (23) (1) (2).png" alt=""><figcaption></figcaption></figure>

5. 이제 임베딩을 테스트할 수 있습니다.

```bash
curl http://localhost:8080/v1/embeddings -H "Content-Type: application/json" -d ‘{
    "input": "Test",
    "model": "text-embedding-ada-002"
  }’
```

6. 응답은 다음과 같이 표시되어야 합니다.

<figure><img src="../../../.gitbook/assets/image (29).png" alt="" width="375"><figcaption></figcaption></figure>

## Flowise 설정

Canvas에 새 LocalAIEmbeddings 컴포넌트를 드래그하여 놓으세요.

<figure><img src="../../../.gitbook/assets/image (21) (1) (2).png" alt=""><figcaption></figcaption></figure>

필드를 채우세요.

* **Base Path**: LocalAI의 기본 URL 예: [http://localhost:8080/v1](http://localhost:8080/v1)
* **Model Name**: 사용하려는 모델. LocalAI 디렉토리의 `/models` 폴더 내에 있어야 합니다. 예: `text-embedding-ada-002`

완료되었습니다. 자세한 내용은 LocalAI [문서](https://localai.io/models/index.html#embeddings-bert)를 참조하세요.
