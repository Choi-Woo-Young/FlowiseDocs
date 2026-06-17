---
설명: Google Drive 파일에서 데이터 로드
---

# Google Drive

<figure><img src="../../../.gitbook/assets/image_google_drive.png" alt="" width="271"><figcaption><p>Google Drive 노드</p></figcaption></figure>

Google Drive Document Loader를 사용하여 Google Drive의 파일을 로드하고 Document로 변환할 수 있습니다. 이를 통해 Google Docs, Google Sheets, 업로드된 파일 등을 처리할 수 있습니다.

이 모듈은 다음을 수행할 수 있는 정교한 Google Drive Document Loader를 제공합니다:

* Google Drive의 파일 로드
* 폴더 지정
* 파일 검색 및 필터링
* Google Docs 콘텐츠 추출
* Google Sheets 데이터 추출
* Text Splitter와 통합

## 입력

### 필수 파라미터

* **Folder ID**: Google Drive 폴더 ID
* **Connect Credential**: Google Drive API 자격증명

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **File Extensions**: 처리할 파일 확장명의 쉼표로 구분된 목록
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Google Drive 파일 로드
* 폴더 탐색
* 파일 검색
* Google Docs 추출
* Google Sheets 추출
* Text Splitter 지원

## 지원 파일 형식

* Google Docs
* Google Sheets
* PDF
* Microsoft Word
* Microsoft Excel
* Text Files

## 참고사항

* Google Drive API 자격증명 필요
* 폴더 공유 권한 필요
* API rate limit 적용
* 대용량 파일의 로드 시간 주의
* 특정 파일만 로드하려면 파일 ID 사용 가능
