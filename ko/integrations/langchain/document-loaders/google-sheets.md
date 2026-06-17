---
설명: Google Sheets 데이터에서 데이터 로드
---

# Google Sheets

<figure><img src="../../../.gitbook/assets/image_google_sheets.png" alt="" width="271"><figcaption><p>Google Sheets 노드</p></figcaption></figure>

Google Sheets Document Loader를 사용하여 Google Sheets의 데이터를 로드하고 Document로 변환할 수 있습니다. 이를 통해 스프레드시트 데이터를 구조화된 Document로 변환할 수 있습니다.

이 모듈은 다음을 수행할 수 있는 정교한 Google Sheets Document Loader를 제공합니다:

* Google Sheets 데이터 로드
* 특정 Sheet 선택
* 행/열 범위 지정
* 헤더 행 처리
* Text Splitter와 통합
* 메타데이터 추출

## 입력

### 필수 파라미터

* **Spreadsheet ID**: Google Sheet의 Spreadsheet ID
* **Connect Credential**: Google Sheets API 자격증명

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Sheet Name**: 로드할 Sheet 이름
* **Row Limit**: 처리할 최대 행 수
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Google Sheets 데이터 로드
* 특정 Sheet 선택
* 행/열 필터링
* 메타데이터 추출
* Text Splitter 지원
* 오류 처리

## 데이터 형식

* 행 기반 처리 (각 행이 하나의 Document)
* 열 기반 메타데이터
* 유형 자동 감지
* 빈 셀 처리

## 참고사항

* Google Sheets API 자격증명 필요
* Spreadsheet ID는 공유 권한 필요
* API rate limit 적용
* 대규모 시트의 로드 시간 주의
* 공개 Sheet도 기술적으로 접근 가능
