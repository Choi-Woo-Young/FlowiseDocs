---
설명: CSV 파일에서 데이터 로드
---

# CSV File

<figure><img src="../../../.gitbook/assets/image_csv.png" alt="" width="271"><figcaption><p>CSV File 노드</p></figcaption></figure>

CSV (Comma-Separated Values)는 표 형식의 데이터를 저장하는 널리 사용되는 파일 형식입니다. 이 모듈은 CSV 파일을 로드하고 구조화된 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 CSV Document Loader를 제공합니다:

* CSV 파일 로드 및 파싱
* 구분자 커스터마이징
* 열 선택 및 필터링
* 행 제한 설정
* Text Splitter로 콘텐츠 처리
* Metadata 추출 및 커스터마이징

## 입력

### 필수 파라미터

* **File Upload**: 로드할 CSV 파일

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Delimiter**: CSV 구분자 (기본값: ,)
* **Column Names**: 포함할 열 이름의 쉼표로 구분된 목록
* **Limit**: 처리할 최대 행 수
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* CSV 파일 파싱
* 열 선택
* 행 제한
* 커스텀 구분자 지원
* Metadata 커스터마이징
* 오류 처리

## 파일 형식

* CSV 파일 지원
* 다양한 구분자 지원 (쉼표, 탭, 세미콜론 등)
* 헤더 행 감지
* 인코딩 처리

## 참고사항

* 유효한 CSV 형식 필요
* 대용량 파일의 메모리 사용량 주의
* 파일 크기 제한 확인
* 인코딩 호환성 확인
* 특수 문자 및 따옴표 처리
