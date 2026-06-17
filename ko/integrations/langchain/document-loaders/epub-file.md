---
설명: EPUB 파일에서 데이터 로드
---

# EPUB File

<figure><img src="../../../.gitbook/assets/image_epub.png" alt="" width="271"><figcaption><p>EPUB File 노드</p></figcaption></figure>

EPUB는 전자책 표준 형식으로, 구조화된 XML 기반 문서를 지원합니다. 이 모듈은 EPUB 파일을 로드하고 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 EPUB Document Loader를 제공합니다:

* EPUB 파일 로드 및 파싱
* 책의 장 및 섹션 추출
* 텍스트 콘텐츠 추출
* 메타데이터 (제목, 저자 등) 추출
* Text Splitter로 콘텐츠 처리
* Metadata 커스터마이징

## 입력

### 필수 파라미터

* **File Upload**: 로드할 EPUB 파일

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* EPUB 파일 파싱
* 장 및 섹션 추출
* 메타데이터 추출
* Text Splitter 지원
* 오류 처리

## 지원 기능

* EPUB 2.0 및 3.0 지원
* 메타데이터 추출
* 목차 구조 이해
* HTML 콘텐츠 파싱
* 다양한 인코딩 지원

## 참고사항

* 유효한 EPUB 파일 형식 필요
* 복잡한 레이아웃은 단순화될 수 있음
* 이미지는 URL로 변환되지 않음
* DRM 보호 파일은 지원 안 함
* 문자 인코딩 호환성 확인
