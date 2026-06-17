---
설명: PDF 파일에서 데이터 로드
---

# PDF File

<figure><img src="../../../.gitbook/assets/image_pdf.png" alt="" width="271"><figcaption><p>PDF File 노드</p></figcaption></figure>

PDF (Portable Document Format)은 일반적으로 사용되는 문서 형식입니다. 이 모듈은 PDF 파일을 로드하고 텍스트 콘텐츠를 추출하여 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 PDF Document Loader를 제공합니다:

* PDF 파일 로드 및 파싱
* 페이지별 텍스트 추출
* 메타데이터 추출
* 페이지 번호 정보 유지
* Text Splitter와 통합
* 다양한 PDF 형식 지원

## 입력

### 필수 파라미터

* **File Upload**: 로드할 PDF 파일

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Page Range**: 로드할 페이지 범위 (예: 1-10)
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* PDF 파일 파싱
* 페이지별 추출
* 메타데이터 수집
* 페이지 번호 추적
* Text Splitter 지원
* 오류 처리

## 지원 PDF 종류

* 텍스트 기반 PDF
* 스캔된 PDF (OCR 지원 가능)
* 이미지 포함 PDF
* 다양한 인코딩

## 참고사항

* 텍스트 기반 PDF 권장 (스캔 이미지는 OCR 필요)
* 매우 큰 파일의 메모리 사용 주의
* 파일 크기 제한 확인
* 암호 보호 PDF는 지원 안 함
* 페이지 범위 설정으로 성능 최적화 가능
