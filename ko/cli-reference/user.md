# 사용자

## 사용자 이메일 목록 조회

이 명령을 사용하면 시스템에 등록된 모든 사용자 이메일을 조회할 수 있습니다.

### 로컬 사용

```bash
pnpm user
```

또는 npm을 사용하는 경우

```bash
npx flowise user
```

### Docker 사용

Flowise를 Docker 컨테이너에서 실행 중인 경우 다음 명령을 사용합니다.

```bash
docker exec -it FLOWISE_CONTAINER_NAME pnpm user
```

`FLOWISE_CONTAINER_NAME`을 실제 Flowise 컨테이너 이름으로 바꿉니다.

## 사용자 비밀번호 재설정

이 명령을 사용하면 사용자의 비밀번호를 재설정할 수 있습니다.

### 로컬 사용

```bash
pnpm user --email "admin@admin.com" --password "myPassword1!"
```

또는 npm을 사용하는 경우

```
npx flowise user --email "admin@admin.com" --password "myPassword1!"
```

### Docker 사용

Flowise를 Docker 컨테이너에서 실행 중인 경우 다음 명령을 사용합니다.

```bash
docker exec -it FLOWISE_CONTAINER_NAME pnpm user --email "admin@admin.com" --password "myPassword1!"
```

`FLOWISE_CONTAINER_NAME`을 실제 Flowise 컨테이너 이름으로 바꿉니다.

### 파라미터

* `--email`: 비밀번호를 재설정할 사용자의 이메일 주소
* `--password`: 사용자에게 설정할 새 비밀번호
