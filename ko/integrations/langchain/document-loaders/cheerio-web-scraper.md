---
설명: Cheerio를 사용한 웹 스크래핑
---

# Cheerio Web Scraper

<figure><img src="../../../.gitbook/assets/image_cheerio.png" alt="" width="271"><figcaption><p>Cheerio Web Scraper 노드</p></figcaption></figure>

Cheerio는 서버측 jQuery 구현으로, Node.js에서 HTML/XML을 빠르고 쉽게 파싱하고 조작할 수 있게 해줍니다. 이 모듈은 Cheerio를 사용하여 웹 페이지를 스크래핑하고 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 웹 스크래퍼를 제공합니다:

* 다중 URL에서 웹 페이지 로드
* jQuery 선택자를 사용한 HTML 파싱 및 추출
* JavaScript 렌더링 없이 정적 콘텐츠 처리
* Text Splitter로 추출된 콘텐츠 처리
* Metadata 추출 및 커스터마이징
* 경량 및 빠른 스크래핑 작업

## 입력

### 필수 파라미터

* **URLs**: 스크래핑할 URL의 쉼표로 구분된 목록

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Selector**: HTML 요소를 추출하기 위한 CSS 선택자
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* 다중 URL 스크래핑
* jQuery 선택자 지원
* 빠른 HTML 파싱
* 경량 처리
* Metadata 커스터마이징
* 오류 처리

## 특징

* JavaScript 실행 불필요 (정적 콘텐츠용)
* 빠르고 효율적
* 경량 리소스 사용
* jQuery 유사 API
* 정규식 지원
* 네임스페이스 지원

## 참고사항

* 웹사이트의 robots.txt 및 이용약관 준수
* JavaScript로 렌더링된 동적 콘텐츠는 로드되지 않음
* 큰 HTML 파일의 경우 메모리 사용량 주의
* 요청 실패에 대한 적절한 오류 처리
* Rate limiting 고려
