# Puppeteer Web Scraper

Puppeteer는 DevTools Protocol을 통해 Chrome/Chromium을 제어하는 고수준 API를 제공하는 Node.js 라이브러리입니다. 이 모듈은 Puppeteer를 사용하여 JavaScript 실행이 필요한 동적 콘텐츠를 포함하여 웹 페이지에서 콘텐츠를 추출하는 고급 웹 스크래핑 기능을 제공합니다.

이 모듈은 다음을 수행할 수 있는 정교한 웹 스크래퍼를 제공합니다:
- 단일 또는 여러 웹 페이지에서 콘텐츠 로드
- JavaScript 렌더링 콘텐츠 처리
- 다양한 페이지 로드 전략 지원
- 특정 요소 로드 대기
- 웹사이트에서 상대 링크 크롤링
- XML 사이트맵 처리

## 입력

- **URL**: 스크래핑할 웹페이지 URL
- **Text Splitter** (선택사항): 추출된 콘텐츠를 처리하기 위한 텍스트 분할기
- **Get Relative Links Method** (선택사항): 다음 중 선택:
  - Web Crawl: HTML URL에서 상대 링크 크롤링
  - Scrape XML Sitemap: XML 사이트맵 URL에서 상대 링크 스크래핑
- **Get Relative Links Limit** (선택사항): 처리할 상대 링크 수의 제한 (기본값: 10, 0은 모든 링크)
- **Wait Until** (선택사항): 페이지 로드 전략:
  - Load: 초기 HTML 문서의 DOM이 로드된 경우
  - DOM Content Loaded: 전체 HTML 문서의 DOM이 로드된 경우
  - Network Idle 0: 500ms 동안 네트워크 연결 없음
  - Network Idle 2: 500ms 동안 2개 이하의 네트워크 연결
- **Wait for selector to load** (선택사항): 스크래핑 전에 대기할 CSS 선택자
- **Additional Metadata** (선택사항): 문서에 추가할 추가 메타데이터가 포함된 JSON 객체
- **Omit Metadata Keys** (선택사항): 생략할 메타데이터 키의 쉼표 구분 목록

## 출력

- **Document**: 메타데이터와 pageContent를 포함하는 문서 객체의 배열
- **Text**: 문서의 pageContent에서 연결된 문자열

## 기능
- JavaScript 실행 지원
- 구성 가능한 페이지 로드 전략
- 요소 대기 기능
- 웹 크롤링 기능
- XML 사이트맵 처리
- 헤드리스 브라우저 작동
- 샌드박스 구성
- 잘못된 URL에 대한 오류 처리
- 메타데이터 사용자 정의

## 참고 사항
- 기본적으로 헤드리스 모드에서 실행됨
- 호환성을 위해 no-sandbox 모드 사용
- 잘못된 URL은 오류를 발생시킵니다
- 링크 제한을 0으로 설정하면 사용 가능한 모든 링크가 검색됩니다 (더 오래 걸릴 수 있음)
- 추출 전에 특정 DOM 요소를 대기하는 것을 지원합니다

## 단일 URL 스크래핑

1.  _(선택사항)_ **[Text Splitter](../text-splitters/)**를 연결합니다.
2. 스크래핑할 원하는 URL을 입력합니다.

## 여러 URL 크롤링 및 스크래핑
여러 페이지의 스크래핑을 허용하려면 **[Web Crawl](../../use-cases/web-crawl.md)** 가이드를 방문하세요.

## 출력

URL 콘텐츠를 Document로 로드합니다

## 리소스

* [LangChain JS Puppeteer](https://js.langchain.com/docs/integrations/document_loaders/web_loaders/web_puppeteer)
* [Puppeteer](https://pptr.dev/)
