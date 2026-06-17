---
설명: JSON 파일에서 데이터 로드
---

# JSON File

<figure><img src="../../../.gitbook/assets/image_json.png" alt="" width="271"><figcaption><p>JSON File 노드</p></figcaption></figure>

JSON (JavaScript Object Notation)은 데이터 교환을 위한 가벼운 형식입니다. 이 모듈은 JSON 파일을 로드하고 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 JSON Document Loader를 제공합니다:

* JSON 파일 로드 및 파싱
* 중첩된 JSON 구조 처리
* JSONPath를 사용한 필터링
* 배열 항목 개별 처리
* Text Splitter와 통합
* 메타데이터 추출

## 입력

### 필수 파라미터

* **File Upload**: 로드할 JSON 파일

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **JSONPath**: 특정 데이터 경로를 지정하는 JSONPath 식
* **Array Root**: 배열인 경우 배열의 경로
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* JSON 파일 파싱
* 중첩된 구조 처리
* JSONPath 필터링
* 배열 처리
* 메타데이터 추출
* Text Splitter 지원

## 지원 구조

* 단순 Object
* 배열 (Array)
* 중첩된 구조
* 다양한 데이터 유형 (문자열, 숫자, 불린 등)

## 참고사항

* 유효한 JSON 형식 필수
* 매우 큰 파일의 메모리 사용 주의
* JSONPath 문법 확인
* 복잡한 구조는 사전 전처리 권장
* 특수 문자 인코딩 확인
