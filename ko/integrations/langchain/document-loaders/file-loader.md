---
설명: 다양한 파일 형식에서 데이터 로드
---

# File Loader

<figure><img src="../../../.gitbook/assets/image_file_loader.png" alt="" width="271"><figcaption><p>File Loader 노드</p></figcaption></figure>

File Loader는 다양한 파일 형식 (PDF, DOCX, TXT, JSON 등)을 자동으로 감지하고 적절한 loader를 사용하여 문서를 로드합니다. 이를 통해 여러 파일 형식을 하나의 노드에서 처리할 수 있습니다.

이 모듈은 다음을 수행할 수 있습니다:

* 다양한 파일 형식 자동 감지
* 파일 형식에 따른 최적의 loader 선택
* 일괄 파일 처리
* 통일된 Document 구조 생성
* Text Splitter와 통합
* Metadata 추출

## 입력

### 필수 파라미터

* **Files**: 로드할 파일 (여러 파일 지원)

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 지원 파일 형식

* PDF (.pdf)
* Word Documents (.docx, .doc)
* Text Files (.txt, .md)
* JSON (.json)
* CSV (.csv)
* EPUB (.epub)
* PowerPoint (.pptx)

## 기능

* 다중 파일 형식 지원
* 자동 형식 감지
* 일괄 처리
* Text Splitter 지원
* 오류 처리

## 참고사항

* 모든 파일 형식이 지원되지 않을 수 있음
* 파일 크기 제한 확인
* 지원 형식에 대해서는 별도의 loader 참조
* 성능 최적화를 위해 파일 수 제한
