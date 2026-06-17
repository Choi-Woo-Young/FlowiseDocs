---
설명: GitBook 문서에서 데이터 로드
---

# GitBook

<figure><img src="../../../.gitbook/assets/image_gitbook.png" alt="" width="271"><figcaption><p>GitBook 노드</p></figcaption></figure>

GitBook은 팀 문서화를 위한 현대적인 플랫폼입니다. 이 모듈은 GitBook Space의 페이지를 로드하고 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 GitBook Document Loader를 제공합니다:

* GitBook Space의 모든 페이지 로드
* 페이지 계층 구조 유지
* 페이지 메타데이터 추출
* 자식 페이지 처리
* Text Splitter와 통합
* 링크 및 참조 보존

## 입력

### 필수 파라미터

* **Space ID**: GitBook Space의 ID
* **Access Token**: GitBook API Access Token

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Page Limit**: 로드할 최대 페이지 수
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Space에서 페이지 로드
* 계층 구조 유지
* 메타데이터 추출
* 자식 페이지 처리
* Text Splitter 지원
* 오류 처리

## 참고사항

* 유효한 GitBook API 토큰 필요
* Space ID 필수
* 페이지 권한 존중
* API rate limit 적용
* 대용량 Space의 성능 고려
