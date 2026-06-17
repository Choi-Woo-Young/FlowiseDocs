---
설명: Confluence Document에서 데이터 로드
---

# Confluence

<figure><img src="../../../.gitbook/assets/image_confluence.png" alt="" width="271"><figcaption><p>Confluence 노드</p></figcaption></figure>

Confluence는 팀 협업을 위한 클라우드 기반 위키 및 문서 관리 플랫폼입니다. 이 모듈은 Confluence에서 페이지를 로드하고 Document로 변환할 수 있는 기능을 제공합니다.

이 모듈은 다음을 수행할 수 있는 정교한 Confluence Document Loader를 제공합니다:

* Confluence Space 및 페이지에서 콘텐츠 로드
* 페이지 계층 및 자식 페이지 처리
* 페이지 메타데이터 및 속성 추출
* Text Splitter로 콘텐츠 처리
* 첨부 파일 및 링크 처리
* 커스텀 metadata 추출

## 입력

### 필수 파라미터

* **Base URL**: Confluence 인스턴스의 기본 URL (예: https://yourspace.atlassian.net)
* **Space Key**: 로드할 Confluence Space의 키
* **Connect Credential**: Confluence API 자격증명

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Page Title Filter**: 포함할 페이지 제목의 필터
* **Include Child Pages**: 자식 페이지 포함 여부 (기본값: true)
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Space에서 페이지 로드
* 페이지 계층 구조 탐색
* Metadata 자동 추출
* Child 페이지 처리
* Text 분할 기능
* 오류 처리

## 참고사항

* 유효한 Confluence API 자격증명 필요
* Space Key 필수
* 페이지 권한 존중
* API rate limit 적용
* Confluence 버전 호환성 확인
* 대용량 Space의 경우 성능 고려
