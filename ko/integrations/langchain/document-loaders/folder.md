---
설명: 폴더의 파일들에서 데이터 로드
---

# Folder

<figure><img src="../../../.gitbook/assets/image_folder.png" alt="" width="271"><figcaption><p>Folder 노드</p></figcaption></figure>

Folder Loader를 사용하면 특정 폴더 내의 모든 지원되는 파일을 자동으로 로드하고 Document로 변환할 수 있습니다. 이는 대량의 파일을 한 번에 처리하는 데 유용합니다.

이 모듈은 다음을 수행할 수 있습니다:

* 폴더의 모든 파일 자동 감지
* 다양한 파일 형식 처리
* 재귀적 폴더 탐색 (선택사항)
* 파일 필터링
* 일괄 Document 생성
* Text Splitter와 통합

## 입력

### 필수 파라미터

* **Folder Path**: 로드할 폴더의 경로

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Recursive**: 하위 폴더 포함 여부 (기본값: true)
* **File Extensions**: 처리할 파일 확장명의 쉼표로 구분된 목록
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* 폴더 스캔
* 파일 자동 감지
* 재귀적 탐색
* 파일 필터링
* 일괄 처리
* Text Splitter 지원

## 지원 파일 형식

* PDF
* DOCX
* TXT
* JSON
* CSV
* EPUB
* Markdown

## 참고사항

* 폴더 경로 접근 권한 필요
* 파일 수에 따라 처리 시간 증가
* 성능 최적화를 위해 필터링 권장
* 대용량 폴더의 경우 메모리 사용 주의
* 재귀 깊이 제한 고려
