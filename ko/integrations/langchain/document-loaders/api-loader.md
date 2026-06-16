---
description: API에서 데이터 로드
---

# API Document Loader

<figure><img src="../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1).png" alt="" width="273"><figcaption><p>API Loader Node</p></figcaption></figure>

API Document Loader는 HTTP 요청을 사용하여 외부 API에서 데이터를 로드하고 처리하기 위한 기능을 제공합니다. 이 모듈은 RESTful API 및 웹 서비스와의 완벽한 통합을 가능하게 합니다.

이 모듈은 다음과 같은 기능을 제공하는 다목적 API 문서 로더입니다:
- HTTP GET 및 POST 요청 수행
- 커스텀 헤더 및 요청 본문 처리
- API 응답을 문서로 처리
- JSON 데이터 구조 지원
- 메타데이터 추출 커스터마이징
- 텍스트 분할기로 응답 처리

## 입력

### 필수 매개변수
- **URL**: 호출할 API 엔드포인트 URL
- **Method**: 사용할 HTTP 메서드 (GET 또는 POST)

### 선택 매개변수
- **Headers**: HTTP 헤더를 포함하는 JSON 객체
- **Body**: POST 요청 본문을 위한 JSON 객체
- **Text Splitter**: 추출된 콘텐츠를 처리할 텍스트 분할기
- **Additional Metadata**: 추가 메타데이터를 포함한 JSON 객체
- **Omit Metadata Keys**: 생략할 메타데이터 키의 쉼표 구분 목록

## 출력

- **Document**: 메타데이터 및 pageContent를 포함하는 문서 객체 배열
- **Text**: 문서의 pageContent에서 연결된 문자열

## 기능
- HTTP 메서드 지원 (GET/POST)
- 커스텀 헤더 설정
- 요청 본문 커스터마이징
- 응답 처리
- 오류 처리
- 메타데이터 커스터마이징
- 텍스트 분할 기능

## 사용 예시

### GET 요청
```json
{
    "method": "GET",
    "url": "https://api.example.com/data",
    "headers": {
        "Authorization": "Bearer token123",
        "Accept": "application/json"
    }
}
```

### POST 요청
```json
{
    "method": "POST",
    "url": "https://api.example.com/data",
    "headers": {
        "Content-Type": "application/json",
        "Authorization": "Bearer token123"
    },
    "body": {
        "query": "example",
        "limit": 10
    }
}
```

## 주의사항
- JSON 요청/응답 형식 지원
- HTTP 오류 응답 처리
- 응답 데이터를 자동으로 문서로 처리
- 콘텐츠 처리를 위해 텍스트 분할기와 함께 사용 가능
- 커스텀 메타데이터 추가 및 생략 지원
- 오류 응답은 적절히 처리되고 보고됨
