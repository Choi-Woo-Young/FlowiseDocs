---
설명: Jira Issue에서 데이터 로드
---

# Jira

<figure><img src="../../../.gitbook/assets/image_jira.png" alt="" width="271"><figcaption><p>Jira 노드</p></figcaption></figure>

Jira Document Loader를 사용하여 Jira 프로젝트의 Issue를 로드하고 Document로 변환할 수 있습니다. 이를 통해 Issue의 제목, 설명, 댓글 등을 처리할 수 있습니다.

이 모듈은 다음을 수행할 수 있는 정교한 Jira Document Loader를 제공합니다:

* Jira Issue 로드
* JQL (Jira Query Language) 지원
* Issue 검색 및 필터링
* 댓글 및 히스토리 추출
* Text Splitter와 통합
* 메타데이터 추출

## 입력

### 필수 파라미터

* **Domain**: Jira 인스턴스의 도메인 (예: https://yourcompany.atlassian.net)
* **Connect Credential**: Jira API 자격증명

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **JQL**: Jira Query Language로 Issue 필터링
* **Max Results**: 반환할 최대 Issue 수
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Jira Issue 로드
* JQL 기반 검색
* Issue 필터링
* 메타데이터 추출
* 댓글 처리
* Text Splitter 지원

## 추출 내용

* Issue ID 및 Key
* 제목 및 설명
* 담당자 및 reporter
* 상태 및 우선순위
* 댓글 및 히스토리
* 첨부 파일 정보

## 참고사항

* 유효한 Jira API 토큰 필요
* 프로젝트 접근 권한 필수
* API rate limit 적용
* JQL 쿼리 문법 확인
* 대규모 Issue 검색의 성능 고려
