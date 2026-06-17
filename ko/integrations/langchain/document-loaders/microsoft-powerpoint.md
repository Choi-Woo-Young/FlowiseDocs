---
설명: Microsoft PowerPoint 파일에서 데이터 로드
---

# Microsoft PowerPoint

<figure><img src="../../../.gitbook/assets/image_powerpoint.png" alt="" width="271"><figcaption><p>Microsoft PowerPoint 노드</p></figcaption></figure>

Microsoft PowerPoint Document Loader를 사용하여 PowerPoint 파일의 슬라이드와 콘텐츠를 로드하고 Document로 변환할 수 있습니다.

이 모듈은 다음을 수행할 수 있는 정교한 PowerPoint Document Loader를 제공합니다:

* PowerPoint 파일 로드
* 각 슬라이드 텍스트 추출
* 제목 및 내용 처리
* 슬라이드 메타데이터 추출
* Text Splitter와 통합
* 슬라이드 번호 정보 유지

## 입력

### 필수 파라미터

* **File Upload**: 로드할 PowerPoint 파일

### 선택적 파라미터

* **Text Splitter**: 추출된 콘텐츠를 처리하기 위한 Text Splitter
* **Slide Range**: 로드할 슬라이드 범위 (예: 1-10)
* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Omit Metadata Keys**: 생략할 metadata 키의 쉼표로 구분된 목록

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* PowerPoint 파일 파싱
* 슬라이드별 텍스트 추출
* 메타데이터 추출
* 슬라이드 범위 선택
* Text Splitter 지원
* 오류 처리

## 지원 형식

* .pptx (PowerPoint 2007+)
* 텍스트 박스 및 제목
* 표 및 목록
* 슬라이드 메모

## 참고사항

* 유효한 PowerPoint 파일 형식 필수
* 이미지와 차트는 텍스트로 추출되지 않음
* 매우 큰 프레젠테이션의 처리 시간 주의
* 암호 보호 파일은 지원 안 함
* 슬라이드 메모도 추출 가능
