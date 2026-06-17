---
설명: Notion 페이지에서 데이터 로드
---

# Notion

<figure><img src="../../../.gitbook/assets/image_notion.png" alt="" width="271"><figcaption><p>Notion 노드</p></figcaption></figure>

Notion은 팀 협업 및 문서화를 위한 올-인-원 워크스페이스입니다. 이 모듈은 Notion 페이지를 로드하고 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 Notion Document Loader를 제공합니다:

* Notion 페이지 및 데이터베이스 로드
* 페이지 계층 구조 탐색
* 텍스트 및 블록 콘텐츠 추출
* 메타데이터 추출
* Text Splitter와 통합
* Database 쿼리 지원

## 입력

### 필수 파라미터

* **Page ID**: Notion 페이지의 ID
* **Connect Credential**: Notion API 자격증명

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Database Query**: Database인 경우 필터 쿼리
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Notion 페이지 로드
* Database 쿼리
* 계층 구조 탐색
* 블록 콘텐츠 추출
* 메타데이터 추출
* Text Splitter 지원

## 지원 콘텐츠

* 제목 및 텍스트 블록
* 목록 및 토글
* 표 및 코드 블록
* 임베드 콘텐츠
* Database 항목

## 참고사항

* Notion API 자격증명 필수
* 페이지 공유 권한 필요
* API rate limit 적용 (초당 3-5 요청)
* 매우 큰 Database의 성능 고려
* Page ID는 URL에서 추출
