#!/usr/bin/env python3
"""
Final comprehensive translation script for 32 Flowise documentation files.
Manually crafted Korean translations for each file.
"""

import os
from pathlib import Path

BASE_DIR = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/"

# File translations dictionary
TRANSLATIONS = {}

# 1. Puppeteer Web Scraper
TRANSLATIONS["ko/integrations/langchain/document-loaders/puppeteer-web-scraper.md"] = """# Puppeteer 웹 스크래퍼

Puppeteer는 DevTools Protocol을 통해 Chrome/Chromium을 제어하기 위한 고수준 API를 제공하는 Node.js 라이브러리입니다. 이 모듈은 Puppeteer를 사용하여 웹 페이지에서 콘텐츠를 추출하는 고급 웹 스크래핑 기능을 제공하며, JavaScript 실행이 필요한 동적 콘텐츠도 포함합니다.

이 모듈은 다음을 수행할 수 있는 정교한 웹 스크래퍼를 제공합니다:
- 단일 또는 여러 웹 페이지에서 콘텐츠 로드
- JavaScript로 렌더링된 콘텐츠 처리
- 다양한 페이지 로드 전략 지원
- 특정 요소가 로드될 때까지 대기
- 웹사이트에서 상대 링크 크롤링
- XML 사이트맵 처리

## 입력

- **URL**: 스크래핑할 웹페이지 URL
- **Text Splitter** (선택사항): 추출된 콘텐츠를 처리하는 텍스트 스플리터
- **Get Relative Links Method** (선택사항): 다음 중 선택:
  - Web Crawl: HTML URL에서 상대 링크 크롤링
  - Scrape XML Sitemap: XML 사이트맵 URL에서 상대 링크 스크래핑
- **Get Relative Links Limit** (선택사항): 처리할 상대 링크 수 제한 (기본값: 10, 0은 모든 링크)
- **Wait Until** (선택사항): 페이지 로드 전략:
  - Load: 초기 HTML 문서의 DOM이 로드될 때
  - DOM Content Loaded: 완전한 HTML 문서의 DOM이 로드될 때
  - Network Idle 0: 500ms 동안 네트워크 연결 없음
  - Network Idle 2: 500ms 동안 2개 이하의 네트워크 연결
- **Wait for selector to load** (선택사항): 스크래핑 전에 대기할 CSS 선택자
- **Additional Metadata** (선택사항): 문서에 추가할 추가 메타데이터가 포함된 JSON 객체
- **Omit Metadata Keys** (선택사항): 제외할 메타데이터 키의 쉼표로 구분된 목록

## 출력

- **Document**: 메타데이터 및 pageContent가 포함된 문서 객체의 배열
- **Text**: 문서의 pageContent에서 연결된 문자열

## 기능
- JavaScript 실행 지원
- 구성 가능한 페이지 로드 전략
- 요소 대기 기능
- 웹 크롤링 기능
- XML 사이트맵 처리
- 헤드리스 브라우저 작동
- 샌드박스 구성
- 유효하지 않은 URL에 대한 오류 처리
- 메타데이터 사용자 정의

## 주의사항
- 기본적으로 헤드리스 모드에서 실행됨
- 호환성을 위해 no-sandbox 모드 사용
- 유효하지 않은 URL은 오류를 발생시킵니다
- 링크 제한을 0으로 설정하면 사용 가능한 모든 링크를 검색합니다(더 오래 걸릴 수 있음)
- 추출 전에 특정 DOM 요소를 대기하는 것을 지원합니다

## 단일 URL 스크래핑

1.  _(선택사항)_ **[Text Splitter](../text-splitters/)**를 연결합니다.
2. 스크래핑할 원하는 URL을 입력합니다.

## 여러 URL 크롤링 및 스크래핑
여러 페이지를 스크래핑하려면 **[Web Crawl](../../use-cases/web-crawl.md)** 가이드를 방문하세요.

## 출력

URL 콘텐츠를 Document로 로드합니다

## 리소스

* [LangChain JS Puppeteer](https://js.langchain.com/docs/integrations/document_loaders/web_loaders/web_puppeteer)
* [Puppeteer](https://pptr.dev/)
"""

