# PDF Document Loader

PDF (Portable Document Format)는 소프트웨어 플랫폼 전체에서 문서를 일관되게 제시하기 위해 Adobe에서 개발한 파일 형식입니다. 이 모듈은 pdf.js를 사용하여 PDF 파일을 로드하고 처리하는 기능을 제공합니다.

이 모듈은 다음을 수행할 수 있는 정교한 PDF document loader를 제공합니다:
- 단일 또는 여러 PDF 파일 로드
- 페이지 또는 파일별 문서 분할
- base64 인코딩된 파일 지원
- 파일 저장소 통합 처리
- text splitters를 사용한 콘텐츠 처리
- 레거시 PDF 버전 지원
- 메타데이터 추출 사용자 정의

## Inputs

### 필수 매개변수
- **PDF File**: 처리할 PDF 파일 (.pdf 확장자)
- **Usage**: 다음 중 선택:
  - 페이지당 하나의 document
  - 파일당 하나의 document

### 선택사항 매개변수
- **Text Splitter**: 추출된 콘텐츠를 처리하는 text splitter
- **Use Legacy Build**: 레거시 PDF.js build를 사용할지 여부
- **Additional Metadata**: 추가 메타데이터가 포함된 JSON 객체
- **Omit Metadata Keys**: 생략할 메타데이터 키의 쉼표 구분 목록

## Outputs

- **Document**: 메타데이터 및 pageContent를 포함하는 document 객체의 배열
- **Text**: documents의 pageContent에서 연결된 문자열

## Features
- 다중 파일 지원
- 페이지 수준 분할
- 레거시 버전 지원
- 텍스트 추출
- 메타데이터 처리
- 오류 처리
- 메모리 효율적인 처리

## Processing Modes

### Per Page Mode
- 각 페이지가 document가 됨
- 페이지 번호 보존
- 개별 페이지 메타데이터
- 세분화된 콘텐츠 액세스

### Per File Mode
- 전체 PDF가 하나의 document
- 결합된 콘텐츠
- 단일 메타데이터 세트
- 메모리 효율적

## Document Structure
각 document 포함:
- **pageContent**: 추출된 텍스트 콘텐츠
- **metadata**:
  - source: 원본 파일 경로
  - pdf: PDF 특정 메타데이터
  - page: 페이지 번호 (per-page mode에서)
  - 추가 사용자 정의 메타데이터

## File Handling

### Local Files
- 직접 파일 로드
- Base64 인코딩된 콘텐츠
- 다중 파일 지원

### Storage Integration
- 파일 저장소 시스템 지원
- 조직 기반 저장소
- Chatflow 기반 저장소

## Notes
- text 추출을 위해 pdf.js 사용
- 레거시 버전 지원
- 메모리 효율적인 처리
- 잘못된 파일에 대한 오류 처리
- 대용량 PDF 지원
- 유연한 출력 형식
- 메타데이터 사용자 정의
- 텍스트 인코딩 처리
