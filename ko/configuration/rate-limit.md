---
description: Flowise에서 API 요청을 관리하는 방법을 알아봅니다
---

# Rate Limit

***

API 또는 임베디드 채팅을 통해 API 인증 없이 chatflow를 공개적으로 공유하면 누구나 해당 flow에 접근할 수 있습니다. 스팸을 방지하기 위해 chatflow에 rate limit을 설정할 수 있습니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="462"><figcaption></figcaption></figure>

* **Message Limit per Duration**: 특정 기간 동안 수신할 수 있는 메시지 수. 예: 20
* **Duration in Seconds**: 지정된 기간. 예: 60
* **Limit Message**: 한도를 초과했을 때 반환할 메시지. 예: Quota Exceeded

위의 예시를 사용하면 60초 동안 20개의 메시지만 수신할 수 있다는 의미입니다. Rate limit은 IP 주소를 기준으로 추적됩니다. Flowise를 클라우드 서비스에 배포한 경우 `NUMBER_OF_PROXIES` 환경 변수를 설정해야 합니다.

## Rate Limit 설정

AWS, GCP, Azure 등의 클라우드에서 Flowise를 호스팅하는 경우 대부분 프록시/로드 밸런서 뒤에 위치하게 됩니다. 따라서 rate limit이 제대로 작동하지 않을 수 있습니다. 자세한 정보는 [여기](https://github.com/express-rate-limit/express-rate-limit/wiki/Troubleshooting-Proxy-Issues)에서 확인할 수 있습니다.

이 문제를 해결하려면 다음과 같이 합니다.

1. **환경 변수 설정:** 호스팅 환경에서 `NUMBER_OF_PROXIES`라는 환경 변수를 생성하고 그 값을 `0`으로 설정합니다.
2. **호스팅된 Flowise 인스턴스 재시작:** 이렇게 하면 Flowise가 환경 변수의 변경 사항을 적용할 수 있습니다.
3. **IP 주소 확인:** IP 주소를 확인하려면 다음 URL에 접속하세요: `{{hosted_url}}/api/v1/ip`. 웹 브라우저에 URL을 입력하거나 API 요청을 보내는 방법으로 확인할 수 있습니다.
4. **IP 주소 비교** 요청을 보낸 후, 반환된 IP 주소를 현재 IP 주소와 비교하세요. 현재 IP 주소는 다음 웹사이트 중 하나를 방문하여 확인할 수 있습니다.
   * [http://ip.nfriedly.com/](http://ip.nfriedly.com/)
   * [https://api.ipify.org/](https://api.ipify.org/)
5. **잘못된 IP 주소:** 반환된 IP 주소가 현재 IP 주소와 일치하지 않으면 `NUMBER_OF_PROXIES`를 1씩 늘리고 Flowise 인스턴스를 재시작하세요. IP 주소가 자신의 것과 일치할 때까지 이 과정을 반복하세요.
