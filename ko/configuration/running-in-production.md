# 프로덕션 환경에서 실행하기

## 모드

프로덕션 환경에서 실행할 때는 다음 설정으로 [Queue](running-flowise-using-queue.md) 모드를 사용하는 것을 강력히 권장합니다:

* 로드 밸런싱을 포함한 2개의 메인 서버, 각각 최소 4vCPU 8GB RAM
* 4개의 워커, 각각 최소 4vCPU 8GB RAM

트래픽과 볼륨에 따라 자동 스케일링을 설정할 수 있습니다.

## 데이터베이스

기본적으로 Flowise는 SQLite를 데이터베이스로 사용합니다. 그러나 대규모 실행 환경에서는 PostgreSQL을 사용하는 것이 권장됩니다.

## 스토리지

현재 Flowise는 [AWS S3](https://aws.amazon.com/s3/)를 지원하며, 더 많은 blob 스토리지 제공자를 지원할 계획이 있습니다. 이를 통해 파일과 로그를 로컬 파일 경로 대신 S3에 저장할 수 있습니다. [#for-storage](environment-variables.md#for-storage "mention")를 참조하세요.

## 암호화

Flowise는 암호화 키를 사용하여 OpenAI API 키와 같이 사용하는 자격증명을 암호화/복호화합니다. 프로덕션 환경에서는 더 나은 보안 제어와 키 로테이션을 위해 [AWS Secret Manager](https://aws.amazon.com/secrets-manager/)를 사용하는 것이 권장됩니다. [#for-credentials](environment-variables.md#for-credentials "mention")를 참조하세요.

## 속도 제한

클라우드/온프레미스에 배포할 때 대부분의 경우 인스턴스는 프록시/로드 밸런서 뒤에 있습니다. 요청의 IP 주소는 로드 밸런서/리버스 프록시의 IP일 수 있으므로, 속도 제한기가 사실상 전역적이 되어 제한에 도달하거나 `undefined`일 때 모든 요청을 차단할 수 있습니다. 올바른 `NUMBER_OF_PROXIES`를 설정하면 이 문제를 해결할 수 있습니다. [#rate-limit-setup](rate-limit.md#rate-limit-setup "mention")를 참조하세요.

## 부하 테스트

Artillery를 사용하여 배포된 Flowise 애플리케이션의 부하 테스트를 수행할 수 있습니다. 예시 스크립트는 [여기](https://github.com/FlowiseAI/Flowise/blob/main/artillery-load-test.yml)에서 찾을 수 있습니다.

## 보안

[#security-configuration](environment-variables.md#security-configuration "mention")를 참조하세요.