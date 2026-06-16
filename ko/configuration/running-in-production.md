# 프로덕션에서 실행

## 모드

프로덕션에서 실행할 때 다음 설정으로 [Queue](running-flowise-using-queue.md) 모드를 사용하는 것을 권장합니다:

* 4vCPU 8GB RAM부터 시작하는 로드 밸런싱을 갖춘 2개의 주 서버
* 4vCPU 8GB RAM부터 시작하는 4개의 워커

트래픽 및 볼륨에 따라 자동 스케일링을 구성할 수 있습니다.

## 데이터베이스

기본적으로 Flowise는 SQLite를 데이터베이스로 사용합니다. 그러나 대규모로 실행할 때는 PostgreSQL을 사용하는 것이 좋습니다.

## 저장소

현재 Flowise는 [AWS S3](https://aws.amazon.com/s3/)만 지원하며 더 많은 블롭 저장소 제공업체를 지원할 계획입니다. 이를 통해 파일과 로그를 로컬 파일 경로 대신 S3에 저장할 수 있습니다. [#for-storage](environment-variables.md#for-storage "mention") 참조

## 암호화

Flowise는 OpenAI API 키와 같이 사용하는 자격 증명을 암호화/복호화하기 위해 암호화 키를 사용합니다. [AWS Secret Manager](https://aws.amazon.com/secrets-manager/)를 프로덕션에서 더 나은 보안 제어 및 키 로테이션을 위해 사용하는 것이 좋습니다. [#for-credentials](environment-variables.md#for-credentials "mention") 참조

## 속도 제한

클라우드/온프레미스에 배포할 때 대부분의 경우 인스턴스가 프록시/로드 밸런서 뒤에 있습니다. 요청의 IP 주소는 로드 밸런서/리버스 프록시의 IP일 수 있으므로 속도 제한기가 사실상 전역이 되고 제한에 도달하거나 `undefined`일 때 모든 요청을 차단합니다. 올바른 `NUMBER_OF_PROXIES`를 설정하면 이 문제를 해결할 수 있습니다. [#rate-limit-setup](rate-limit.md#rate-limit-setup "mention") 참조

## 로드 테스트

Artillery를 사용하여 배포된 Flowise 애플리케이션을 로드 테스트할 수 있습니다. 예제 스크립트는 [여기](https://github.com/FlowiseAI/Flowise/blob/main/artillery-load-test.yml)에서 찾을 수 있습니다.

## 보안

[#security-configuration](environment-variables.md#security-configuration "mention") 참조
