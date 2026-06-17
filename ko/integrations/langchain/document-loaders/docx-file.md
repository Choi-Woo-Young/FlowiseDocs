---
설명: DOCX 파일에서 데이터 로드
---

# DOCX File

<figure><img src="../../../.gitbook/assets/image_docx.png" alt="" width="271"><figcaption><p>DOCX File 노드</p></figcaption></figure>

DOCX는 Microsoft Word에서 사용하는 문서 형식으로, 텍스트, 이미지, 표 등의 리치 콘텐츠를 포함할 수 있습니다. 이 모듈은 DOCX 파일을 로드하고 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 DOCX Document Loader를 제공합니다:

* DOCX 파일 로드 및 파싱
* 텍스트 콘텐츠 추출
* 표 데이터 추출
* 제목 및 단락 구조 보존
* Text Splitter로 콘텐츠 처리
* Metadata 추출 및 커스터마이징

## 입력

### 필수 파라미터

* **File Upload**: 로드할 DOCX 파일

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* DOCX 파일 파싱
* 텍스트 추출
* 표 처리
* 메타데이터 추출
* Text Splitter 지원
* 오류 처리

## 지원 기능

* 일반 텍스트
* 제목 및 단락
* 표 및 목록
* 이미지 캡션
* 헤더 및 푸터
* 메타데이터

## 참고사항

* 유효한 DOCX 파일 형식 필요
* 매우 큰 문서의 처리 시간 주의
* 암호로 보호된 파일은 지원 안 함
* 이미지는 URL로 변환되지 않음
* 복잡한 형식의 손실 가능성
