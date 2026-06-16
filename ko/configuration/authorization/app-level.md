---
description: Flowise 인스턴스에 대한 App 수준 접근 제어를 설정하는 방법을 알아봅니다
---

# 애플리케이션

***

## 이메일 및 비밀번호

v3.0.1부터 새로운 인증 방식이 도입되었습니다. Flowise는 보안 HTTP 전용(HTTP-only) 쿠키에 저장되는 JWT 토큰을 사용하는 [**Passport.js**](https://www.passportjs.org/)**기반 인증 시스템**을 사용합니다. 사용자가 로그인하면 시스템은 bcrypt 해시 비교를 통해 데이터베이스에 저장된 이메일/비밀번호를 검증한 후, 두 개의 JWT 토큰을 생성합니다. 하나는 수명이 짧은 액세스 토큰(기본 60분)이고, 다른 하나는 수명이 긴 리프레시 토큰(기본 90일)입니다. 이 토큰들은 보안 쿠키로 저장됩니다. 이후 요청에 대해 시스템은 쿠키에서 JWT를 추출하고, Passport의 JWT 전략을 사용하여 서명과 클레임을 검증하며, 사용자 세션이 여전히 존재하는지 확인합니다. 또한 액세스 토큰이 만료되면 자동 토큰 갱신을 지원하며, 설정에 따라 Redis 또는 데이터베이스 저장소를 사용하여 세션을 유지합니다.

기존에 [사용자 이름 및 비밀번호(더 이상 사용되지 않음)](app-level.md#username-and-password-deprecated)를 사용하던 사용자는 새로운 관리자 계정을 설정해야 합니다. 권한 없는 소유권 주장을 방지하기 위해, 먼저 `FLOWISE_USERNAME` 및 `FLOWISE_PASSWORD`로 설정된 기존 사용자 이름과 비밀번호를 사용하여 인증해야 합니다.

<figure><img src="../../.gitbook/assets/image (18) (1) (1).png" alt="" width="387"><figcaption></figcaption></figure>

다음 환경 변수를 변경할 수 있습니다.

### 애플리케이션 URL

* `APP_URL` - 호스팅된 Flowise 애플리케이션 URL입니다. 기본값은 `http://localhost:3000`입니다.

### JWT 환경 변수 설정

Flowise의 JWT 인증 매개변수를 설정하려면 다음 환경 변수를 변경할 수 있습니다.

* `JWT_AUTH_TOKEN_SECRET` - 액세스 토큰 서명에 사용되는 비밀 키입니다.
* `JWT_REFRESH_TOKEN_SECRET` - 리프레시 토큰용 비밀 키입니다(설정하지 않으면 인증 토큰 비밀 키를 기본값으로 사용).
* `JWT_TOKEN_EXPIRY_IN_MINUTES` - 액세스 토큰 수명입니다(기본값: 60분).
* `JWT_REFRESH_TOKEN_EXPIRY_IN_MINUTES` - 리프레시 토큰 수명입니다(기본값: 129,600분 또는 90일).
* `JWT_AUDIENCE` - 토큰 검증 대상(audience) 클레임입니다(기본값: 'AUDIENCE').
* `JWT_ISSUER` - 토큰 검증 발급자(issuer) 클레임입니다(기본값: 'ISSUER').
* `EXPRESS_SESSION_SECRET` - 세션 암호화 비밀 키입니다(기본값: 'flowise').
* `EXPIRE_AUTH_TOKENS_ON_RESTART` - 'true'로 설정하면 서버 재시작 시 모든 토큰을 무효화합니다(개발 시 유용).

### SMTP 이메일 설정

비밀번호 재설정 및 알림을 위한 이메일 기능을 활성화하려면 다음 변수를 설정합니다.

* `SMTP_HOST` - SMTP 서버의 호스트 이름입니다(예: `smtp.gmail.com`, `smtp.host.com`).
* `SMTP_PORT` - SMTP 연결에 사용되는 포트 번호입니다(일반적인 값: TLS는 `587`, SSL은 `465`, 암호화하지 않을 경우 `25`).
* `SMTP_USER` - SMTP 인증을 위한 사용자 이름입니다(일반적으로 이메일 주소).
* `SMTP_PASSWORD` - SMTP 인증을 위한 비밀번호 또는 앱 전용 비밀번호입니다.
* `SMTP_SECURE` - SSL/TLS 암호화를 사용하려면 `true`, 암호화하지 않으려면 `false`로 설정합니다.
* `ALLOW_UNAUTHORIZED_CERTS` - 자체 서명 인증서를 허용하려면 `true`로 설정합니다(프로덕션에서는 권장하지 않음).
* `SENDER_EMAIL` - 발신 이메일에 표시될 "보낸 사람" 이메일 주소입니다.

### 보안 및 토큰 설정

다음 변수는 인증 보안, 토큰 만료, 비밀번호 해싱을 제어합니다.

* `PASSWORD_RESET_TOKEN_EXPIRY_IN_MINS` - 비밀번호 재설정 토큰의 만료 시간입니다(기본값: 15분).
* `PASSWORD_SALT_HASH_ROUNDS` - 비밀번호 해싱을 위한 bcrypt salt 라운드 수입니다(기본값: 10, 값이 클수록 보안은 강화되지만 속도는 느려짐).
* `TOKEN_HASH_SECRET` - 토큰 및 민감한 데이터 해싱에 사용되는 비밀 키입니다(강력하고 무작위적인 문자열 사용).

### 보안 모범 사례

{% hint style="warning" %}
사용자 고유의 JWT 및 Secret 토큰 환경 변수를 설정할 것을 권장합니다. 그렇지 않으면 기본값이 사용되어, 공격자가 유효한 토큰을 위조하고 사용자를 사칭할 가능성이 높아질 수 있습니다.
{% endhint %}

* `TOKEN_HASH_SECRET`에는 강력하고 고유한 값을 사용하고 안전하게 보관합니다.
* 프로덕션 환경에서는 `SMTP_SECURE=true` 및 `ALLOW_UNAUTHORIZED_CERTS=false`를 사용합니다.
* 보안 요구사항에 따라 적절한 토큰 만료 시간을 설정합니다.
* 프로덕션 환경에서 보안을 강화하려면 더 높은 `PASSWORD_SALT_HASH_ROUNDS` 값(12~15)을 사용합니다.

## 사용자 이름 및 비밀번호(더 이상 사용되지 않음)

App 수준 인증은 사용자 이름과 비밀번호로 Flowise 인스턴스를 보호합니다. 이를 통해 온라인에 배포되었을 때 누구나 앱에 접근하는 것을 방지합니다.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 사용자 이름 및 비밀번호 설정 방법

#### Npm

1. Flowise 설치

__CODE_BLOCK_0__

2. 사용자 이름 및 비밀번호로 Flowise 시작

__CODE_BLOCK_1__

3. [http://localhost:3000](http://localhost:3000) 열기

#### Docker

1. `docker` 폴더로 이동

__CODE_BLOCK_2__

2. `.env` 파일을 만들고 `PORT`, `FLOWISE_USERNAME`, `FLOWISE_PASSWORD`를 지정

__CODE_BLOCK_3__

3. `docker-compose.yml` 파일에 `FLOWISE_USERNAME` 및 `FLOWISE_PASSWORD` 전달:

__CODE_BLOCK_4__

4. `docker compose up -d`
5. [http://localhost:3000](http://localhost:3000) 열기
6. `docker compose stop`으로 컨테이너를 종료할 수 있습니다.

#### Git clone

App 수준 인증을 활성화하려면 `packages/server`의 `.env` 파일에 `FLOWISE_USERNAME` 및 `FLOWISE_PASSWORD`를 추가합니다.

__CODE_BLOCK_5__
