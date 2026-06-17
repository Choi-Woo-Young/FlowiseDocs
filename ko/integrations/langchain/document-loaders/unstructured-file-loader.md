---
description: Unstructured.io를 사용하여 파일 경로에서 데이터를 로드합니다.
---

# Unstructured File Loader

<figure><img src="../../../.gitbook/assets/image (90).png" alt="" width="332"><figcaption><p>Unstructured File Loader Node</p></figcaption></figure>

Unstructured File Loader는 [Unstructured.io](https://unstructured.io)를 사용하여 다양한 파일 형식에서 콘텐츠를 추출하고 처리합니다. OCR, 청킹 및 메타데이터 추출을 위한 구성 가능한 옵션을 사용하여 고급 문서 구문 분석 기능을 제공합니다.

## 기능
- 고급 문서 구문 분석
- 다양한 언어 옵션이 있는 OCR 지원
- 유연한 청킹 전략
- 테이블 구조 추론
- 좌표 추출
- 페이지 나누기 처리
- XML 태그 처리
- 사용자 정의 가능한 모델 선택
- 메타데이터 추출

## 구성

### API 설정
- 기본 API URL: `https://api.unstructuredapp.io/general/v0/general`
- Unstructured.io의 API 키 필요
- 환경 변수를 통해 구성 가능:
  - `UNSTRUCTURED_API_URL`
  - `UNSTRUCTURED_API_KEY`

### 처리 전략
- **Strategy**: 기본값은 "hi_res"
  - 옵션에는 다양한 문서 유형에 대한 다양한 처리 전략이 포함됩니다
- **Chunking Strategy**:
  - None (기본값)
  - by_title (제목 기반 텍스트 청킹)

## 매개변수

### 필수 매개변수
- **File**: 처리할 문서
- **API Key**: Unstructured.io API 키 (환경을 통해 설정하지 않은 경우)

### 선택사항 매개변수

#### OCR 옵션
- **OCR Languages**: OCR 처리용 언어 배열
- **Encoding**: 문서 인코딩 지정

#### 처리 옵션
- **Coordinates**: 요소 좌표 추출 (true/false)
- **PDF Table Structure**: PDF의 테이블 구조 추론 (true/false)
- **XML Tags**: 출력에서 XML 태그 유지 (true/false)
- **Skip Table Types**: 추론을 건너뛸 테이블 유형 배열
- **Hi-Res Model**: 고해상도 모델 이름 지정
- **Include Page Breaks**: 페이지 나누기 정보 포함 (true/false)

#### 텍스트 청킹 옵션
- **Multi-page Sections**: 페이지 간 섹션 처리 (true/false)
- **Combine Under N Chars**: 지정된 문자 수 이하의 요소 결합
- **New After N Chars**: 지정된 문자 수 이후 새 요소 생성
- **Max Characters**: 요소당 최대 문자 수

## 출력 구조

### 문서 형식
처리된 각 요소는 다음을 포함하는 문서가 됩니다:
- **pageContent**: 추출된 텍스트 콘텐츠
- **metadata**: 
  - category: 요소 유형
  - 처리에서 나온 추가 메타데이터

### 요소 유형
로더는 다양한 요소 유형을 식별할 수 있습니다:
- 텍스트 블록
- 테이블
- 목록
- 헤더
- 푸터
- 페이지 나누기 (활성화된 경우)
- 기타 구조적 요소

## 사용 예제

### 기본 구성
```typescript
{
  "apiKey": "your-api-key",
  "strategy": "hi_res",
  "ocrLanguages": ["eng"]
}
```

### 고급 처리
```typescript
{
  "apiKey": "your-api-key",
  "strategy": "hi_res",
  "coordinates": true,
  "pdfInferTableStructure": true,
  "chunkingStrategy": "by_title",
  "multiPageSections": true,
  "combineUnderNChars": 100,
  "maxCharacters": 4000
}
```

## 참고 사항
- 각 파일 처리 요청에 대해 API 호출이 수행됩니다
- 응답에는 텍스트 및 메타데이터가 있는 구조화된 요소가 포함됩니다
- 유효한 텍스트 콘텐츠를 보장하도록 요소를 필터링합니다
- 버퍼 기반 처리 지원
- API 응답에 대한 오류 처리
- 자동 메타데이터 분류
- 메모리 효율적인 처리

## 모범 사례
1. 사용 사례에 맞는 청킹 매개변수를 설정합니다
2. 영어가 아닌 문서의 OCR 언어 설정을 고려합니다
3. 테이블이 있는 문서에 대해 테이블 구조 추론을 활성화합니다
4. 공간 정보가 중요한 경우 좌표를 사용합니다
5. 다운스트림 처리 요구에 따라 문자 제한을 구성합니다
6. API 사용량 및 응답 시간을 모니터링합니다
7. 워크플로우에서 잠재적 API 오류를 처리합니다

{% hint style="info" %}
이 섹션은 진행 중입니다. 이 섹션을 완성하는 데 도움을 주시면 감사하겠습니다. 시작하려면 [기여 가이드](broken-reference)를 확인하세요.
{% endhint %}
