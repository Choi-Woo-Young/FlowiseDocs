# BraveSearch API Document Loader

BraveSearch는 웹 검색을 위한 강력한 API를 제공하는 프라이버시 중심의 검색 엔진입니다. 이 모듈은 BraveSearch의 검색 결과를 로드하고 documents로 처리할 수 있게 합니다.

이 모듈은 다음을 수행할 수 있는 정교한 search document loader를 제공합니다:
- BraveSearch API를 사용하여 웹 검색 실행
- 검색 결과를 구조화된 documents로 변환
- 결과에서 snippets 및 메타데이터 추출
- text splitters를 사용한 결과 처리
- 메타데이터 추출 사용자 정의

## Inputs

### 필수 매개변수
- **Query**: 실행할 검색 쿼리
- **Connect Credential**: BraveSearch API 자격증명

### 선택사항 매개변수
- **Text Splitter**: 추출된 콘텐츠를 처리하는 text splitter
- **Additional Metadata**: 추가 메타데이터가 포함된 JSON 객체
- **Omit Metadata Keys**: 생략할 메타데이터 키의 쉼표 구분 목록

## Outputs

- **Document**: 메타데이터 및 pageContent를 포함하는 document 객체의 배열
- **Text**: documents의 pageContent에서 연결된 문자열

## Features
- 프라이버시 중심의 웹 검색
- 구조화된 결과 처리
- 자동 메타데이터 추출
- 결과 콘텐츠 분할
- 사용자 정의 가능한 메타데이터 처리
- API 응답에 대한 오류 처리

## Document Structure
각 검색 결과는 다음과 같은 document로 변환됩니다:
- **pageContent**: 검색 결과의 snippet/콘텐츠
- **metadata**:
  - title: 웹페이지의 제목
  - link: 웹페이지의 URL
  - 지정된 추가 사용자 정의 메타데이터

## Notes
- 유효한 BraveSearch API 키 필요
- 결과에는 웹페이지 snippets 및 메타데이터 포함
- 콘텐츠 처리를 위해 text splitters와 결합될 수 있음
- 사용자 정의 메타데이터 추가 및 생략 지원
- API 속도 제한 및 오류 처리
- 프라이버시 중심의 검색 기능 유지
