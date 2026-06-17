---
설명: Firecrawl을 사용한 웹 스크래핑
---

# Firecrawl

<figure><img src="../../../.gitbook/assets/image_firecrawl.png" alt="" width="271"><figcaption><p>Firecrawl 노드</p></figcaption></figure>

Firecrawl은 웹사이트를 스크래핑하고 LLM-ready한 markdown으로 변환하는 서비스입니다. 이 모듈은 Firecrawl API를 사용하여 웹 콘텐츠를 로드합니다.

이 모듈은 다음을 수행할 수 있는 정교한 웹 스크래퍼를 제공합니다:

* 웹페이지를 Markdown으로 변환
* JavaScript 렌더링 지원
* 메타데이터 추출
* 여러 URL 처리
* Text Splitter와 통합
* 구조화된 출력

## 입력

### 필수 파라미터

* **URLs**: 스크래핑할 URL의 쉼표로 구분된 목록
* **Connect Credential**: Firecrawl API 자격증명

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* HTML을 Markdown으로 변환
* JavaScript 렌더링
* 메타데이터 자동 추출
* 다중 URL 처리
* Text Splitter 지원
* 오류 처리

## 특징

* LLM-ready 형식
* 깨끗한 markdown 출력
* 이미지 URL 보존
* 링크 구조 유지
* 메타데이터 포함

## 참고사항

* 유효한 Firecrawl API 키 필요
* API rate limit 적용
* 웹사이트 이용약관 준수
* 크롤링 속도 제한 가능
* robots.txt 준수
