---
설명: JSON Lines 파일에서 데이터 로드
---

# JSON Lines

<figure><img src="../../../.gitbook/assets/image_jsonlines.png" alt="" width="271"><figcaption><p>JSON Lines 노드</p></figcaption></figure>

JSON Lines (JSONL)은 개행으로 분리된 JSON 객체들의 스트림 형식입니다. 이 모듈은 JSON Lines 파일을 로드하고 각 라인을 개별 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 JSON Lines Document Loader를 제공합니다:

* JSON Lines 파일 로드
* 각 라인을 개별 항목으로 처리
* 대용량 데이터 효율적 처리
* Text Splitter와 통합
* 메타데이터 추출
* 스트림 처리 지원

## 입력

### 필수 파라미터

* **File Upload**: 로드할 JSON Lines 파일

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **JSONPath**: 특정 필드를 지정하는 JSONPath 식
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* JSON Lines 파일 파싱
* 라인별 처리
* 스트림 처리
* 메타데이터 추출
* Text Splitter 지원
* 오류 처리

## 파일 형식

* 각 라인은 유효한 JSON 객체
* 개행(\n)으로 분리
* 라인별 독립적 처리
* 매우 큰 파일 효율적 처리

## 참고사항

* 각 라인이 유효한 JSON이어야 함
* 메모리 효율적 (스트림 처리)
* 라인 단위 오류는 해당 라인만 영향
* 대용량 데이터에 권장
* JSONPath 문법 확인
