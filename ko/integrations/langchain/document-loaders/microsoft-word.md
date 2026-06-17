---
설명: Microsoft Word 파일에서 데이터 로드
---

# Microsoft Word

<figure><img src="../../../.gitbook/assets/image_word.png" alt="" width="271"><figcaption><p>Microsoft Word 노드</p></figcaption></figure>

Microsoft Word Document Loader (DOCX 파일)를 사용하여 Word 문서의 콘텐츠를 로드하고 Document로 변환할 수 있습니다.

이 모듈은 다음을 수행할 수 있는 정교한 Word Document Loader를 제공합니다:

* Word 문서 로드 및 파싱
* 텍스트 콘텐츠 추출
* 표 및 목록 처리
* 제목 및 단락 구조 보존
* Text Splitter와 통합
* 메타데이터 추출

## 입력

### 필수 파라미터

* **File Upload**: 로드할 Word 파일 (.docx)

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Word 파일 파싱
* 텍스트 추출
* 표 처리
* 메타데이터 추출
* Text Splitter 지원
* 오류 처리

## 지원 기능

* 일반 텍스트
* 제목 및 단락
* 표 및 목록
* 번호 목록
* 들여쓰기
* 메타데이터

## 참고사항

* .docx 형식만 지원 (.doc은 미지원)
* 이미지는 추출되지 않음
* 매우 큰 문서의 처리 시간 주의
* 암호 보호 파일은 지원 안 함
* 형식 손실은 최소화됨
