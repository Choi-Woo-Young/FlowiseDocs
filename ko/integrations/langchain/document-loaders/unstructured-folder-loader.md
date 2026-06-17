---
description: >-
  Unstructured.io를 사용하여 폴더에서 데이터를 로드합니다. 참고: Unstructured이 업데이트될 때까지 현재 .png 및 .heic를 지원하지 않습니다.
---

# Unstructured Folder Loader

<figure><img src="../../../.gitbook/assets/image (101).png" alt="" width="320"><figcaption><p>Unstructured Folder Loader Node</p></figcaption></figure>

Unstructured Folder Loader는 [Unstructured.io](https://unstructured.io)를 사용하여 폴더에서 여러 문서를 로드하고 처리합니다. OCR, 청킹 및 메타데이터 추출을 위한 광범위한 구성 옵션을 사용하여 고급 문서 구문 분석 기능을 제공합니다.

{% hint style="warning" %}
Unstructured이 업데이트될 때까지 현재 .png 및 .heic 파일을 지원하지 않습니다.
{% endhint %}

## 기능
- 여러 문서의 일괄 처리
- 다양한 처리 전략
- 15개 이상의 언어를 지원하는 OCR
- 유연한 청킹 전략
- 테이블 구조 추론
- XML 처리 옵션
- 페이지 나누기 처리
- 좌표 추출
- 메타데이터 사용자 정의

## 구성

### API 설정
- 기본 API URL: `http://localhost:8000/general/v0/general`
- 환경 변수를 통해 구성 가능: `UNSTRUCTURED_API_URL`
- 선택사항 API 키 인증

## 매개변수

### 필수 매개변수
- **Folder Path**: 처리할 문서를 포함하는 폴더 경로

### 선택사항 매개변수

#### 기본 구성
- **Unstructured API URL**: API 엔드포인트 (기본값: http://localhost:8000/general/v0/general)
- **Strategy**: 처리 전략 (기본값: auto)
  - hi_res: 고해상도 처리
  - fast: 빠른 처리
  - ocr_only: OCR 중심 처리
  - auto: 자동 선택
- **Encoding**: 문서 인코딩 (기본값: utf-8)

#### OCR 옵션
- **OCR Languages**: 다음을 포함한 다중 언어 지원:
  - English (eng)
  - Spanish (spa)
  - Mandarin Chinese (cmn)
  - Hindi (hin)
  - Arabic (ara)
  - Portuguese (por)
  - Bengali (ben)
  - Russian (rus)
  - Japanese (jpn)
  - 그 외 많은 언어...

#### 처리 옵션
- **Skip Infer Table Types**: 테이블 추출을 건너뛸 파일 유형 (기본값: ["pdf", "jpg", "png"])
- **Hi-Res Model Name**: hi_res 전략에 대한 모델 선택 (기본값: detectron2_onnx)
  - chipper: Unstructured의 자체 VDU 모델
  - detectron2_onnx: Facebook AI의 빠른 객체 감지
  - yolox: 단계 실시간 감지기
  - yolox_quantized: 최적화된 YOLOX 버전
- **Coordinates**: 요소 좌표 추출 (기본값: false)
- **Include Page Breaks**: 페이지 나누기 요소 포함
- **XML Keep Tags**: XML 태그 보존
- **Multi-Page Sections**: 다중 페이지 섹션 처리

#### 텍스트 청킹 옵션
- **Chunking Strategy**: 텍스트 청킹 방법 (기본값: by_title)
  - None: 청킹 없음
  - by_title: 문서 제목별 청킹
- **Combine Under N Chars**: 최소 청크 크기
- **New After N Chars**: 소프트 최대 청크 크기
- **Max Characters**: 하드 최대 청크 크기 (기본값: 500)

#### 메타데이터 옵션
- **Source ID Key**: 문서 소스 식별용 키 (기본값: source)
- **Additional Metadata**: JSON으로 사용자 정의 메타데이터
- **Omit Metadata Keys**: 메타데이터에서 제외할 키

## 지원되는 파일 유형
- 문서: .doc, .docx, .odt, .ppt, .pptx, .pdf
- 스프레드시트: .xls, .xlsx
- 텍스트: .txt, .text, .md, .rtf
- 웹: .html, .htm
- 이메일: .eml, .msg
- 이미지: .jpg, .jpeg (참고: .png 및 .heic는 현재 지원되지 않음)

## 출력 구조

### 문서 형식
처리된 각 문서에는 다음이 포함됩니다:
- **pageContent**: 추출된 텍스트 콘텐츠
- **metadata**: 
  - source: 문서 소스 식별자
  - 처리에서 나온 추가 메타데이터
  - 사용자 정의 메타데이터 (지정된 경우)

## 사용 예제

### 기본 구성
```json
{
  "folderPath": "/path/to/documents",
  "strategy": "auto",
  "encoding": "utf-8"
}
```

### 고급 처리
```json
{
  "folderPath": "/path/to/documents",
  "strategy": "hi_res",
  "hiResModelName": "detectron2_onnx",
  "ocrLanguages": ["eng", "spa", "fra"],
  "chunkingStrategy": "by_title",
  "maxCharacters": 500,
  "coordinates": true,
  "metadata": {
    "source": "company_docs",
    "department": "legal"
  }
}
```

## 모범 사례
1. 문서 품질 및 처리 요구에 따라 적절한 전략을 선택합니다
2. 문서 콘텐츠를 기반으로 OCR 언어를 구성합니다
3. 최적의 텍스트 분할을 위해 청킹 매개변수를 조정합니다
4. 사용 사례에 맞는 hi-res 모델을 사용합니다
5. 큰 폴더를 처리할 때 메모리 사용량을 고려합니다
6. API 사용량 및 응답 시간을 모니터링합니다
7. 워크플로우에서 잠재적 API 오류를 처리합니다

## 참고 사항
- 일괄적으로 여러 문서 처리
- 다양한 파일 형식 지원
- 메모리 효율적인 처리
- 자동 메타데이터 처리
- 유연한 출력 형식
- API 응답에 대한 오류 처리
- 구성 가능한 처리 옵션

{% hint style="info" %}
이 섹션은 진행 중입니다. 이 섹션을 완성하는 데 도움을 주시면 감사하겠습니다. 시작하려면 [기여 가이드](broken-reference)를 확인하세요.
{% endhint %}
