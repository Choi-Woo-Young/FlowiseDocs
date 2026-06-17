---
설명: BraveSearch API를 사용한 검색 결과 로드
---

# BraveSearch API

<figure><img src="../../../.gitbook/assets/image_bravesearch.png" alt="" width="271"><figcaption><p>BraveSearch API 노드</p></figcaption></figure>

BraveSearch는 개인정보 보호를 중심으로 하는 검색 엔진으로, 강력한 웹 검색 API를 제공합니다. 이 모듈은 BraveSearch의 검색 결과를 로드하고 Document로 처리할 수 있게 합니다.

이 모듈은 다음을 수행할 수 있는 정교한 검색 document loader를 제공합니다:

* BraveSearch API를 사용한 웹 검색 실행
* 검색 결과를 구조화된 Document로 변환
* 결과에서 Snippet 및 Metadata 추출
* Text Splitter로 결과 처리
* Metadata 추출 커스터마이징

## 입력

### 필수 파라미터

* **Query**: 실행할 검색 쿼리
* **Connect Credential**: BraveSearch API 자격증명

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* 개인정보 보호 중심 웹 검색
* 구조화된 결과 처리
* 자동 metadata 추출
* 결과 콘텐츠 분할
* 커스터마이즈 가능한 metadata 처리
* API 응답에 대한 오류 처리

## Document 구조

각 검색 결과는 다음을 포함하는 document로 변환됩니다:

* **pageContent**: 검색 결과의 snippet/콘텐츠
* **metadata**:
  * title: 웹페이지의 제목
  * link: 웹페이지의 URL
  * 지정된 추가 커스텀 metadata

## 참고사항

* 유효한 BraveSearch API 키 필요
* 결과에는 웹페이지 snippet 및 metadata 포함
* 콘텐츠 처리를 위해 text splitter와 결합 가능
* 커스텀 metadata 추가 및 생략 지원
* API rate limit 및 오류 처리
* 개인정보 보호 중심 검색 기능 유지
