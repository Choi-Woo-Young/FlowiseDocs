---
설명: Oxylabs Web Scraping API 통합
---

# Oxylabs

<figure><img src="../../../.gitbook/assets/image_oxylabs.png" alt="" width="271"><figcaption><p>Oxylabs 노드</p></figcaption></figure>

Oxylabs는 대규모 웹 스크래핑을 위한 프록시 및 API 서비스를 제공합니다. 이 모듈은 Oxylabs API를 사용하여 웹 페이지를 스크래핑하고 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 웹 스크래퍼를 제공합니다:

* Oxylabs Scraper API를 통한 웹 스크래핑
* 대규모 병렬 처리
* 프록시 회전
* JavaScript 렌더링
* 캡차 처리
* Text Splitter와 통합

## 입력

### 필수 파라미터

* **URLs**: 스크래핑할 URL의 쉼표로 구분된 목록
* **Connect Credential**: Oxylabs API 자격증명

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Parser**: 응답 파싱 방식 (html, json 등)
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Scraper API 통합
* 병렬 처리
* 프록시 회전
* JavaScript 렌더링
* 캡차 처리
* 메타데이터 추출

## 특징

* 높은 성공률
* 대규모 데이터 수집 가능
* 자동 프록시 관리
* 고급 파싱 옵션
* 상세한 응답 정보

## 참고사항

* Oxylabs API 자격증명 필수
* 요청당 비용 발생
* API rate limit 및 할당량 적용
* 웹사이트 이용약관 준수
* robots.txt 존중
