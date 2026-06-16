---
description: Confluence Document에서 데이터를 로드합니다.
---

# Confluence

## Confluence

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2).png" alt="" width="263"><figcaption><p>Confluence Node</p></figcaption></figure>

## Confluence Document Loader

Confluence는 Atlassian의 엔터프라이즈 wiki 및 협업 플랫폼입니다. 이 모듈은 Confluence spaces 및 pages에서 콘텐츠를 로드하고 처리하는 기능을 제공합니다.

이 모듈은 다음을 수행할 수 있는 정교한 Confluence document loader를 제공합니다:

* 특정 Confluence spaces에서 콘텐츠 로드
* Cloud 및 Server/Data Center 배포 모두 지원
* 다양한 방법의 인증 처리
* 검색된 페이지 수 제한
* text splitters를 사용한 콘텐츠 처리
* 메타데이터 추출 사용자 정의

### Inputs

#### 필수 매개변수

* **Base URL**: Confluence 인스턴스 URL (예: https://example.atlassian.net/wiki)
* **Space Key**: Confluence space의 고유 식별자
* **Connect Credential**: 다음 중 선택:
  * Confluence Cloud API 자격증명 (username + access token)
  * Confluence Server/DC API 자격증명 (personal access token)

#### 선택사항 매개변수

* **Text Splitter**: 추출된 콘텐츠를 처리하는 text splitter
* **Limit**: 검색할 최대 페이지 수 (무제한의 경우 0)
* **Additional Metadata**: 추가 메타데이터가 포함된 JSON 객체
* **Omit Metadata Keys**: 생략할 메타데이터 키의 쉼표 구분 목록

### Outputs

* **Document**: 메타데이터 및 pageContent를 포함하는 document 객체의 배열
* **Text**: documents의 pageContent에서 연결된 문자열

### Features

* 다중 배포 지원 (Cloud/Server/DC)
* 유연한 인증 옵션
* 페이지 제한 제어
* 콘텐츠 처리 기능
* 메타데이터 사용자 정의
* 오류 처리
* Text splitting 지원

### Authentication Methods

#### Confluence Cloud

* username과 access token 필요
* Atlassian 계정 설정에서 생성된 access token
* API 토큰 인증 지원

#### Confluence Server/Data Center

* personal access token 사용
* Confluence 인스턴스에서 생성된 토큰
* 직접 서버 액세스 지원

### Notes

* Space Key는 Confluence space 설정에서 찾을 수 있음
* Cloud와 Server의 다양한 인증 방법
* 인스턴스에 따라 속도 제한이 적용될 수 있음
* 콘텐츠에는 페이지 텍스트 및 메타데이터 포함
* 전체 및 부분 콘텐츠 검색 지원
* 잘못된 자격증명 또는 URL에 대한 오류 처리

### Finding Space Key

Confluence Space Key를 찾으려면:

1. Confluence에서 space로 이동
2. Space Settings로 이동
3. 개요에서 "Space Key" 찾기
4. 형식 예시: \~EXAMPLE362906de5d343d49dcdbae5dEXAMPLE
