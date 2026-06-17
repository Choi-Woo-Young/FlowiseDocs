---
description: 웹 검색 결과에서 데이터를 로드하고 처리합니다.
---

# SerpApi For Web Search

<figure><img src="../../../.gitbook/assets/image (81).png" alt="" width="319"><figcaption><p>SerpApi For Web Search Node</p></figcaption></figure>

SerpApi For Web Search 로더를 사용하면 SerpApi 서비스를 사용하여 웹 검색 결과를 가져오고 처리할 수 있습니다. 이 로더는 검색 결과를 워크플로우에 쉽게 통합할 수 있는 구조화된 문서로 변환하므로 실시간 웹 검색 데이터가 필요한 애플리케이션에 이상적입니다.

## 기능
- 실시간 웹 검색 결과
- 텍스트 분할 기능
- 사용자 정의 가능한 메타데이터 처리
- 다양한 출력 형식
- API 키 인증
- 효율적인 문서 처리

## 입력

### 필수 매개변수
- **Connect Credential**: SerpApi API 키 자격증명
- **Query**: 실행할 검색 쿼리

### 선택사항 매개변수
- **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 텍스트 분할기
- **Additional Metadata**: 문서에 추가할 추가 메타데이터가 포함된 JSON 객체
- **Omit Metadata Keys**: 제외할 메타데이터 키의 쉼표 구분 목록
  - 형식: `key1, key2, key3.nestedKey1`
  - *를 사용하여 모든 기본 메타데이터를 제거하되 사용자 정의 메타데이터는 유지

## 출력

- **Document**: 다음을 포함하는 문서 객체의 배열:
  - metadata: 검색 결과 메타데이터
  - pageContent: 검색 결과 콘텐츠
- **Text**: 모든 검색 결과 콘텐츠의 연결된 문자열

## 문서 구조
각 문서에는 다음이 포함됩니다:
- **pageContent**: 검색 결과의 주요 콘텐츠
- **metadata**:
  - 기본 검색 결과 메타데이터
  - 사용자 정의 메타데이터 (지정된 경우)
  - 필터링된 메타데이터 (생략된 키 기반)

## 메타데이터 처리
메타데이터를 사용자 정의하는 두 가지 방법:
1. **Additional Metadata**
   - JSON을 통해 새로운 메타데이터 필드 추가
   - 기존 메타데이터와 병합됨
   - 사용자 정의 추적 또는 분류를 추가하는 데 유용합니다

2. **Omit Metadata Keys**
   - 원하지 않는 메타데이터 필드 제거
   - 제외할 키의 쉼표 구분 목록
   - 중첩된 키 제거 지원
   - *를 사용하여 모든 기본 메타데이터 제거

## 사용 팁
- 더 나은 결과를 위해 구체적인 검색 쿼리를 제공하세요
- 큰 검색 결과에 대해 텍스트 분할기를 사용하세요
- 필요에 맞게 메타데이터를 사용자 정의하세요
- 여러 쿼리를 만들 때 속도 제한을 고려하세요
- 크기에 따라 검색 결과를 적절히 처리하세요

## 참고 사항
- SerpApi API 키 필요
- API 속도 제한 준수
- 실시간 검색 결과
- 메모리 효율적인 처리
- API 요청에 대한 오류 처리
- 문서 및 텍스트 출력 형식 모두 지원

## 사용 예제
```typescript
// 검색 쿼리 예제
query: "artificial intelligence latest developments"

// 추가 메타데이터 예제
metadata: {
  "source": "serpapi",
  "category": "tech",
  "timestamp": "2024-03-21"
}

// 생략할 메타데이터 키 예제
omitMetadataKeys: "snippet, position, link"
```
