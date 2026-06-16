---
description: Replit에 Flowise를 배포하는 방법을 알아봅니다
---

# Replit

***

1. [Replit](https://replit.com/~)에 로그인합니다.
2. 새 **Repl**을 생성합니다. 템플릿으로 **Node.js**를 선택하고 원하는 **Title**을 입력합니다.

<figure><img src="../../.gitbook/assets/image (18) (1) (2) (1).png" alt="" width="551"><figcaption></figcaption></figure>

3. 새 Repl이 생성되면 왼쪽 사이드바에서 Secret을 클릭합니다:

<figure><img src="../../.gitbook/assets/image (2) (4) (1).png" alt="" width="219"><figcaption></figcaption></figure>

4. Puppeteer 및 Playwright 라이브러리의 Chromium 다운로드를 건너뛰기 위해 3개의 Secret을 생성합니다.

<table><thead><tr><th width="403">Secrets</th><th>Value</th></tr></thead><tbody><tr><td>PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD</td><td>1</td></tr><tr><td>PUPPETEER_SKIP_DOWNLOAD</td><td>true</td></tr><tr><td>PUPPETEER_SKIP_CHROMIUM_DOWNLOAD</td><td>true</td></tr></tbody></table>

<figure><img src="../../.gitbook/assets/image (5) (3).png" alt="" width="535"><figcaption></figcaption></figure>

5. 이제 Shell 탭으로 전환할 수 있습니다.

<figure><img src="../../.gitbook/assets/image (13) (2) (1).png" alt="" width="539"><figcaption></figcaption></figure>

6. Shell 터미널 창에 `npm install -g flowise`를 입력합니다. node 버전 호환성 오류가 발생하는 경우 다음 명령을 사용하세요: `yarn global add flowise --ignore-engines`

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="530"><figcaption></figcaption></figure>

7. 그런 다음 `npx flowise start`를 실행합니다.

<figure><img src="../../.gitbook/assets/image (17) (1) (2).png" alt="" width="533"><figcaption></figcaption></figure>

8. 이제 Replit에서 Flowise를 확인할 수 있습니다!

<figure><img src="../../.gitbook/assets/image (15) (3).png" alt="" width="545"><figcaption></figcaption></figure>

9. 이제 로그인 페이지가 표시됩니다. 설정한 사용자 이름과 비밀번호로 로그인하면 됩니다.

<figure><img src="../../.gitbook/assets/image (12) (2) (1).png" alt=""><figcaption></figcaption></figure>
