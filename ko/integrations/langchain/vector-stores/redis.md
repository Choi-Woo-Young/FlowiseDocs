# Redis

## 사전 준비

1. Docker를 사용하여 [Redis-Stack Server](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/docker/)를 실행하세요```bash
docker run -d --name redis-stack-server -p 6379:6379 redis/redis-stack-server:latest
```## 설정

1. Canvas에 새로운 **Redis** node를 추가합니다.
2. 새로운 Redis credential을 생성합니다.

<figure><img src="../../../.gitbook/assets/image (1) (1) (3) (1) (1).png" alt="" width="257"><figcaption></figcaption></figure>

3. Redis Credential의 유형을 선택합니다. username과 password가 있는 경우 Redis API를 선택하고, 그렇지 않으면 Redis URL을 선택합니다:

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

4. url을 입력합니다:

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (2) (1).png" alt="" width="542"><figcaption></figcaption></figure>

5. 이제 Redis로 데이터를 upsert하기 시작할 수 있습니다:

<figure><img src="../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (9) (2) (1).png" alt=""><figcaption></figcaption></figure>

6. Redis Insight 포털로 이동하여 데이터베이스로 가면, upsert된 모든 데이터를 확인할 수 있습니다:

<figure><img src="../../../.gitbook/assets/image (138).png" alt=""><figcaption></figcaption></figure>