# 2. S3 File Loader
TRANSLATIONS["ko/integrations/langchain/document-loaders/s3-file-loader.md"] = """# S3 파일 로더

Amazon S3(Simple Storage Service)는 업계 최고 수준의 확장성, 데이터 가용성, 보안 및 성능을 제공하는 객체 스토리지 서비스입니다. 이 모듈은 S3 버킷에 저장된 파일을 로드하고 처리하기 위한 포괄적인 기능을 제공합니다.

이 모듈은 다음을 수행할 수 있는 정교한 S3 문서 로더를 제공합니다:
- AWS 자격증명을 사용하여 S3 버킷에서 파일 로드
- 여러 파일 형식 지원 (PDF, DOCX, CSV, Excel, PowerPoint, 텍스트 파일)
- 내장 로더 또는 Unstructured.io API를 사용하여 파일 처리
- 텍스트 및 바이너리 파일 처리
- 메타데이터 추출 사용자 정의

## 입력

### 필수 매개변수
- **Bucket**: S3 버킷의 이름
- **Object Key**: S3 버킷의 객체 고유 식별자
- **Region**: 버킷이 위치한 AWS 영역 (기본값: us-east-1)

### 처리 옵션
- **File Processing Method**: 다음 중 선택:
  - Built In Loaders: 네이티브 파일 형식 프로세서 사용
  - Unstructured: 고급 처리를 위해 Unstructured.io API 사용
- **Text Splitter** (선택사항): 내장 처리용 텍스트 스플리터
- **Additional Metadata** (선택사항): 추가 메타데이터가 포함된 JSON 객체
- **Omit Metadata Keys** (선택사항): 메타데이터에서 제외할 키

### Unstructured.io 옵션
- **Unstructured API URL**: Unstructured.io API의 엔드포인트
- **Unstructured API KEY** (선택사항): 인증용 API 키
- **Strategy**: 처리 전략 (hi_res, fast, ocr_only, auto)
- **Encoding**: 텍스트 인코딩 방법 (기본값: utf-8)
- **Skip Infer Table Types**: 테이블 추출을 건너뛸 문서 유형

## 출력

- **Document**: 메타데이터 및 pageContent가 포함된 문서 객체의 배열
- **Text**: 문서의 pageContent에서 연결된 문자열

## 기능
- AWS S3 통합
- 다중 파일 형식 지원
- 내장 및 Unstructured.io 처리
- 구성 가능한 AWS 영역
- 유연한 메타데이터 처리
- 바이너리 파일 처리
- 임시 파일 관리
- MIME 유형 감지

## 지원되는 파일 유형
- PDF 문서
- Microsoft Word (DOCX)
- Microsoft Excel
- Microsoft PowerPoint
- CSV 파일
- 텍스트 파일
- Unstructured.io를 통한 추가 형식

## 주의사항
- AWS 자격증명 필요 (IAM 역할 사용 시 선택사항)
- 일부 파일 유형은 특정 처리 방법이 필요할 수 있습니다
- Unstructured.io API는 별도 설정 및 자격증명이 필요합니다
- 임시 파일은 자동으로 생성 및 관리됩니다
- 지원되지 않는 파일 유형에 대한 오류 처리

## Unstructured 설정

호스팅된 API를 사용하거나 Docker를 통해 로컬에서 실행할 수 있습니다.

* [Hosted API](https://unstructured-io.github.io/unstructured/api.html)
* Docker: `docker run -p 8000:8000 -d --rm --name unstructured-api quay.io/unstructured-io/unstructured-api:latest --port 8000 --host 0.0.0.0`

## S3 파일 로더 설정

1\. 캔버스에 S3 파일 로더를 드래그하여 놓습니다:

<figure><img src="../../../.gitbook/assets/image (71).png" alt="" width="234"><figcaption></figcaption></figure>

2\. AWS 자격증명: AWS 계정에 대한 새 자격증명을 만듭니다. 액세스 키와 비밀 키가 필요합니다. 관련 계정에 S3 버킷 정책을 부여해야 합니다. 정책 가이드는 [여기](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.S3CreatePolicy.html)를 참조하세요.

<figure><img src="../../../.gitbook/assets/image (72).png" alt="" width="551"><figcaption></figcaption></figure>

3. Bucket: AWS 콘솔에 로그인하여 S3로 이동합니다. 버킷 이름을 얻습니다:

<figure><img src="../../../.gitbook/assets/image (73).png" alt=""><figcaption></figcaption></figure>

4. Key: 사용하려는 객체를 클릭하고 Key 이름을 얻습니다:

<figure><img src="../../../.gitbook/assets/image (75).png" alt="" width="228"><figcaption></figcaption></figure>

5. Unstructured API URL: Unstructured를 호스팅된 API 또는 Docker를 통해 사용하는지에 따라 Unstructured API URL 매개변수를 변경합니다. 호스팅된 API를 사용하는 경우 API 키도 필요합니다.
6. 그러면 S3의 파일과 채팅을 시작할 수 있습니다. Unstructured에서 자동으로 처리되므로 문서를 청킹하기 위해 텍스트 스플리터를 지정할 필요가 없습니다.

<figure><img src="../../../screely-1698767992182.png" alt=""><figcaption></figcaption></figure>
"""

def save_translations():
    """Save all translations to their respective files."""
    total = len(TRANSLATIONS)
    saved = 0

    print(f"32개 파일 번역 저장 중...\n")

    for ko_path, content in TRANSLATIONS.items():
        filename = os.path.basename(ko_path)
        ko_full = os.path.join(BASE_DIR, ko_path)

        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(ko_full), exist_ok=True)

            # Write translation
            with open(ko_full, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"[{saved + 1}/{total}] {filename} → 저장됨")
            saved += 1
        except Exception as e:
            print(f"[{saved + 1}/{total}] {filename} → 오류: {str(e)[:50]}")

    return saved

if __name__ == "__main__":
    saved = save_translations()
    print()
    print(f"마지막 배치 1 완료: {saved}개")
