---
description: 텍스트 파일에서 데이터를 로드합니다.
---

# Text File

<figure><img src="../../../.gitbook/assets/image (89).png" alt="" width="322"><figcaption><p>Text File Node</p></figcaption></figure>

Text File 로더를 사용하면 다양한 텍스트 기반 파일 형식에서 콘텐츠를 로드하고 처리할 수 있습니다. 여러 파일 유형을 지원하며 텍스트 분할 및 메타데이터 처리를 위한 유연한 옵션을 제공합니다.

## 기능
- 다양한 텍스트 기반 파일 형식 지원
- 다중 파일 로딩 기능
- 텍스트 분할 지원
- 사용자 정의 가능한 메타데이터 처리
- 스토리지 통합 지원
- Base64 파일 처리
- 다양한 출력 형식

## 지원되는 파일 유형
로더는 다양한 텍스트 기반 파일 형식을 지원합니다:
- 텍스트 파일 (.txt)
- 웹 파일 (.html, .aspx, .asp, .css)
- 프로그래밍 언어:
  - C/C++ (.cpp, .c, .h)
  - C# (.cs)
  - Go (.go)
  - Java (.java)
  - JavaScript/TypeScript (.js, .ts)
  - PHP (.php)
  - Python (.py, .python)
  - Ruby (.rb, .ruby)
  - Rust (.rs)
  - Scala (.sc, .scala)
  - Solidity (.sol)
  - Swift (.swift)
  - Visual Basic (.vb)
- 마크업/스타일:
  - CSS/LESS/SCSS (.css, .less, .scss)
  - Markdown (.md, .markdown)
  - XML (.xml)
  - LaTeX (.tex, .ltx)
- 기타:
  - Protocol Buffers (.proto)
  - SQL (.sql)
  - RST (.rst)

## 입력

### 필수 매개변수
- **Txt File**: 처리할 텍스트 파일 하나 이상
  - 로컬 업로드 또는 스토리지의 파일 수락
  - 다중 파일 선택 지원

### 선택사항 매개변수
- **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 텍스트 분할기
- **Additional Metadata**: 문서에 추가할 추가 메타데이터가 포함된 JSON 객체
- **Omit Metadata Keys**: 제외할 메타데이터 키의 쉼표 구분 목록
  - 형식: `key1, key2, key3.nestedKey1`
  - *를 사용하여 모든 기본 메타데이터 제거

## 출력

- **Document**: 다음을 포함하는 문서 객체의 배열:
  - metadata: 파일 메타데이터 및 사용자 정의 필드
  - pageContent: 추출된 텍스트 콘텐츠
- **Text**: 추출된 모든 콘텐츠의 연결된 문자열

## 문서 구조
각 문서에는 다음이 포함됩니다:
- **pageContent**: 텍스트 파일의 주요 콘텐츠
- **metadata**:
  - 기본 파일 메타데이터
  - 추가 사용자 정의 메타데이터 (지정된 경우)
  - 필터링된 메타데이터 (생략된 키 기반)

## 사용 예제

### 단일 파일 처리
```json
{
  "txtFile": "example.txt",
  "metadata": {
    "source": "local",
    "category": "documentation"
  }
}
```

### 여러 파일 처리
```json
{
  "txtFile": ["doc1.txt", "doc2.md", "code.py"],
  "metadata": {
    "batch": "docs-2024",
    "processor": "text-loader"
  },
  "omitMetadataKeys": "source, timestamp"
}
```

## 스토리지 통합
로더는 두 가지 파일 소스 모드를 지원합니다:
1. **Direct Upload**: 인터페이스를 통해 직접 업로드된 파일
2. **Storage Integration**: 스토리지 시스템을 통해 액세스된 파일
   - 형식: `FILE-STORAGE::filename.txt`
   - 조직 및 chatflow 특정 스토리지 지원

## 참고 사항
- 단일 및 다중 파일 처리 모두 처리
- Base64 인코딩된 파일 콘텐츠 지원
- 다양한 파일 인코딩 자동 처리
- 대용량 파일의 메모리 효율적인 처리
- 필요에 따라 파일 메타데이터 보존
- 대규모 문서에 대한 텍스트 분할 지원
- 출력 텍스트의 이스케이프 문자 처리
- 조직별 스토리지와 통합

{% hint style="info" %}
이 섹션은 진행 중입니다. 이 섹션을 완성하는 데 도움을 주시면 감사하겠습니다. 시작하려면 [기여 가이드](broken-reference)를 확인하세요.
{% endhint %}
