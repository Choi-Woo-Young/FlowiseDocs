---
description: GitHub 저장소에서 데이터를 로드합니다.
---

# GitHub Document Loader

<figure><img src="../../../.gitbook/assets/image (79).png" alt="" width="260"><figcaption><p>Github Node</p></figcaption></figure>

GitHub는 버전 관리 및 협업을 위한 플랫폼입니다. 이 모듈은 GitHub 저장소에서 콘텐츠를 로드하고 처리하는 기능을 제공하며, public 및 private 저장소를 모두 지원합니다.

이 모듈은 다음을 수행할 수 있는 정교한 GitHub document loader를 제공합니다:
- GitHub 저장소에서 콘텐츠 로드
- private 저장소 액세스 지원
- 저장소를 재귀적으로 처리
- 사용자 정의 GitHub 인스턴스 처리
- concurrency 및 retries 제어
- 파일 필터링 사용자 정의
- text splitters를 사용한 콘텐츠 처리

## Inputs

### 필수 매개변수
- **Repo Link**: GitHub 저장소 URL (예: https://github.com/FlowiseAI/Flowise)
- **Branch**: 콘텐츠를 로드할 branch (기본값: main)

### 선택사항 매개변수
- **Connect Credential**: GitHub API 자격증명 (private repos 필요)
- **Recursive**: 하위 디렉토리를 처리할지 여부
- **Max Concurrency**: 최대 동시 파일 로드 수
- **Github Base URL**: enterprise 인스턴스용 사용자 정의 GitHub base URL
- **Github Instance API**: enterprise 인스턴스용 사용자 정의 GitHub API URL
- **Ignore Paths**: 무시할 경로의 glob 패턴 배열
- **Max Retries**: 최대 재시도 횟수
- **Text Splitter**: 추출된 콘텐츠를 처리하는 text splitter
- **Additional Metadata**: 추가 메타데이터가 포함된 JSON 객체
- **Omit Metadata Keys**: 생략할 메타데이터 키의 쉼표 구분 목록

## Outputs

- **Document**: 메타데이터 및 pageContent를 포함하는 document 객체의 배열
- **Text**: documents의 pageContent에서 연결된 문자열

## Features
- Public/private repo 지원
- Enterprise 인스턴스 지원
- 재귀적 디렉토리 처리
- Concurrency 제어
- Retry 메커니즘
- 경로 필터링
- Text splitting 지원
- 메타데이터 사용자 정의

## Authentication Methods

### Public Repositories
- 인증 불필요
- 속도 제한 적용
- public 콘텐츠로 제한

### Private Repositories
- GitHub access token 필요
- 더 높은 속도 제한
- private 콘텐츠 액세스
- Enterprise 지원

## Document Structure
각 document 포함:
- **pageContent**: 파일 콘텐츠
- **metadata**:
  - source: 저장소의 파일 경로
  - branch: 저장소 branch
  - commit: Commit hash
  - 추가 사용자 정의 메타데이터

## Notes
- public 및 private repos 지원
- Enterprise GitHub 인스턴스 지원
- 속도 제한이 자동으로 처리됨
- Retries를 위한 exponential backoff
- glob 패턴을 사용한 경로 필터링
- 메모리 효율적인 처리
- 잘못된 repos에 대한 오류 처리
