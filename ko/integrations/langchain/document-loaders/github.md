---
설명: GitHub 저장소에서 데이터 로드
---

# GitHub

<figure><img src="../../../.gitbook/assets/image_github.png" alt="" width="271"><figcaption><p>GitHub 노드</p></figcaption></figure>

GitHub Document Loader를 사용하여 GitHub 저장소의 파일과 콘텐츠를 로드할 수 있습니다. 이를 통해 GitHub 저장소의 코드, README, 문서 등을 Document로 변환할 수 있습니다.

이 모듈은 다음을 수행할 수 있는 정교한 GitHub Document Loader를 제공합니다:

* GitHub 저장소의 파일 로드
* 특정 Branch 선택
* Markdown 문서 처리
* 파일 필터링
* Text Splitter와 통합
* 메타데이터 추출

## 입력

### 필수 파라미터

* **Repository**: GitHub 저장소 (예: owner/repo)
* **Access Token**: GitHub Personal Access Token

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Branch**: 로드할 Branch (기본값: main)
* **File Extensions**: 처리할 파일 확장명의 쉼표로 구분된 목록
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* 저장소 파일 로드
* Branch 선택
* 파일 필터링
* 메타데이터 추출
* Text Splitter 지원
* 오류 처리

## 지원 형식

* Markdown (.md)
* JavaScript/TypeScript (.js, .ts)
* Python (.py)
* JSON (.json)
* 기타 텍스트 형식

## 참고사항

* 유효한 GitHub Personal Access Token 필요
* 공개 저장소는 토큰 없이도 접근 가능
* 저장소 크기에 따라 로드 시간 증가
* API rate limit 적용 (시간당 60개, 인증 시 5000개)
* 대용량 파일의 메모리 사용 주의
