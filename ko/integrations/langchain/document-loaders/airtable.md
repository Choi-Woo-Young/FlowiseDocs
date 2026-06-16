---
description: Airtable 테이블에서 데이터 로드
---

# Airtable

<figure><img src="../../../.gitbook/assets/image_airtable.png" alt="" width="271"><figcaption><p>Airtable Node</p></figcaption></figure>

Airtable는 스프레드시트와 데이터베이스의 기능을 결합한 클라우드 협업 서비스입니다. 이 모듈은 Airtable 테이블에서 데이터를 로드하고 처리하기 위한 포괄적인 기능을 제공합니다.

이 모듈은 다음과 같은 기능을 제공하는 정교한 Airtable 문서 로더입니다:

* 특정 Airtable 베이스, 테이블 및 뷰에서 데이터 로드
* 특정 필드 필터링 및 선택
* 페이지네이션 및 대용량 데이터셋 처리
* 수식을 이용한 커스텀 필터링 지원
* 텍스트 분할기로 데이터 처리
* 메타데이터 추출 커스터마이징

## 입력

### 필수 매개변수

* **Base Id**: Airtable 베이스 식별자 (예: app11RobdGoX0YNsC)
* **Table Id**: 특정 테이블 식별자 (예: tblJdmvbrgizbYICO)
* **Connect Credential**: Airtable API 자격증명

### 선택 매개변수

* **View Id**: 특정 뷰 식별자 (예: viw9UrP77Id0CE4ee)
* **Text Splitter**: 추출된 콘텐츠를 처리할 텍스트 분할기
* **Include Only Fields**: 포함할 필드 이름 또는 ID의 쉼표 구분 목록
* **Return All**: 모든 결과 반환 여부 (기본값: true)
* **Limit**: Return All이 false일 때 반환할 결과 수 (기본값: 100)
* **Filter By Formula**: 레코드를 필터링할 Airtable 수식
* **Additional Metadata**: 추가 메타데이터를 포함한 JSON 객체
* **Omit Metadata Keys**: 생략할 메타데이터 키의 쉼표 구분 목록

## 출력

* **Document**: 메타데이터 및 pageContent를 포함하는 문서 객체 배열
* **Text**: 문서의 pageContent에서 연결된 문자열

## 기능

* API 기반 데이터 검색
* 필드 선택 및 필터링
* 페이지네이션 지원
* 수식 기반 필터링
* 커스터마이징 가능한 메타데이터 처리
* 텍스트 분할 기능
* 잘못된 입력에 대한 오류 처리

## 주의사항

* 유효한 Airtable API 자격증명 필요
* Base ID와 Table ID는 필수 항목
* 쉼표를 포함하는 필드 이름은 필드 ID 사용 권장
* 필터 수식은 Airtable 수식 구문을 따라야 함
* 속도 제한 및 API 할당량 적용
* 전체 및 부분 데이터 검색 지원

## URL 구조 예시

다음과 같은 테이블 URL의 경우:

```
https://airtable.com/app11RobdGoX0YNsC/tblJdmvbrgizbYICO/viw9UrP77Id0CE4ee
```

* Base ID: app11RobdGoX0YNsC
* Table ID: tblJdmvbrgizbYICO
* View ID: viw9UrP77Id0CE4ee
