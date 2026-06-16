---
description: Hugging Face에 Flowise를 배포하는 방법을 알아봅니다
---

# Hugging Face

***

### 새 Space 생성

1. [Hugging Face](https://huggingface.co/login)에 로그인합니다.
2. 원하는 이름으로 [새 Space](https://huggingface.co/new-space)를 생성하기 시작합니다.
3. **Space SDK**로 **Docker**를 선택하고, Docker 템플릿으로 **Blank**을 선택합니다.
4. **Space hardware**로 **CPU basic ∙ 2 vCPU ∙ 16GB ∙ FREE**를 선택합니다.
5. **Create Space**를 클릭합니다.

### 환경 변수 설정

1. 새로 만든 space의 **Settings**로 이동하여 **Variables and Secrets** 섹션을 찾습니다.
2. **New variable**을 클릭하고 이름을 `PORT`, 값을 `7860`으로 추가합니다.
3. **Save**를 클릭합니다.
4. _(선택 사항)_ **New secret**을 클릭합니다.
5. _(선택 사항)_ 데이터베이스 자격 증명, 파일 경로 등 환경 변수를 입력합니다. 유효한 필드는 [여기](https://github.com/FlowiseAI/Flowise/blob/main/docker/.env.example)의 `.env.example`에서 확인할 수 있습니다.

### Dockerfile 생성

1. files 탭에서 _**+ Add file**_ 버튼을 클릭한 후 **Create a new file**을 클릭합니다(원한다면 Upload files를 사용해도 됩니다).
2. **Dockerfile**이라는 이름의 파일을 생성하고 다음 내용을 붙여 넣습니다:

```Dockerfile
FROM node:20-alpine
USER root

# Arguments that can be passed at build time
ARG FLOWISE_PATH=/usr/local/lib/node_modules/flowise
ARG BASE_PATH=/root/.flowise
ARG DATABASE_PATH=$BASE_PATH
ARG SECRETKEY_PATH=$BASE_PATH
ARG LOG_PATH=$BASE_PATH/logs
ARG BLOB_STORAGE_PATH=$BASE_PATH/storage

# Install dependencies
RUN apk add --no-cache git python3 py3-pip make g++ build-base cairo-dev pango-dev chromium

ENV PUPPETEER_SKIP_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

# Install Flowise globally
RUN npm install -g flowise

# Configure Flowise directories using the ARG
RUN mkdir -p $LOG_PATH $FLOWISE_PATH/uploads && chmod -R 777 $LOG_PATH $FLOWISE_PATH

WORKDIR /data

CMD ["npx", "flowise", "start"]
```

3. **Commit file to `main`**을 클릭하면 앱 빌드가 시작됩니다.

### 완료 🎉

빌드가 완료되면 **App** 탭을 클릭하여 실행 중인 앱을 확인할 수 있습니다.
