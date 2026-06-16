---
description: API에서 데이터를 로드합니다.
---

# API Document Loader

<figure><img src="../../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1).png" alt="" width="273"><figcaption><p>API Loader Node</p></figcaption></figure>

API Document Loader는 HTTP 요청을 사용하여 외부 API에서 데이터를 로드하고 처리하는 기능을 제공합니다. 이 모듈은 RESTful API 및 웹 서비스와의 원활한 통합을 가능하게 합니다.

이 모듈은 다음을 수행할 수 있는 다목적 API document loader를 제공합니다:
- HTTP GET 및 POST 요청 수행
- 사용자 정의 헤더 및 요청 본문 처리
- API 응답을 documents로 처리
- JSON 데이터 구조 지원
- 메타데이터 추출 사용자 정의
- text splitters를 사용한 응답 처리

## Inputs

### 필수 매개변수
- **URL**: 호출할 API 엔드포인트 URL
- **Method**: 사용할 HTTP 메소드 (GET 또는 POST)

### 선택사항 매개변수
- **Headers**: HTTP 헤더를 포함하는 JSON 객체
- **Body**: POST 요청 본문에 대한 JSON 객체
- **Text Splitter**: 추출된 콘텐츠를 처리하는 text splitter
- **Additional Metadata**: 추가 메타데이터가 포함된 JSON 객체
- **Omit Metadata Keys**: 생략할 메타데이터 키의 쉼표 구분 목록

## Outputs

- **Document**: 메타데이터 및 pageContent를 포함하는 document 객체의 배열
- **Text**: documents의 pageContent에서 연결된 문자열

## Features
- HTTP 메소드 지원 (GET/POST)
- 사용자 정의 헤더 구성
- 요청 본문 사용자 정의
- 응답 처리
- 오류 처리
- 메타데이터 사용자 정의
- Text splitting 기능

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

## Notes
- JSON 요청/응답 형식 지원
- HTTP 오류 응답 처리
- 자동으로 응답 데이터를 documents로 처리
- 콘텐츠 처리를 위해 text splitters와 결합될 수 있음
- 사용자 정의 메타데이터 추가 및 생략 지원
- 오류 응답은 적절히 처리되고 보고됨
