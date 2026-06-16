---
description: AWS에 Flowise를 배포하는 방법을 알아봅니다
---

# AWS

***

## 사전 요구사항

이 작업에는 AWS의 작동 방식에 대한 기본적인 이해가 필요합니다.

Flowise를 AWS에 배포하는 방법으로는 두 가지 옵션이 있습니다:

* [CloudFormation을 사용하여 ECS에 배포](aws.md#deploy-on-ecs-using-cloudformation)
* [EC2 인스턴스를 수동으로 구성](aws.md#launch-ec2-instance)

## CloudFormation을 사용하여 ECS에 배포

CloudFormation 템플릿은 여기에서 확인할 수 있습니다: [https://gist.github.com/MrHertal/549b31a18e350b69c7200ae8d26ed691](https://gist.github.com/MrHertal/549b31a18e350b69c7200ae8d26ed691)

이 템플릿은 ELB를 통해 노출되는 ECS 클러스터에 Flowise를 배포합니다.

이 템플릿은 다음 참조 아키텍처에서 영감을 받았습니다: [https://github.com/aws-samples/ecs-refarch-cloudformation](https://github.com/aws-samples/ecs-refarch-cloudformation)

Flowise 이미지 버전, 환경 변수 등을 조정하려면 이 템플릿을 자유롭게 편집하세요.

[AWS CLI](https://aws.amazon.com/fr/cli/)를 사용하여 Flowise를 배포하는 명령어 예시입니다:

```bash
aws cloudformation create-stack --stack-name flowise --template-body file://flowise-cloudformation.yml --capabilities CAPABILITY_IAM
```

배포가 완료되면 Flowise 애플리케이션의 URL은 CloudFormation 스택 출력(outputs)에서 확인할 수 있습니다.

## Terraform을 사용하여 ECS에 배포

Terraform 파일(`variables.tf`, `main.tf`)은 이 GitHub 저장소에서 확인할 수 있습니다: [terraform-flowise-setup](https://github.com/huiseo/terraform-flowise-setup/tree/main).

이 설정은 Application Load Balancer(ALB)를 통해 노출되는 ECS 클러스터에 Flowise를 배포합니다. ECS 배포에 대한 AWS 모범 사례를 기반으로 합니다.

Terraform 템플릿을 수정하여 다음 항목을 조정할 수 있습니다:

* Flowise 이미지 버전
* 환경 변수
* 리소스 구성(CPU, 메모리 등)

### 배포 명령어 예시:

1. **Terraform 초기화:**

```bash
terraform init
terraform apply
terraform destroy
```

## EC2 인스턴스 시작

1. EC2 대시보드에서 **Launch Instance**를 클릭합니다

<figure><img src="../../.gitbook/assets/image (19) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

2. 아래로 스크롤하여 키 페어가 없는 경우 **Create new key pair**를 클릭합니다

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

3. 원하는 키 페어 이름을 입력합니다. Windows의 경우 `.ppk`와 PuTTY를 사용하여 인스턴스에 연결합니다. Mac과 Linux의 경우 `.pem`과 OpenSSH를 사용합니다

<figure><img src="../../.gitbook/assets/image (15) (2) (1).png" alt="" width="370"><figcaption></figcaption></figure>

4. **Create key pair**를 클릭하고 `.ppk` 파일을 저장할 위치 경로를 선택합니다
5. 왼쪽 사이드바를 열고 **Security Groups**에서 새 탭을 엽니다. 그런 다음 **Create security group**을 클릭합니다

<figure><img src="../../.gitbook/assets/image (20) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. 원하는 보안 그룹 이름과 설명을 입력합니다. 다음으로 Inbound Rules에 아래 항목을 추가하고 **Create security group**을 클릭합니다

<figure><img src="../../.gitbook/assets/image (12) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

7. 첫 번째 탭(EC2 Launch an instance)으로 돌아가 **Network settings**까지 아래로 스크롤합니다. 방금 생성한 보안 그룹을 선택합니다

<figure><img src="../../.gitbook/assets/image (7) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

8. **Launch instance**를 클릭합니다. EC2 대시보드로 돌아가면 몇 분 후 새 인스턴스가 실행 중인 것을 확인할 수 있습니다 [🎉](https://emojipedia.org/party-popper/)

<figure><img src="../../.gitbook/assets/image (17) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## 인스턴스에 연결하는 방법 (Windows)

1. Windows의 경우 PuTTY를 사용합니다. [여기](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)에서 다운로드할 수 있습니다.
2. PuTTY를 열고 **HostName**에 인스턴스의 Public IPv4 DNS 이름을 입력합니다

<figure><img src="../../.gitbook/assets/image (9) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. PuTTY Configuration의 왼쪽 사이드바에서 **SSH**를 펼치고 **Auth**를 클릭합니다. Browse를 클릭하고 앞서 다운로드한 `.ppk` 파일을 선택합니다.

<figure><img src="../../.gitbook/assets/image (23) (1) (1).png" alt="" width="296"><figcaption></figcaption></figure>

4. **Open**을 클릭하고 팝업 메시지에서 **Accept**를 클릭합니다

<figure><img src="../../.gitbook/assets/image (18) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

5. 그런 다음 `ec2-user`로 로그인합니다

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

6. 이제 EC2 인스턴스에 연결되었습니다

## 인스턴스에 연결하는 방법 (Mac 및 Linux)

1. Mac/Linux에서 터미널 애플리케이션을 엽니다.
2. _(선택 사항)_ 개인 키 파일에 대한 접근을 제한하도록 권한을 설정합니다:

```bash
chmod 400 /path/to/mykey.pem
```

3. `ssh` 명령어를 사용하여 EC2 인스턴스에 연결합니다. 사용자 이름(`ec2-user`), Public IPv4 DNS, 그리고 `.pem` 파일의 경로를 지정합니다.

```bash
ssh -i /Users/username/Documents/mykey.pem ec2-user@ec2-123-45-678-910.compute-1.amazonaws.com
```

4. Enter를 누르고, 모든 설정이 올바르게 구성되었다면 EC2 인스턴스에 SSH 연결을 성공적으로 설정할 수 있습니다

## Docker 설치

1. yum 명령어를 사용하여 대기 중인 업데이트를 적용합니다:

```bash
sudo yum update
```

2. Docker 패키지를 검색합니다:

```bash
sudo yum search docker
```

3. 버전 정보를 확인합니다:

```bash
sudo yum info docker
```

4. Docker를 설치하려면 다음을 실행합니다:

```bash
sudo yum install docker
```

5. 기본 ec2-user에 그룹 멤버십을 추가하여 sudo 명령어를 사용하지 않고도 모든 docker 명령어를 실행할 수 있도록 합니다:

```bash
sudo usermod -a -G docker ec2-user
id ec2-user
newgrp docker
```

6. docker-compose를 설치합니다:

```bash
sudo yum install docker-compose-plugin
```

7. AMI 부팅 시 docker 서비스를 활성화합니다:

```bash
sudo systemctl enable docker.service
```

8. Docker 서비스를 시작합니다:

```bash
sudo systemctl start docker.service
```

## Git 설치

```bash
sudo yum install git -y
```

## 설정

1. 저장소를 복제합니다

```bash
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

<figure><img src="../../.gitbook/assets/image (13) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

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

7. 이제 애플리케이션이 Public IPv4 DNS의 3000번 포트에서 준비되었습니다:

```
http://ec2-123-456-789.compute-1.amazonaws.com:3000
```

8. 다음 명령어로 앱을 종료할 수 있습니다:

```bash
docker compose stop
```

9. 다음 명령어로 최신 이미지를 가져올 수 있습니다:

```bash
docker pull flowiseai/flowise
```

또는:

```bash
docker-compose pull
docker-compose up --build -d
```

## NGINX 사용

URL에서 :3000을 제거하고 사용자 지정 도메인을 사용하려면 NGINX를 사용하여 80번 포트를 3000번 포트로 리버스 프록시할 수 있습니다. 그러면 사용자가 도메인을 사용하여 앱을 열 수 있습니다. 예: `http://yourdomain.com`.

1. ```bash
   sudo yum install nginx
   ```
2. ```bash
   nginx -v
   ```
3. <pre class="language-bash"><code class="lang-bash"><strong>sudo systemctl start nginx
   </strong></code></pre>
4. <pre class="language-bash"><code class="lang-bash"><strong>sudo nano /etc/nginx/conf.d/flowise.conf
   </strong></code></pre>
5. 다음 내용을 복사하여 붙여넣고 본인의 도메인으로 변경합니다:

```shell
server {
    listen 80;
    listen [::]:80;
    server_name yourdomain.com; #Example: demo.flowiseai.com
    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

`Ctrl + X`를 눌러 종료하고, `Y`를 눌러 파일을 저장합니다

6. ```bash
   sudo systemctl restart nginx
   ```
7. DNS 공급자로 이동하여 새 A 레코드를 추가합니다. Name은 본인의 도메인 이름이 되고, Value는 EC2 인스턴스의 Public IPv4 주소가 됩니다

<figure><img src="../../.gitbook/assets/image (3) (2).png" alt="" width="367"><figcaption></figcaption></figure>

6. 이제 앱을 열 수 있습니다: `http://yourdomain.com`.

### HTTPS를 위한 Certbot 설치

앱에 `https://yourdomain.com`을 적용하려면 다음과 같이 진행합니다:

1. Certbot을 설치하고 NGINX에서 HTTPS를 활성화하기 위해 Python을 사용합니다. 따라서 먼저 가상 환경을 설정하겠습니다:

```bash
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

5. 인증서 생성 마법사를 따라 진행하면 `https://yourdomain.com` 주소를 사용하여 HTTPS로 EC2 인스턴스에 접근할 수 있습니다

## 자동 갱신 설정

Certbot이 인증서를 자동으로 갱신할 수 있도록 하려면, 다음 명령어를 실행하여 cron 작업을 추가하는 것으로 충분합니다:

```bash
echo "0 0,12 * * * root /opt/certbot/bin/python -c 'import random; import time; time.sleep(random.random() * 3600)' && sudo certbot renew -q" | sudo tee -a /etc/crontab > /dev/null
```

## 축하합니다!

도메인에 SSL 인증서가 적용된 EC2 인스턴스에 Flowise 앱을 성공적으로 설정했습니다 [🥳](https://emojipedia.org/partying-face/)
