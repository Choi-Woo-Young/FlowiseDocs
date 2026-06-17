---
설명: 커스텀 함수를 사용하여 문서 로드
---

# Custom Document Loader

<figure><img src="../../../.gitbook/assets/image_custom_loader.png" alt="" width="271"><figcaption><p>Custom Document Loader 노드</p></figcaption></figure>

Custom Document Loader를 사용하면 JavaScript 함수를 작성하여 사용자 정의 방식으로 콘텐츠를 로드하고 Document로 변환할 수 있습니다. 이를 통해 기본 제공 loader로 지원되지 않는 데이터 소스와 형식을 처리할 수 있습니다.

이 모듈은 다음을 수행할 수 있는 유연한 커스텀 로더를 제공합니다:

* 커스텀 JavaScript 함수 정의
* 외부 API 호출 및 통합
* 복잡한 데이터 변환 로직
* Document 구조 커스터마이징
* Metadata 추출 및 처리
* 동적 콘텐츠 처리

## 입력

### 필수 파라미터

* **Custom Loader Code**: Document Loader를 구현하는 JavaScript 함수

### 선택적 파라미터

* **Additional Metadata**: 추가 metadata가 있는 JSON 객체
* **Function Parameters**: 커스텀 함수에 전달할 파라미터

## 출력

* **Document**: Metadata 및 pageContent를 포함하는 document 객체의 배열
* **Text**: Document의 pageContent에서 연결된 문자열

## 기능

* 완전한 커스터마이징 가능
* JavaScript 함수 작성
* 외부 API 통합
* 복잡한 데이터 처리
* 동적 콘텐츠 생성
* 오류 처리

## 예제 구조

커스텀 함수는 다음과 같은 구조를 따라야 합니다:

```javascript
async function loader(input) {
    // 로딩 로직 구현
    const documents = [];
    // Document 객체 생성
    return documents;
}
```

## 참고사항

* JavaScript 코드 문법 검증 필요
* 보안 고려사항 - 신뢰할 수 있는 코드만 실행
* API 자격증명은 환경 변수로 관리
* 오류 처리 및 예외 관리 필수
* 성능 및 타임아웃 고려
* Document 구조 일관성 유지
