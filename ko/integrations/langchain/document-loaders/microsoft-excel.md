---
설명: Microsoft Excel 파일에서 데이터 로드
---

# Microsoft Excel

<figure><img src="../../../.gitbook/assets/image_excel.png" alt="" width="271"><figcaption><p>Microsoft Excel 노드</p></figcaption></figure>

Microsoft Excel Document Loader를 사용하여 Excel 파일의 데이터를 로드하고 Document로 변환할 수 있습니다. .xlsx 및 .xls 형식을 지원합니다.

이 모듈은 다음을 수행할 수 있는 정교한 Excel Document Loader를 제공합니다:

* Excel 파일 로드 및 파싱
* 특정 Sheet 선택
* 행/열 범위 지정
* 헤더 행 처리
* Text Splitter와 통합
* 메타데이터 추출

## 입력

### 필수 파라미터

* **File Upload**: 로드할 Excel 파일

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

* Excel 파일 파싱
* 특정 Sheet 선택
* 행/열 필터링
* 메타데이터 추출
* Text Splitter 지원
* 오류 처리

## 지원 형식

* .xlsx (Excel 2007+)
* .xls (Excel 97-2003)
* 다양한 데이터 유형
* 공식 (값으로 변환)

## 참고사항

* 유효한 Excel 파일 형식 필수
* 매우 큰 파일의 메모리 사용 주의
* 파일 크기 제한 확인
* 공식은 계산된 값으로 추출
* 암호 보호 파일은 지원 안 함
