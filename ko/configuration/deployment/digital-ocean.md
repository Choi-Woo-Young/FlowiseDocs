---
description: Digital Ocean에 Flowise를 배포하는 방법을 알아봅니다
---

# Digital Ocean

***

## Droplet 생성

이 섹션에서는 Droplet을 생성합니다. 자세한 내용은 [공식 가이드](https://docs.digitalocean.com/products/droplets/quickstart/)를 참조하세요.

1. 먼저 드롭다운에서 **Droplets**를 클릭합니다

<figure><img src="../../.gitbook/assets/image (15) (2) (2).png" alt=""><figcaption></figcaption></figure>

2. Data Region과 Basic $6/mo Droplet 유형을 선택합니다

<figure><img src="../../.gitbook/assets/image (17) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. 인증 방법(Authentication Method)을 선택합니다. 이 예시에서는 Password를 사용합니다

<figure><img src="../../.gitbook/assets/image (5) (2).png" alt=""><figcaption></figcaption></figure>

4. 잠시 후 Droplet이 성공적으로 생성된 것을 확인할 수 있습니다

<figure><img src="../../.gitbook/assets/image (7) (2) (1).png" alt=""><figcaption></figcaption></figure>

## Droplet에 연결하는 방법

Windows의 경우 이 [가이드](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/putty/)를 따르세요.

Mac/Linux의 경우 이 [가이드](https://docs.digitalocean.com/products/droplets/how-to/connect-with-ssh/openssh/)를 따르세요.

## Docker 설치

1. ```
   curl -fsSL https://get.docker.com -o get-docker.sh
   ```
2. ```
   sudo sh get-docker.sh
   ```
3. docker-compose를 설치합니다:

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

4. 권한을 설정합니다:

```
sudo chmod +x /usr/local/bin/docker-compose
```

## 설정

1. 저장소를 복제합니다

```
git clone https://github.com/FlowiseAI/Flowise.git
```

2. docker 폴더로 이동합니다

```bash
cd Flowise && cd docker
```

3. `.env` 파일을 생성합니다. 원하는 편집기를 사용할 수 있습니다. 여기서는 `nano`를 사용하겠습니다

```bash
nano .env
```

<figure><img src="../../.gitbook/assets/image (10) (2) (1).png" alt="" width="375"><figcaption></figcaption></figure>

4. 환경 변수를 지정합니다:

```sh
PORT=3000
DATABASE_PATH=/root/.flowise
SECRETKEY_PATH=/root/.flowise
LOG_PATH=/root/.flowise/logs
BLOB_STORAGE_PATH=/root/.flowise/storage
```

5. 그런 다음 `Ctrl + X`를 눌러 종료하고, `Y`를 눌러 파일을 저장합니다
6. docker compose를 실행합니다

```bash
docker compose up -d
```

7. 그러면 앱을 볼 수 있습니다: "Your Public IPv4 DNS":3000. 예: `176.63.19.226:3000`
8. 다음 명령어로 앱을 종료할 수 있습니다:

```bash
docker compose stop
```

9. 다음 명령어로 최신 이미지를 가져올 수 있습니다:

```bash
docker pull flowiseai/flowise
```

## 리버스 프록시 및 SSL 추가

리버스 프록시는 애플리케이션 서버를 인터넷에 노출하는 권장 방법입니다. 이를 통해 서버 IP와 포트 번호 대신 URL만으로 Droplet에 연결할 수 있습니다. 이는 애플리케이션 서버를 직접적인 인터넷 접근으로부터 격리하는 보안 이점, 방화벽 보호를 중앙 집중화할 수 있는 기능, 서비스 거부 공격과 같은 일반적인 위협에 대한 공격 면 최소화, 그리고 무엇보다 우리의 목적에서 중요한 SSL/TLS 암호화를 한 곳에서 종료할 수 있는 기능을 제공합니다.

> Droplet에 SSL이 없으면 임베드 가능한 위젯과 API 엔드포인트가 최신 브라우저에서 접근 불가능해집니다. 이는 브라우저가 HTTP 대신 HTTPS를 선호하며 사용을 중단하기 시작했고, HTTPS로 로드된 페이지에서의 HTTP 요청을 차단하기 때문입니다.

### 1단계 — Nginx 설치

1. Nginx는 기본 저장소를 통해 apt로 설치할 수 있습니다. 저장소 인덱스를 업데이트한 다음 Nginx를 설치합니다:

```bash
sudo apt update
sudo apt install nginx
```

> 설치를 확인하려면 Y를 누릅니다. 서비스를 재시작하라는 메시지가 나타나면 ENTER를 눌러 기본값을 수락합니다.

2. 방화벽을 통해 Nginx에 대한 접근을 허용해야 합니다. 초기 서버 사전 요구사항에 따라 서버를 설정했다면 ufw로 다음 규칙을 추가합니다:

```bash
sudo ufw allow 'Nginx HTTP'
```

3. 이제 Nginx가 실행 중인지 확인할 수 있습니다:

```bash
systemctl status nginx
```

출력:

```bash
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2022-08-29 06:52:46 UTC; 39min ago
       Docs: man:nginx(8)
   Main PID: 9919 (nginx)
      Tasks: 2 (limit: 2327)
     Memory: 2.9M
        CPU: 50ms
     CGroup: /system.slice/nginx.service
             ├─9919 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             └─9920 "nginx: worker process
```

다음으로 도메인과 앱 서버 프록시를 포함한 사용자 지정 서버 블록을 추가합니다.

### 2단계 — 서버 블록 + DNS 레코드 구성

기본 구성을 직접 편집하는 대신 새 서버 블록 추가를 위한 사용자 지정 구성 파일을 생성하는 것이 권장되는 방식입니다.

1. nano 또는 선호하는 텍스트 편집기를 사용하여 새 Nginx 구성 파일을 생성하고 엽니다:

```bash
sudo nano /etc/nginx/sites-available/your_domain
```

2. 새 파일에 다음을 삽입하되, `your_domain`을 본인의 도메인 이름으로 교체합니다:

```
server {
    listen 80;
    listen [::]:80;
    server_name your_domain; #Example: demo.flowiseai.com
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_cache_bypass $http_upgrade;
    }
}
```

3. 저장하고 종료합니다. `nano`의 경우 `CTRL+O`를 누른 다음 `CTRL+X`를 눌러 수행할 수 있습니다.
4. 다음으로 Nginx가 시작 시 읽는 sites-enabled 디렉터리에 이 파일에 대한 링크를 생성하여 이 구성 파일을 활성화합니다. 다시 한 번 `your_domain`을 본인의 도메인 이름으로 교체합니다:

```bash
sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/
```

5. 이제 구성 파일에 구문 오류가 있는지 테스트할 수 있습니다:

```bash
sudo nginx -t
```

6. 보고된 문제가 없으면 변경 사항을 적용하기 위해 Nginx를 재시작합니다:

```bash
sudo systemctl restart nginx
```

7. DNS 공급자로 이동하여 새 A 레코드를 추가합니다. Name은 본인의 도메인 이름이 되고, Value는 Droplet의 Public IPv4 주소가 됩니다

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt="" width="367"><figcaption></figcaption></figure>

이제 Nginx가 애플리케이션 서버의 리버스 프록시로 구성되었습니다. 이제 앱을 열 수 있습니다: http://yourdomain.com.

### 3단계 — HTTPS(SSL)를 위한 Certbot 설치

https://yourdomain.com과 같이 Droplet에 보안 `https` 연결을 추가하려면 다음을 수행해야 합니다:

1. Certbot을 설치하고 NGINX에서 HTTPS를 활성화하기 위해 Python을 사용합니다. 따라서 먼저 가상 환경을 설정하겠습니다:

```bash
apt install python3.10-venv
sudo python3 -m venv /opt/certbot/
sudo /opt/certbot/bin/pip install --upgrade pip
```

2. 그런 다음 다음 명령어를 실행하여 Certbot을 설치합니다:

```bash
sudo /opt/certbot/bin/pip install certbot certbot-nginx
```

3. 이제 `certbot` 명령어를 실행할 수 있도록 다음 명령어를 실행합니다:

```bash
sudo ln -s /opt/certbot/bin/certbot /usr/bin/certbot
```

4. 마지막으로 다음 명령어를 실행하여 인증서를 발급받고 Certbot이 NGINX 구성을 자동으로 수정하여 HTTPS를 활성화하도록 합니다:

```bash
sudo certbot --nginx
```

5. 인증서 생성 마법사를 따라 진행하면 https://yourdomain.com 주소를 사용하여 HTTPS로 Droplet에 접근할 수 있습니다

### 자동 갱신 설정

Certbot이 인증서를 자동으로 갱신할 수 있도록 하려면, 다음 명령어를 실행하여 cron 작업을 추가하는 것으로 충분합니다:

```bash
echo "0 0,12 * * * root /opt/certbot/bin/python -c 'import random; import time; time.sleep(random.random() * 3600)' && sudo certbot renew -q" | sudo tee -a /etc/crontab > /dev/null
```

## 축하합니다!

도메인에 SSL 인증서가 적용된 Droplet에 Flowise를 성공적으로 설정했습니다 [🥳](https://emojipedia.org/partying-face/)

## Digital Ocean에서 Flowise를 업데이트하는 단계

1. Flowise를 설치한 디렉터리로 이동합니다

```bash
cd Flowise/docker
```

2. docker 이미지를 중지하고 제거합니다

참고: 데이터베이스가 별도의 폴더에 저장되므로 이 작업은 플로우를 삭제하지 않습니다

```bash
sudo docker compose stop
sudo docker compose rm
```

3. 최신 Flowise 이미지를 가져옵니다

최신 버전 릴리스는 [여기](https://github.com/FlowiseAI/Flowise/releases)에서 확인할 수 있습니다

```bash
docker pull flowiseai/flowise
```

4. docker를 시작합니다

```bash
docker compose up -d
```
