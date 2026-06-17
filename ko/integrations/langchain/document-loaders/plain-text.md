---
설명: 일반 텍스트 파일에서 데이터 로드
---

# Plain Text

<figure><img src="../../../.gitbook/assets/image_plaintext.png" alt="" width="271"><figcaption><p>Plain Text 노드</p></figcaption></figure>

Plain Text Document Loader를 사용하여 일반 텍스트 파일을 로드하고 Document로 변환할 수 있습니다. .txt 및 기타 텍스트 형식을 지원합니다.

이 모듈은 다음을 수행할 수 있습니다:

* 일반 텍스트 파일 로드
* 파일 인코딩 자동 감지
* Text Splitter와 통합
* 메타데이터 추출
* 간단하고 빠른 처리

## 입력

### 필수 파라미터

* **File Upload**: 로드할 텍스트 파일

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* 텍스트 파일 로드
* 인코딩 자동 감지
* Text Splitter 지원
* 메타데이터 추출
* 오류 처리

## 지원 형식

* .txt (일반 텍스트)
* .log (로그 파일)
* .md (Markdown, 선택사항)
* 기타 텍스트 기반 형식

## 참고사항

* 인코딩 호환성 확인
* 매우 큰 파일의 메모리 사용 주의
* 바이너리 파일은 지원하지 않음
* 특수 문자 처리 고려
* 성능 최적화를 위해 적절한 Text Splitter 사용 권장
