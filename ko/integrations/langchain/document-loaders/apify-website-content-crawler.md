---
description: Apify Website Content Crawler에서 데이터를 로드합니다.
---

# Apify Website Content Crawler

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="266"><figcaption><p>Apify Website Content Crawler Node</p></figcaption></figure>

[Apify](https://apify.com/) Website Content Crawler는 다양한 crawling engines를 사용하여 웹사이트에서 콘텐츠를 추출할 수 있는 강력한 웹 스크래핑 도구입니다. 이 모듈은 Apify의 Website Content Crawler와의 통합을 제공하여 웹 콘텐츠를 로드하고 처리합니다.

이 모듈은 다음을 수행할 수 있는 정교한 웹 crawler를 제공합니다:

* 지정된 시작 URL에서 여러 웹사이트 crawl
* 다양한 crawling engines 사용 (Chrome, Firefox, Cheerio, JSDOM)
* crawling depth 및 페이지 제한 제어
* JavaScript로 렌더링된 콘텐츠 처리
* text splitters를 사용한 추출된 콘텐츠 처리
* 메타데이터 추출 사용자 정의

## Inputs

### 필수 매개변수

* **Start URLs**: crawling이 시작될 URL의 쉼표 구분 목록
* **Connect Apify API**: Apify API 자격증명
* **Crawler Type**: crawling engine 선택:
  * Headless 웹 브라우저 (Chrome+Playwright)
  * Stealthy 웹 브라우저 (Firefox+Playwright)
  * Raw HTTP 클라이언트 (Cheerio)
  * JavaScript 실행 지원 Raw HTTP 클라이언트 (JSDOM)

### 선택사항 매개변수

* **Text Splitter**: 추출된 콘텐츠를 처리하는 text splitter
* **Max Crawling Depth**: 따라갈 페이지 링크의 최대 깊이 (기본값: 1)
* **Max Crawl Pages**: crawl할 최대 페이지 수 (기본값: 3)
* **Additional Input**: 추가 crawler 구성이 포함된 JSON 객체
* **Additional Metadata**: 추가 메타데이터가 포함된 JSON 객체
* **Omit Metadata Keys**: 생략할 메타데이터 키의 쉼표 구분 목록

## Outputs

* **Document**: 메타데이터 및 pageContent를 포함하는 document 객체의 배열
* **Text**: documents의 pageContent에서 연결된 문자열

## Features

* 다중 crawling engine 지원
* 구성 가능한 crawling 매개변수
* JavaScript 렌더링 지원
* Depth 및 페이지 제한 제어
* 메타데이터 사용자 정의
* Text splitting 기능
* 오류 처리

## Crawler Types

### Headless Chrome (Playwright)

* 최신 웹 애플리케이션에 최적
* 완전한 JavaScript 지원
* 높은 리소스 사용량

### Stealthy Firefox (Playwright)

* 봇 감지 방지 사이트에 적합
* 완전한 JavaScript 지원
* 더 은폐된 작동

### Cheerio

* 빠르고 가벼움
* JavaScript 미지원
* 낮은 리소스 사용량

### JSDOM (Experimental)

* JavaScript 실행 지원
* 브라우저의 경량 대안
* 실험적 기능

## Notes

* 유효한 Apify API 토큰 필요
* 다양한 crawler 유형은 다양한 기능을 가짐
* 리소스 사용량은 crawler 유형에 따라 다름
* JavaScript 지원은 crawler 유형에 따라 달라짐
* Apify 계획에 따라 속도 제한이 적용될 수 있음
* JSON 입력을 통해 추가 구성 가능

## 전체 웹사이트 Crawl

1. _(선택사항)_ [**Text Splitter**](../text-splitters/)에 연결합니다.
2. Apify API에 연결 ([Apify API 토큰](https://my.apify.com/account#/integrations)으로 새 자격증명 생성).
3. crawler가 시작할 URL을 하나 이상 입력합니다 (쉼표로 구분), 예: `https://docs.flowiseai.com/`.
4. crawler 유형을 선택합니다. [Website Content Crawler 문서](https://apify.com/apify/website-content-crawler/input-schema#crawlerType)에서 더 자세한 정보를 확인하세요.
5. _(선택사항)_ 최대 crawling depth 및 최대 crawl 페이지 수와 같은 추가 매개변수를 지정합니다.

## Output
