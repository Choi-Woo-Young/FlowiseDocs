---
description: 실시간 검색 결과에서 데이터를 로드합니다.
---

# SearchApi For Web Search

<figure><img src="../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="322"><figcaption><p>SearchApi For Web Search</p></figcaption></figure>

SearchApi For Web Search loader는 SearchApi 서비스를 사용하여 여러 검색 엔진의 실시간 검색 결과에 대한 액세스를 제공합니다. 이 loader를 통해 검색 결과를 가져오고, 처리하고, workflow에서 사용할 수 있는 documents로 구조화할 수 있습니다.

## Features

* 여러 검색 엔진의 실시간 검색 결과
* 사용자 정의 가능한 검색 매개변수
* Text splitting 기능
* 유연한 메타데이터 처리
* 다중 출력 형식
* API key 인증

## Inputs

### 필수 매개변수

* **Connect Credential**: SearchApi API key 자격증명
* 다음 중 최소 하나:
  * **Query**: 검색 쿼리 문자열
  * **Custom Parameters**: 검색 매개변수를 포함하는 JSON 객체

### 선택사항 매개변수

* **Query**: 실행할 검색 쿼리 (custom parameters를 사용하지 않는 경우)
* **Custom Parameters**: 추가 검색 매개변수를 포함하는 JSON 객체
  * [SearchApi 문서](https://www.searchapi.io/docs/google)의 모든 매개변수 지원
  * 기본 설정을 override할 수 있음
  * engine 특정 구성 허용
* **Text Splitter**: 추출된 콘텐츠를 처리하는 text splitter
* **Additional Metadata**: documents에 추가할 추가 메타데이터가 포함된 JSON 객체
* **Omit Metadata Keys**: 제외할 메타데이터 키의 쉼표 구분 목록
  * 형식: `key1, key2, key3.nestedKey1`
  * 모든 기본 메타데이터를 제거하려면 \*를 사용

## Outputs

* **Document**: 다음을 포함하는 document 객체의 배열:
  * metadata: 검색 결과 메타데이터
  * pageContent: 검색 결과 콘텐츠
* **Text**: 모든 검색 결과의 콘텐츠의 연결된 문자열

## Document Structure

각 document 포함:

* **pageContent**: 검색 결과의 주요 콘텐츠
* **metadata**:
  * 기본 검색 결과 메타데이터
  * 사용자 정의 메타데이터 (지정된 경우)
  * 필터링된 메타데이터 (omitted keys 기반)

## Metadata Handling

메타데이터를 사용자 정의하는 두 가지 방법:

1. **Additional Metadata**
   * JSON을 통해 새 메타데이터 필드 추가
   * 기존 메타데이터와 병합됨
   * 사용자 정의 tracking 또는 categorization 추가에 유용
2. **Omit Metadata Keys**
   * 원하지 않는 메타데이터 필드 제거
   * 제외할 키의 쉼표 구분 목록
   * 중첩 key 제거 지원
   * 모든 기본 메타데이터를 제거하려면 \*를 사용

## Usage Tips

* 더 나은 결과를 위해 특정 검색 쿼리 제공
* 고급 검색 구성을 위해 custom parameters 사용
* 큰 검색 결과에 대해 text splitters 사용 고려
* 관련 정보를 유지하기 위해 메타데이터 관리
* 적절한 쿼리 간격을 통해 속도 제한 처리

## Notes

* SearchApi API key 필요
* API 속도 제한 준수
* 여러 검색 엔진 지원
* 실시간 검색 결과
* 메모리 효율적인 처리
* API 요청에 대한 오류 처리
