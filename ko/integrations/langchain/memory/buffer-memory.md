# Buffer 메모리

Flowise 데이터베이스 테이블 `chat_message`를 대화를 저장/검색하는 저장소 메커니즘으로 사용합니다.

<figure><img src="../../../.gitbook/assets/image (1) (1) (3).png" alt="" width="299"><figcaption></figcaption></figure>

## 입력

| Parameter  | 설명                                                                       | 기본값       |
| ---------- | -------------------------------------------------------------------------- | ------------ |
| Session Id | 메시지를 검색/저장하기 위한 ID입니다. 지정되지 않은 경우 임의의 ID가 사용됩니다. |              |
| Memory Key | 프롬프트 템플릿에서 메시지 형식을 지정하기 위해 사용되는 키                   | chat\_history |