# 시작하기

***

## 클라우드

자체 호스팅은 인스턴스 설정, 데이터베이스 백업, 업데이트 유지 관리에 더 많은 기술적 기술이 필요합니다. 서버 관리 경험이 없거나 단순히 웹 애플리케이션을 사용하고 싶으신 경우 [Flowise 클라우드](https://cloud.flowiseai.com)를 사용하시기를 권장합니다.

## 빠른 시작

{% hint style="info" %}
필수 조건: 컴퓨터에 [NodeJS](https://nodejs.org/en/download)가 설치되어 있는지 확인합니다. Node `v18.15.0` 또는 `v20` 이상 버전이 지원됩니다.
{% endhint %}

NPM을 사용하여 Flowise를 로컬로 설치합니다.

1. Flowise 설치:

```bash
npm install -g flowise
```

특정 버전을 설치할 수도 있습니다. 사용 가능한 [버전](https://www.npmjs.com/package/flowise?activeTab=versions)을 참고합니다.

```
npm install -g flowise@x.x.x
```

2. Flowise 시작:

```bash
npx flowise start
```

3. 열기: [http://localhost:3000](http://localhost:3000)

***

## Docker

Flowise를 Docker로 배포하는 두 가지 방법이 있습니다. 먼저 프로젝트를 git clone합니다: [https://github.com/FlowiseAI/Flowise](https://github.com/FlowiseAI/Flowise)

### Docker Compose

1. 프로젝트 루트의 `docker 폴더`로 이동합니다.
2. `.env.example` 파일을 복사하여 `.env`라는 이름의 파일로 붙여넣습니다.
3. 다음 명령을 실행합니다:

```bash
docker compose up -d
```

4. 열기: [http://localhost:3000](http://localhost:3000)
5. 다음 명령을 실행하여 컨테이너를 종료할 수 있습니다:

```bash
docker compose stop
```

### Docker 이미지

1. 이미지를 빌드합니다:

```bash
docker build --no-cache -t flowise .
```

2. 이미지를 실행합니다:

```bash
docker run -d --name flowise -p 3000:3000 flowise
```

3. 이미지를 중지합니다:

```bash
docker stop flowise
```

***

## 개발자용

Flowise는 단일 모노 레포지토리에 4개의 서로 다른 모듈을 가지고 있습니다:

* **Server**: API 로직을 제공하는 Node 백엔드
* **UI**: React 프론트엔드
* **Components**: 통합 컴포넌트
* **Api Documentation**: Flowise API의 Swagger 스펙

### 필수 조건

[PNPM](https://pnpm.io/installation)을 설치합니다.

```bash
npm i -g pnpm
```

### 설정 1

PNPM을 사용한 간단한 설정:

1. 리포지토리 복제

```bash
git clone https://github.com/FlowiseAI/Flowise.git
```

2. 리포지토리 폴더로 이동

```bash
cd Flowise
```

3. 모든 모듈의 모든 의존성을 설치합니다:

```bash
pnpm install
```

4. 코드를 빌드합니다:

```bash
pnpm build
```

[http://localhost:3000](http://localhost:3000)에서 앱을 시작합니다

```bash
pnpm start
```

### 설정 2

프로젝트 기여자를 위한 단계별 설정:

1. 공식 [Flowise Github 리포지토리](https://github.com/FlowiseAI/Flowise)를 포크합니다
2. 포크한 리포지토리를 복제합니다
3. 새 브랜치를 생성합니다. [가이드](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository)를 참고합니다. 네이밍 컨벤션:
   * 기능 브랜치의 경우: `feature/<Your New Feature>`
   * 버그 수정 브랜치의 경우: `bugfix/<Your New Bugfix>`.
4. 방금 생성한 브랜치로 전환합니다
5. 리포지토리 폴더로 이동합니다:

```bash
cd Flowise
```

6. 모든 모듈의 모든 의존성을 설치합니다:

```bash
pnpm install
```

7. 코드를 빌드합니다:

```bash
pnpm build
```

8. [http://localhost:3000](http://localhost:3000)에서 앱을 시작합니다

```bash
pnpm start
```

9. 개발 빌드의 경우:

* `packages/ui`에서 `.env` 파일을 생성하고 `PORT`를 지정합니다 (`.env.example` 참고)
* `packages/server`에서 `.env` 파일을 생성하고 `PORT`를 지정합니다 (`.env.example` 참고)

```bash
pnpm dev
```

* `packages/ui` 또는 `packages/server`에서 변경한 모든 내용은 [http://localhost:8080](http://localhost:8080/)에 반영됩니다
* `packages/components`에서 변경한 경우 변경 사항을 선택하려면 다시 빌드해야 합니다
*   모든 변경을 완료한 후 다음을 실행합니다:

    ```bash
    pnpm build
    ```

    그리고

    ```bash
    pnpm start
    ```

    프로덕션에서 모든 것이 올바르게 작동하는지 확인합니다.

***

## 엔터프라이즈용

앱을 시작하기 전에 엔터프라이즈 사용자는 `.env` 파일의 엔터프라이즈 파라미터 값을 입력해야 합니다. 필요한 변경 사항에 대해 `.env.example`을 참고합니다.

다음 환경 변수 값에 대해 support@flowiseai.com으로 연락합니다:

```
LICENSE_URL
FLOWISE_EE_LICENSE_KEY
```

***

## 더 알아보기

이 비디오 튜토리얼에서 Leon은 Flowise를 소개하고 로컬 컴퓨터에 설정하는 방법을 설명합니다.

{% embed url="https://youtu.be/nqAK_L66sIQ" %}

## 커뮤니티 가이드

* [Introduction to \[Practical\] Building LLM Applications with Flowise / LangChain](https://volcano-ice-cd6.notion.site/Introduction-to-Practical-Building-LLM-Applications-with-Flowise-LangChain-03d6d75bfd20495d96dfdae964bea5a5)
* [Flowise / LangChainによるLLMアプリケーション構築\[実践\]入門](https://volcano-ice-cd6.notion.site/Flowise-LangChain-LLM-e106bb0f7e2241379aad8fa428ee064a)
