---
description: 실시간 검색 결과에서 데이터를 로드합니다.
---

# SearchApi For Web Search

<figure><img src="../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="322"><figcaption><p>SearchApi For Web Search</p></figcaption></figure>

SearchApi For Web Search 로더는 SearchApi 서비스를 사용하여 여러 검색 엔진의 실시간 검색 결과에 액세스를 제공합니다. 이 로더를 사용하면 워크플로우에서 사용할 수 있는 문서로 검색 결과를 가져오고, 처리하고, 구조화할 수 있습니다.

## 기능

* 여러 검색 엔진의 실시간 검색 결과
* 사용자 정의 가능한 검색 매개변수
* 텍스트 분할 기능
* 유연한 메타데이터 처리
* 다양한 출력 형식
* API 키 인증

## 입력

### 필수 매개변수

* **Connect Credential**: SearchApi API 키 자격증명
* 다음 중 최소 하나:
  * **Query**: 검색 쿼리 문자열
  * **Custom Parameters**: 검색 매개변수가 포함된 JSON 객체

### 선택사항 매개변수

* **Query**: 실행할 검색 쿼리 (사용자 정의 매개변수를 사용하지 않는 경우)
* **Custom Parameters**: 추가 검색 매개변수가 포함된 JSON 객체
  * [SearchApi 설명서](https://www.searchapi.io/docs/google)의 모든 매개변수를 지원합니다
  * 기본 설정을 재정의할 수 있습니다
  * 엔진별 구성을 허용합니다
* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 텍스트 분할기
* **Additional Metadata**: 문서에 추가할 추가 메타데이터가 포함된 JSON 객체
* **Omit Metadata Keys**: 제외할 메타데이터 키의 쉼표 구분 목록
  * 형식: `key1, key2, key3.nestedKey1`
  * \*를 사용하여 모든 기본 메타데이터 제거

## 출력

* **Document**: 다음을 포함하는 문서 객체의 배열:
  * metadata: 검색 결과 메타데이터
  * pageContent: 검색 결과 콘텐츠
* **Text**: 모든 검색 결과 콘텐츠의 연결된 문자열

## 문서 구조

각 문서에는 다음이 포함됩니다:

* **pageContent**: 검색 결과의 주요 콘텐츠
* **metadata**:
  * 기본 검색 결과 메타데이터
  * 사용자 정의 메타데이터 (지정된 경우)
  * 필터링된 메타데이터 (생략된 키 기반)

## 메타데이터 처리

메타데이터를 사용자 정의하는 두 가지 방법:

1. **Additional Metadata**
   * JSON을 통해 새로운 메타데이터 필드 추가
   * 기존 메타데이터와 병합됨
   * 사용자 정의 추적 또는 분류를 추가하는 데 유용합니다
2. **Omit Metadata Keys**
   * 원하지 않는 메타데이터 필드 제거
   * 제외할 키의 쉼표 구분 목록
   * 중첩된 키 제거 지원
   * \*를 사용하여 모든 기본 메타데이터 제거

## 사용 팁

* 더 나은 결과를 위해 구체적인 검색 쿼리를 제공하세요
* 고급 검색 구성을 위해 사용자 정의 매개변수를 사용하세요
* 큰 검색 결과에 대해 텍스트 분할기 사용을 고려하세요
* 관련 정보를 유지하기 위해 메타데이터를 관리하세요
* 적절한 쿼리 간격을 통해 속도 제한을 처리하세요

## 참고 사항

* SearchApi API 키 필요
* API 속도 제한 준수
* 여러 검색 엔진 지원
* 실시간 검색 결과
* 메모리 효율적인 처리
* API 요청에 대한 오류 처리
