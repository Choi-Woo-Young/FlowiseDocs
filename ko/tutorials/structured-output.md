# 구조화된 출력

채봇과 같은 많은 사용 사례에서 모델은 사용자에게 자연어로 답변할 것으로 예상됩니다. 그러나 자연어 응답이 이상적이지 않은 상황이 있습니다. 예를 들어, 모델의 출력을 가져와 HTTP 요청의 본문으로 전달하거나 데이터베이스에 저장해야 하는 경우 출력이 미리 정의된 스키마와 일치해야 합니다. 이 요구 사항으로 인해 **구조화된 출력**의 개념이 나타나며, 모델은 특정 구조화된 형식으로 응답을 생성하도록 안내됩니다.

이 튜토리얼에서는 LLM에서 구조화된 출력을 생성하고 이를 HTTP 요청의 본문으로 전달하는 방법을 살펴봅니다.

## 전제 조건

HTTP 요청을 위해 동일한 [이벤트 관리 서버](interacting-with-api.md#prerequisite)를 사용할 것입니다.

***

## 개요

1. Start 노드를 통해 사용자 입력을 받습니다.
2. LLM을 사용하여 구조화된 JSON 배열을 생성합니다.
3. 배열의 각 항목을 통해 반복합니다.
4. 각 항목을 HTTP를 통해 외부 엔드포인트로 전송합니다.

<figure><img src="../.gitbook/assets/image (306).png" alt=""><figcaption></figcaption></figure>

### 1단계: Start 노드 설정

캔버스에 **Start** 노드를 추가하여 시작합니다.

<figure><img src="../.gitbook/assets/image (307).png" alt="" width="417"><figcaption></figcaption></figure>

**주요 입력 매개변수:**

* **Input Type:**
  * `chatInput` (기본값): 흐름이 사용자의 채팅 메시지로 시작됩니다.
  * `formInput`: 사용자로부터 구조화된 데이터를 수집하려는 경우 폼으로 시작합니다.
* **Ephemeral Memory:**
  * (선택 사항) 활성화되면 흐름이 실행 간 채팅 기록을 유지하지 않습니다.
* **Flow State:**
  * (선택 사항) 상태 변수를 미리 채웁니다.
  *   예:

      ```json
      [
        { "key": "answers", "value": "" }
      ]
      ```
* **Persist State:**
  * (선택 사항) 활성화되면 상태가 동일 세션에서 유지됩니다.

### 2단계: LLM으로 구조화된 출력 생성

LLM 노드를 추가하고 Start 노드에 연결합니다.

<figure><img src="../.gitbook/assets/image (308).png" alt="" width="563"><figcaption></figcaption></figure>

**목적:** 언어 모델을 사용하여 입력을 분석하고 구조화된 JSON 배열을 생성합니다.

**주요 입력 매개변수:**

* **JSON Structured Output:**
  * **Key:** `answers`
  * **Type:** `JSON Array`
  *   **JSON Schema:**

      ```json
      {
        "name": { "type": "string", "required": true, "description": "Name of the event" },
        "date": { "type": "string", "required": true, "description": "Date of the event" },
        "location": { "type": "string", "required": true, "description": "Location of the event" }
      }
      ```
  * **Description:** "answer to user query"
* **Update Flow State:**
  * 생성된 JSON 출력으로 흐름 상태를 업데이트합니다.
  *   예:

      ```json
      [
        {
          "key": "answers",
          "value": "{{ output.answers }}"
        }
      ]
      ```

### 3단계: JSON 배열을 통해 반복

Iteration 노드를 추가하고 LLM 노드의 출력에 연결합니다.

<figure><img src="../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

**목적:** LLM 노드에서 생성된 JSON 배열의 각 항목을 반복합니다.

**주요 입력 매개변수:**

*   **Array Input:**

    * 반복할 배열입니다. 저장된 상태의 답변으로 설정합니다:

    ```html
    {{ $flow.state.answers }}
    ```

    * 이는 노드가 답변 배열의 각 이벤트를 통해 반복함을 의미합니다.

### 4단계: HTTP를 통해 각 항목 전송

루프 내에서 **HTTP** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (311).png" alt="" width="563"><figcaption></figcaption></figure>

**목적:** 배열의 각 항목에 대해 지정된 엔드포인트(예: `http://localhost:5566/events`)로 HTTP POST 요청을 전송합니다.

**주요 입력 매개변수:**

* **Method:**
  * `POST` (이 사용 사례의 기본값).
* **URL:**
  * 데이터를 전송할 엔드포인트입니다.
  *   예:

      ```
      http://localhost:5566/events
      ```
* **Headers:**
  * (선택 사항) 필요한 HTTP 헤더를 추가합니다(예: 인증용).
* **Query Params:**
  * (선택 사항) 필요한 경우 쿼리 매개변수를 추가합니다.
* **Body Type:**
  * `json` (기본값): 본문을 JSON으로 전송합니다.
* **Body:**
  * 요청 본문에서 보낼 데이터입니다.
  *   루프의 현재 항목으로 설정합니다:

      ```html
      {{ $iteration }}
      ```
* **Response Type:**
  * `json` (기본값): JSON 응답을 예상합니다.

***

## 상호 작용 예시

**사용자 입력:**

```
create 2 events:
1. JS Conference on next Sat in Netherlands
2. GenAI meetup, Sept 19, in Dublin
```

**흐름:**

* Start 노드가 입력을 받습니다.
* LLM 노드가 이벤트의 JSON 배열을 생성합니다.
* Loop 노드가 각 이벤트를 통해 반복합니다.
* HTTP 노드가 API를 통해 각 이벤트를 생성합니다.

<figure><img src="../.gitbook/assets/image (304).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (305).png" alt=""><figcaption></figcaption></figure>

***

## 완전한 흐름 구조

{% file src="../.gitbook/assets/Structured Output.json" %}

***

## 모범 사례

**설계 지침:**

1. **명확한 출력 스키마:** 신뢰할 수 있는 다운스트림 처리를 보장하기 위해 LLM 출력에 대한 예상 구조를 정의합니다.

**일반적인 사용 사례:**

* **이벤트 처리:** 이벤트 데이터를 수집하여 캘린더 또는 이벤트 관리 시스템으로 전송합니다.
* **대량 데이터 입력:** 데이터베이스 또는 API에 여러 레코드를 생성하고 제출합니다.
* **자동 알림:** 목록의 각 항목에 대해 개인화된 메시지 또는 경고를 전송합니다.
