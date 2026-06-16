---
description: Flowise에서 API 요청을 관리하는 방법을 알아봅시다
---

# 속도 제한

***

Chatflow를 API 또는 임베딩 채팅을 통해 API 인증 없이 공개적으로 공유할 때, 누구나 흐름에 액세스할 수 있습니다. 스팸을 방지하기 위해 chatflow에서 속도 제한을 설정할 수 있습니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="462"><figcaption></figcaption></figure>

* **Message Limit per Duration**: 특정 기간 동안 받을 수 있는 메시지 수. 예: 20
* **Duration in Seconds**: 지정된 기간. 예: 60
* **Limit Message**: 제한을 초과할 때 반환할 메시지. 예: Quota Exceeded

위의 예제를 사용하면 60초 동안 20개의 메시지만 받을 수 있다는 의미입니다. 속도 제한은 IP 주소로 추적됩니다. Flowise를 클라우드 서비스에 배포한 경우 `NUMBER_OF_PROXIES` 환경 변수를 설정해야 합니다.

## 속도 제한 설정

AWS, GCP, Azure 등의 클라우드에서 Flowise를 호스팅할 때 대부분의 경우 프록시/로드 밸런서 뒤에 있습니다. 따라서 속도 제한이 작동하지 않을 수 있습니다. 자세한 정보는 [여기](https://github.com/express-rate-limit/express-rate-limit/wiki/Troubleshooting-Proxy-Issues)에서 찾을 수 있습니다.

문제를 해결하려면:

1. **환경 변수 설정:** 호스팅 환경에서 `NUMBER_OF_PROXIES`라는 환경 변수를 만들고 그 값을 `0`으로 설정합니다.
2. **호스팅된 Flowise 인스턴스 재시작:** 이를 통해 Flowise가 환경 변수의 변경 사항을 적용할 수 있습니다.
3. **IP 주소 확인:** IP 주소를 확인하려면 다음 URL에 액세스합니다: `{{hosted_url}}/api/v1/ip`. 웹 브라우저에 URL을 입력하거나 API 요청을 하여 이를 수행할 수 있습니다.
4. **IP 주소 비교** 요청을 한 후 반환된 IP 주소를 현재 IP 주소와 비교합니다. 다음 웹사이트를 방문하여 현재 IP 주소를 찾을 수 있습니다:
   * [http://ip.nfriedly.com/](http://ip.nfriedly.com/)
   * [https://api.ipify.org/](https://api.ipify.org/)
5. **잘못된 IP 주소:** 반환된 IP 주소가 현재 IP 주소와 일치하지 않으면 `NUMBER_OF_PROXIES`를 1씩 증가시키고 Flowise 인스턴스를 재시작합니다. IP 주소가 자신의 주소와 일치할 때까지 이 과정을 반복합니다.
