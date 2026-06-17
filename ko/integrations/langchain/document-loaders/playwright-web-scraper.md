---
설명: Playwright를 사용한 웹 스크래핑
---

# Playwright Web Scraper

<figure><img src="../../../.gitbook/assets/image_playwright.png" alt="" width="271"><figcaption><p>Playwright Web Scraper 노드</p></figcaption></figure>

Playwright는 최신 웹 애플리케이션을 자동화하기 위한 Node.js 라이브러리입니다. 이 모듈은 Playwright를 사용하여 JavaScript 렌더링이 필요한 웹 페이지를 스크래핑합니다.

이 모듈은 다음을 수행할 수 있는 정교한 웹 스크래퍼를 제공합니다:

* Playwright 브라우저 자동화
* 동적 웹 페이지 로드 및 렌더링
* JavaScript 실행 및 콘텐츠 동적 생성 처리
* 페이지 상호작용 (클릭, 입력 등)
* CSS 선택자를 사용한 요소 추출
* Text Splitter와 통합

## 입력

### 필수 파라미터

* **URLs**: 스크래핑할 URL의 쉼표로 구분된 목록

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Selector**: 추출할 HTML 요소의 CSS 선택자
* **Wait For Selector**: 페이지 로드 대기 조건 (CSS 선택자)
* **Timeout**: 페이지 로드 제한시간 (밀리초)
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* 동적 페이지 렌더링
* JavaScript 실행
* 페이지 상호작용
* CSS 선택자 지원
* 메타데이터 추출
* Text Splitter 지원

## 특징

* 현대적 웹 애플리케이션 지원
* Chromium, Firefox, WebKit 지원
* 완전한 자동화 가능
* 높은 리소스 사용
* 느린 처리 속도

## 참고사항

* 높은 리소스 사용 (브라우저 실행 필요)
* 처리 속도가 느림 (동적 로드)
* 제한된 동시 실행 (시스템 리소스)
* 웹사이트 이용약관 준수
* robots.txt 존중
* CSS 선택자 문법 확인
