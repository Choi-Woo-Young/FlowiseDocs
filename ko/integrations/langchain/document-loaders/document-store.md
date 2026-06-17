---
설명: Document Store에서 데이터 로드
---

# Document Store

<figure><img src="../../../.gitbook/assets/image_document_store.png" alt="" width="271"><figcaption><p>Document Store 노드</p></figcaption></figure>

Document Store는 Flowise 내에 저장된 문서들을 로드하는 loader입니다. 이전에 업로드되거나 생성된 문서들을 Flowise의 Document Store에서 검색하고 활용할 수 있습니다.

이 모듈은 다음을 수행할 수 있습니다:

* Document Store에 저장된 모든 문서 로드
* Store ID 또는 Store 이름으로 문서 검색
* 문서 메타데이터 활용
* 저장된 Document 객체 직접 활용
* Text Splitter와 통합

## 입력

### 필수 파라미터

* **Document Store**: 로드할 Document Store 선택

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Document Store에 저장된 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Document Store 통합
* 저장된 문서 검색
* Metadata 보존
* Text Splitter 지원
* 오류 처리

## 참고사항

* Document Store에 먼저 문서 저장 필수
* Store ID 또는 Store 이름 필요
* Metadata는 원본 문서에서 유지
* 자주 사용하는 Document Set은 Document Store에 저장 권장
* 성능 최적화를 위해 필요한 문서만 로드
