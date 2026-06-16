---
description: Railway에 Flowise를 배포하는 방법을 알아봅니다
---

# Railway

***

1. 다음의 사전 구성된 [템플릿](https://railway.app/template/pn4G8S?referralCode=WVNPD9)을 클릭합니다.
2. Deploy Now를 클릭합니다.

<figure><img src="../../.gitbook/assets/image (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

3. 원하는 저장소 이름으로 변경한 후 Deploy를 클릭합니다.

<figure><img src="../../.gitbook/assets/image (2) (1) (2) (1).png" alt="" width="375"><figcaption></figcaption></figure>

4. 성공하면 배포된 URL을 확인할 수 있습니다.

<figure><img src="../../.gitbook/assets/image (2) (2).png" alt=""><figcaption></figcaption></figure>

5. 인증을 추가하려면 Variables 탭으로 이동하여 다음을 추가합니다:

* FLOWISE\_USERNAME
* FLOWISE\_PASSWORD

<figure><img src="../../.gitbook/assets/image (15) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. 구성할 수 있는 환경 변수 목록이 있습니다. [environment-variables.md](../environment-variables.md "mention")를 참고하세요.

이것으로 끝입니다! 이제 Railway에 Flowise가 배포되었습니다 [🎉](https://emojipedia.org/party-popper/)[🎉](https://emojipedia.org/party-popper/)

## 영구 볼륨(Persistent Volume)

Railway에서 실행되는 서비스의 기본 파일 시스템은 임시(ephemeral)입니다. Flowise 데이터는 배포와 재시작 시 유지되지 않습니다. 이 문제를 해결하기 위해 [Railway Volume](https://docs.railway.app/reference/volumes)을 사용할 수 있습니다.

단계를 간소화하기 위해 볼륨이 마운트된 Railway 템플릿을 제공합니다: [https://railway.app/template/nEGbjR](https://railway.app/template/nEGbjR)

Deploy를 클릭하고 아래와 같이 환경 변수를 입력하기만 하면 됩니다:

* DATABASE\_PATH - `/opt/railway/.flowise`
* APIKEY\_PATH - `/opt/railway/.flowise`
* LOG\_PATH - `/opt/railway/.flowise/logs`
* SECRETKEY\_PATH - `/opt/railway/.flowise`
* BLOB\_STORAGE\_PATH - `/opt/railway/.flowise/storage`

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="420"><figcaption></figcaption></figure>

이제 Flowise에서 플로우를 생성하고 저장해 보세요. 그런 다음 서비스를 재시작하거나 재배포해 보면, 이전에 저장한 플로우를 여전히 확인할 수 있습니다.
