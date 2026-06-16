# RAG

대규모 언어 모델(LLM)은 특정 콘텐츠를 기반으로 정확한 답변을 제공할 수 있는 고급 Q&A 챗봇을 만들 수 있는 잠재력을 열어주었습니다. 이러한 시스템은 검색-증강 생성(RAG)이라는 방법에 의존하며, 이는 관련 출처 자료에 기반한 응답을 제공함으로써 응답을 향상시킵니다.

이 튜토리얼에서는 주어진 문서 소스에서 질문을 추출하고 답변할 수 있는 기본 Q&A 애플리케이션을 만드는 방법을 배우게 됩니다.

이 프로세스는 2가지 하위 프로세스로 나눌 수 있습니다:

* 인덱싱
* 검색

## 인덱싱

[Document Stores](../using-flowise/document-stores.md)는 전체 인덱싱 파이프라인(다양한 소스에서 데이터 검색, 청킹 전략, 벡터 데이터베이스에 업서트, 업데이트된 데이터와 동기화)을 지원하기 위해 설계되었습니다.

우리는 Pdf, Word, Google Drive와 같은 파일부터 Playwright, Firecrawl, Apify 및 기타 웹 스크래퍼에 이르기까지 광범위한 문서 로더를 지원합니다. 사용자 정의 문서 로더를 만들 수도 있습니다.

<figure><img src="../.gitbook/assets/image (293).png" alt="" width="563"><figcaption></figcaption></figure>

## 검색

사용자의 입력에 따라 관련된 문서 청크가 벡터 데이터베이스에서 가져와집니다. LLM은 검색된 컨텍스트를 사용하여 응답을 생성합니다.

1. [Agent](../using-flowise/agentflowv2.md#id-3.-agent-node) 노드를 드래그 앤 드롭하고 사용할 모델을 구성합니다.

<figure><img src="../.gitbook/assets/image (290).png" alt="" width="391"><figcaption></figcaption></figure>

2. 새로운 Knowledge(Document Store)를 추가하고 콘텐츠가 무엇에 관한 것인지 정의합니다. 이는 LLM이 언제, 어떻게 관련 정보를 검색할지 이해하는 데 도움이 됩니다. 자동 생성 버튼을 사용하여 이 프로세스에 도움을 받을 수도 있습니다.

{% hint style="success" %}
업서트된 문서 저장소만 사용할 수 있습니다.
{% endhint %}

<figure><img src="../.gitbook/assets/image (288).png" alt="" width="482"><figcaption></figcaption></figure>

3. (선택 사항) 데이터가 이미 문서 저장소 인덱싱 파이프라인을 거치지 않고 벡터 데이터베이스에 저장된 경우 벡터 데이터베이스와 임베딩 모델에 직접 연결할 수도 있습니다.

<figure><img src="../.gitbook/assets/image (289).png" alt="" width="388"><figcaption></figcaption></figure>

4. 시스템 프롬프트를 추가하거나 **Generate** 버튼을 사용하여 도움을 받으세요. 더 효과적이고 최적화된 프롬프트를 작성하는 데 도움이 되므로 사용을 권장합니다.

<figure><img src="../.gitbook/assets/image (294).png" alt="" width="482"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (292).png" alt="" width="563"><figcaption></figcaption></figure>

5. 이제 RAG 에이전트를 사용할 준비가 되었습니다!

## 리소스

{% embed url="https://youtu.be/KHc0ClOIv0A?si=mEZJydM8bT2imKJY" %}
