---
설명: Apify Website Content Crawler에서 데이터 로드
---

# Apify Website Content Crawler

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="266"><figcaption><p>Apify Website Content Crawler 노드</p></figcaption></figure>

[Apify](https://apify.com/) Website Content Crawler는 다양한 크롤링 엔진을 사용하여 웹사이트에서 콘텐츠를 추출할 수 있는 강력한 웹 스크래핑 도구입니다. 이 모듈은 Apify의 Website Content Crawler와 통합하여 웹 콘텐츠를 로드하고 처리합니다.

이 모듈은 다음을 수행할 수 있는 정교한 웹 크롤러를 제공합니다:

* 지정된 시작 URL에서 여러 웹사이트 크롤링
* 다양한 크롤링 엔진 사용 (Chrome, Firefox, Cheerio, JSDOM)
* 크롤링 깊이 및 페이지 제한 제어
* JavaScript로 렌더링된 콘텐츠 처리
* Text Splitter로 추출된 콘텐츠 처리
* Metadata 추출 커스터마이징

## 입력

### 필수 파라미터

* **Start URLs**: 크롤링이 시작될 URL의 쉼표로 구분된 목록
* **Connect Apify API**: Apify API 자격증명
* **Crawler Type**: 크롤링 엔진 선택:
  * Headless 웹 브라우저 (Chrome+Playwright)
  * Stealthy 웹 브라우저 (Firefox+Playwright)
  * Raw HTTP 클라이언트 (Cheerio)
  * Raw HTTP 클라이언트 및 JavaScript 실행 (JSDOM)

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Max Crawling Depth**: 따를 페이지 링크의 최대 깊이 (기본값: 1)
* **Max Crawl Pages**: 크롤링할 최대 페이지 수 (기본값: 3)
* **Additional Input**: 추가 크롤러 구성이 있는 JSON 객체
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* 여러 크롤링 엔진 지원
* 구성 가능한 크롤링 파라미터
* JavaScript 렌더링 지원
* 깊이 및 페이지 제한 제어
* Metadata 커스터마이징
* Text 분할 기능
* 오류 처리

## 크롤러 유형

### Headless Chrome (Playwright)

* 최신 웹 애플리케이션에 최적
* 완전한 JavaScript 지원
* 높은 리소스 사용

### Stealthy Firefox (Playwright)

* Bot 탐지가 있는 사이트에 적합
* 완전한 JavaScript 지원
* 더 은폐된 작동

### Cheerio

* 빠르고 가벼움
* JavaScript 지원 없음
* 낮은 리소스 사용

### JSDOM (실험적)

* JavaScript 실행 지원
* 브라우저의 경량 대안
* 실험적 기능

## 참고사항

* 유효한 Apify API 토큰 필요
* 크롤러 유형마다 다른 기능
* 크롤러 유형에 따라 리소스 사용이 다름
* JavaScript 지원은 크롤러 유형에 따라 다름
* Rate limiting은 Apify 플랜에 따라 적용될 수 있음
* JSON 입력을 통해 추가 구성 사용 가능

## 전체 웹사이트 크롤

1. _(선택사항)_ [**Text Splitter**](../text-splitters/)를 연결합니다.
2. Apify API를 연결합니다 (당신의 [Apify API 토큰](https://my.apify.com/account#/integrations)으로 새 자격증명을 생성하세요).
3. 크롤러가 시작할 URL을 하나 이상 입력합니다 (쉼표로 구분), 예: `https://docs.flowiseai.com/`
4. 크롤러 유형을 선택합니다. 자세한 내용은 [Website Content Crawler 문서](https://apify.com/apify/website-content-crawler/input-schema#crawlerType)를 참조하세요.
5. _(선택사항)_ 최대 크롤링 깊이 및 크롤할 최대 페이지 수와 같은 추가 파라미터를 지정합니다.

## 출력

웹사이트 콘텐츠를 Document로 로드합니다.

## 리소스

* [Apify-Flowise integration](https://docs.apify.com/platform/integrations/flowise)
* [Website Content Crawler](https://apify.com/apify/website-content-crawler)
