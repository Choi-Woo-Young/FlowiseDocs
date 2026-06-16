---
description: LangChain Embedding Nodes
---

# Embeddings

***

embedding은 부동 소수점 숫자의 벡터(목록)입니다. 두 벡터 사이의 거리는 그들의 관련성을 측정합니다. 작은 거리는 높은 관련성을 시사하고 큰 거리는 낮은 관련성을 시사합니다.

Embeddings은 텍스트 데이터의 수치적 표현을 만드는 데 사용할 수 있습니다. 이 수치적 표현은 유사한 documents를 찾는 데 사용할 수 있기 때문에 유용합니다.

이들은 일반적으로 다음에 사용됩니다:

* Search (결과가 쿼리 문자열과의 관련성으로 순위가 지정되는 경우)
* Clustering (텍스트 문자열이 유사성별로 그룹화되는 경우)
* Recommendations (관련 텍스트 문자열이 있는 항목이 권장되는 경우)
* Anomaly detection (관련성이 거의 없는 이상값이 식별되는 경우)
* Diversity measurement (유사성 분포가 분석되는 경우)
* Classification (텍스트 문자열이 가장 유사한 레이블로 분류되는 경우)

### Embedding Nodes:

* [AWS Bedrock Embeddings](aws-bedrock-embeddings.md)
* [Azure OpenAI Embeddings](azure-openai-embeddings.md)
* [Cohere Embeddings](cohere-embeddings.md)
* [Google GenerativeAI Embeddings](googlegenerativeai-embeddings.md)
* [Google PaLM Embeddings](broken-reference)
* [Google VertexAI Embeddings](googlevertexai-embeddings.md)
* [HuggingFace Inference Embeddings](huggingface-inference-embeddings.md)
* [LocalAI Embeddings](localai-embeddings.md)
* [MistralAI Embeddings](mistralai-embeddings.md)
* [Ollama Embeddings](ollama-embeddings.md)
* [OpenAI Embeddings](openai-embeddings.md)
* [OpenAI Embeddings Custom](openai-embeddings-custom.md)
* [TogetherAI Embedding](togetherai-embedding.md)
* [VoyageAI Embeddings](voyageai-embeddings.md)
