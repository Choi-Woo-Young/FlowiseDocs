---
설명: Figma 디자인에서 데이터 로드
---

# Figma

<figure><img src="../../../.gitbook/assets/image_figma.png" alt="" width="271"><figcaption><p>Figma 노드</p></figcaption></figure>

Figma는 클라우드 기반 디자인 협업 도구입니다. 이 모듈은 Figma 파일의 구조, 컴포넌트, 메타데이터를 로드하고 Document로 변환합니다.

이 모듈은 다음을 수행할 수 있는 정교한 Figma Document Loader를 제공합니다:

* Figma 파일 및 프레임 로드
* 컴포넌트 및 스타일 정보 추출
* 텍스트 콘텐츠 추출
* 디자인 메타데이터 추출
* 계층 구조 정보 보존
* Text Splitter와 통합

## 입력

### 필수 파라미터

* **File Key**: Figma 파일의 File Key (URL에서 추출)
* **Connect Credential**: Figma API 자격증명

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Frame Names**: 추출할 Frame 이름의 쉼표로 구분된 목록
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* Figma 파일 접근
* Frame 추출
* 컴포넌트 정보 추출
* 메타데이터 수집
* Text Splitter 지원
* 오류 처리

## 참고사항

* 유효한 Figma API 토큰 필요
* File Key 필수
* 파일 공유 권한 필요
* API rate limit 적용
* 대용량 파일의 성능 고려
