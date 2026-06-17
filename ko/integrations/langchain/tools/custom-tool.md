# Custom Tool

Custom Tool 사용 방법 보기

{% embed url="https://youtu.be/HSp9LkkTVY0" %}

## 문제

함수는 보통 구조화된 입력 데이터를 가져갑니다. LLM이 Airtable Create Record [API](https://airtable.com/developers/web/api/create-records)를 호출할 수 있기를 원한다고 가정해봅시다. 본문 매개변수는 특정 방식으로 구조화되어야 합니다. 예를 들어:

```json
"records": [
  {
    "fields": {
      "Address": "some address",
      "Name": "some name",
      "Visited": true
    }
  }
]
```

이상적으로는 LLM이 다음과 같은 적절히 구조화된 데이터를 반환하기를 원합니다:

```json
{
  "Address": "some address",
  "Name": "some name",
  "Visited": true
}
```

그러면 값을 추출하여 API에 필요한 본문으로 구문 분석할 수 있습니다. 하지만 LLM에 정확한 패턴을 출력하도록 지시하는 것은 어렵습니다.

새로운 [OpenAI Function Calling](https://openai.com/blog/function-calling-and-other-api-updates) 모델을 사용하면 이제 가능합니다. `gpt-4-0613`과 `gpt-3.5-turbo-0613`은 구조화된 데이터를 반환하도록 특별히 훈련되었습니다. 모델은 이러한 함수를 호출하기 위한 인수를 포함하는 JSON 객체를 출력하도록 지능적으로 선택합니다.

## 튜토리얼

**목표**: Agent가 자동으로 주식 가격 변동을 얻고, 관련 주식 뉴스를 검색하고, Airtable에 새 기록을 추가하도록 합니다.

시작해봅시다[🚀](https://emojipedia.org/rocket/)

### Tool 생성

목표를 달성하기 위해 3개의 Tool이 필요합니다:

* 주식 가격 변동 얻기
* 주식 뉴스 얻기
* Airtable 기록 추가

#### 주식 가격 변동 얻기

다음 세부 정보로 새 Tool을 생성합니다 (원하는 대로 변경할 수 있습니다):

* 이름: get\_stock\_movers
* 설명: 가장 큰 가격/거래량 변동을 가진 주식을 얻습니다. 예: 활발한 주식, 상승주, 하락주 등.

설명은 ChatGPT가 이 Tool을 사용할 시기를 결정하는 데 의존하므로 중요한 부분입니다.

<figure><img src="../../../.gitbook/assets/image (6) (3).png" alt=""><figcaption></figcaption></figure>

* JavaScript 함수: 데이터를 얻기 위해 [Morning Star](https://rapidapi.com/apidojo/api/morning-star) `/market/v2/get-movers` API를 사용할 것입니다. 아직 하지 않았다면 먼저 구독 테스트를 클릭한 다음 코드를 복사하여 JavaScript 함수에 붙여넣습니다.
  * 라이브러리를 가져오기 위해 맨 위에 `const fetch = require('node-fetch');`를 추가합니다. 모든 내장 NodeJS [모듈](https://www.w3schools.com/nodejs/ref_modules.asp)과 [외부 라이브러리](https://github.com/FlowiseAI/Flowise/blob/main/packages/components/src/utils.ts#L289)를 가져올 수 있습니다.
  * 끝에 `result`를 반환합니다.

<figure><img src="../../../.gitbook/assets/Untitled (4) (1).png" alt=""><figcaption></figcaption></figure>

최종 코드는 다음과 같아야 합니다:

```javascript
const fetch = require('node-fetch');
const url = 'https://morning-star.p.rapidapi.com/market/v2/get-movers';
const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'replace with your api key',
		'X-RapidAPI-Host': 'morning-star.p.rapidapi.com'
	}
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
	return result;
} catch (error) {
	console.error(error);
	return '';
}
```

이제 저장할 수 있습니다.

#### 주식 뉴스 얻기

다음 세부 정보로 새 Tool을 생성합니다 (원하는 대로 변경할 수 있습니다):

* 이름: get\_stock\_news
* 설명: 주식의 최신 뉴스를 얻습니다
* Input Schema:
  * Property: performanceId
  * Type: string
  * Description: 주식의 ID이며 API에서 performanceID로 참조됩니다
  * Required: true

Input Schema는 LLM에 JSON 객체로 반환할 내용을 알려줍니다. 이 경우 다음과 같은 JSON 객체를 예상합니다:

<pre class="language-json"><code class="lang-json"><strong>{ "performanceId": "SOME TICKER" }
</strong></code></pre>

<figure><img src="../../../.gitbook/assets/image (4) (2).png" alt=""><figcaption></figcaption></figure>

* JavaScript 함수: 데이터를 얻기 위해 [Morning Star](https://rapidapi.com/apidojo/api/morning-star) `/news/list` API를 사용할 것입니다. 아직 하지 않았다면 먼저 구독 테스트를 클릭한 다음 코드를 복사하여 JavaScript 함수에 붙여넣습니다.
  * 라이브러리를 가져오기 위해 맨 위에 `const fetch = require('node-fetch');`를 추가합니다. 모든 내장 NodeJS [모듈](https://www.w3schools.com/nodejs/ref_modules.asp)과 [외부 라이브러리](https://github.com/FlowiseAI/Flowise/blob/main/packages/components/src/utils.ts#L289)를 가져올 수 있습니다.
  * 끝에 `result`를 반환합니다.
* 다음으로 하드코딩된 URL 쿼리 매개변수 performanceId: `0P0000OQN8`를 Input Schema에 지정된 속성 변수 `$performanceId`로 바꿉니다
* Input Schema에 지정된 모든 속성을 변수 이름 앞에 `$` 접두사를 추가하여 JavaScript 함수에서 변수로 사용할 수 있습니다.

<figure><img src="../../../.gitbook/assets/Untitled (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

Final code:

```javascript
const fetch = require('node-fetch');
const url = 'https://morning-star.p.rapidapi.com/news/list?performanceId=' + $performanceId;
const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'replace with your api key',
		'X-RapidAPI-Host': 'morning-star.p.rapidapi.com'
	}
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
	return result;
} catch (error) {
	console.error(error);
	return '';
}
```

이제 저장할 수 있습니다.

#### Airtable 기록 추가

다음 세부 정보로 새 Tool을 생성합니다 (원하는 대로 변경할 수 있습니다):

* 이름: add\_airtable
* 설명: 주식, 뉴스 요약 및 가격 변동을 Airtable에 추가합니다
* Input Schema:
  * Property: stock
  * Type: string
  * Description: 주식 티커
  * Required: true
  * Property: move
  * Type: string
  * Description: 가격 변동 백분율
  * Required: true
  * Property: news\_summary
  * Type: string
  * Description: 주식의 뉴스 요약
  * Required: true

ChatGPT는 다음과 같은 JSON 객체를 반환합니다:

```json
{ "stock": "SOME TICKER", "move": "20%", "news_summary": "Some summary" }
```

<figure><img src="../../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

* JavaScript 함수: [Airtable Create Record API](https://airtable.com/developers/web/api/create-records)를 사용하여 기존 테이블에 새 기록을 생성합니다. tableId와 baseId는 [여기](https://www.highviewapps.com/kb/where-can-i-find-the-airtable-base-id-and-table-id/)에서 찾을 수 있습니다. 개인 액세스 토큰도 생성해야 하며, [여기](https://www.highviewapps.com/kb/how-do-i-create-an-airtable-personal-access-token/)에서 방법을 찾을 수 있습니다.

최종 코드는 다음과 같아야 합니다. `$stock`, `$move` 및 `$news_summary`을 변수로 전달하는 방법에 주의합니다:

```javascript
const fetch = require('node-fetch');
const baseId = 'your-base-id';
const tableId = 'your-table-id';
const token = 'your-token';

const body = {
	"records": [
		{
			"fields": {
				"stock": $stock,
				"move": $move,
				"news_summary": $news_summary,
			}
		}
	]
};

const options = {
	method: 'POST',
	headers: {
		'Authorization': `Bearer ${token}`,
		'Content-Type': 'application/json'
	},
	body: JSON.stringify(body)
};

const url = `https://api.airtable.com/v0/${baseId}/${tableId}`

try {
	const response = await fetch(url, options);
	const text = await response.text();
	return text;
} catch (error) {
	console.error(error);
	return '';
}
```

이제 저장할 수 있습니다.

생성된 3개의 Tool이 표시되어야 합니다:

<figure><img src="../../../.gitbook/assets/image (3) (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Chatflow 생성

Marketplace에서 **OpenAI Function Agent** 템플릿을 사용할 수 있으며 Tool을 **Custom Tool**로 바꿀 수 있습니다. 생성한 Tool을 선택합니다.

참고: OpenAI Function Agent는 현재 0613 모델만 지원합니다.

<figure><img src="../../../.gitbook/assets/image (15) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Chatflow를 저장하고 테스트를 시작합니다. 시작으로 다음을 시도해볼 수 있습니다:

_<mark style="color:blue;">오늘 가장 큰 가격 변동을 가진 주식은 무엇입니까?</mark>_

_<mark style="color:orange;">오늘 가장 큰 가격 변동을 가진 주식은 Overstock.com(OSTK)이며 17.47%의 가격 변동을 가집니다.</mark>_

그런 다음 다른 질문을 하여 해당 주식의 뉴스를 얻을 수 있습니다:

_<mark style="color:blue;">이 주식에 대한 최신 뉴스 중 가격 변동을 야기할 수 있는 것은 무엇입니까?</mark>_

_<mark style="color:orange;">Overstock.com(OSTK)에 대한 최신 뉴스로 가격 변동을 야기했을 수 있습니다:</mark>_

1. _<mark style="color:orange;">제목: "Overstock의 Bed Bath & Beyond 자산 2,150만 달러 입찰 성공으로 주가 상승" 출처: MarketWatch 발행일: 2023년 6월 22일 요약: Overstock.com은 Bed Bath & Beyond 자산에 대해 2,150만 달러의 입찰에 성공한 후 주가가 크게 상승했습니다.</mark>_
2. _<mark style="color:orange;">제목: "Meta Platforms, Overstock.com, Walmart, Home Depot 또는 United Parcel Service의 거래 옵션 또는 주식을 생각 중이신가요?" 출처: PR Newswire 발행일: 2023년 6월 22일 요약: 이 뉴스 기사는 투자자가 고려할 수 있는 잠재적인 거래 옵션 및 주식(Overstock.com 포함)에 대해 설명합니다.</mark>_

_<mark style="color:orange;">이러한 뉴스 기사는 정보 제공 목적으로만 제공되며 가격 변동의 유일한 이유가 아닐 수 있습니다. 투자 결정을 내리기 전에 항상 철저한 조사 및 분석을 수행하는 것이 좋습니다.</mark>_

마지막으로 ChatGPT에 Airtable에 새 기록을 추가하도록 요청할 수 있습니다:

_<mark style="color:blue;">주식 티커, 가격 변동 및 뉴스 요약이 포함된 기록을 Airtable에 추가할 수 있습니까?</mark>_

_<mark style="color:orange;">다음 세부 정보와 함께 Airtable에 기록을 추가했습니다:</mark>_

_<mark style="color:orange;">주식 티커: OSTK 가격 변동: 17.47% 뉴스 요약: Overstock.com은 Bed Bath & Beyond 자산에 대해 2,150만 달러의 입찰에 성공한 후 주가가 크게 상승했습니다.</mark>_

[🎉](https://emojipedia.org/party-popper/)[🎉](https://emojipedia.org/party-popper/)**완료!** 이것이 자신의 Custom Tool을 만들고 OpenAI Function Agent와 함께 사용하는 방법입니다!

## 추가

### 함수에 Session ID 전달

기본적으로 Custom Tool의 함수는 다음 Flow 구성에 액세스할 수 있습니다:

```json5
$flow.sessionId 
$flow.chatId
$flow.chatflowId
$flow.input
```

다음은 sessionId를 Discord 웹훅으로 전송하는 예입니다:

{% tabs %}
{% tab title="Javascript" %}
```javascript
const fetch = require('node-fetch');
const webhookUrl = "https://discord.com/api/webhooks/1124783587267";
const content = $content; // captured from input schema
const sessionId = $flow.sessionId;

const body = {
	"content": `${mycontent} and the sessionid is ${sessionId}`
};

const options = {
	method: 'POST',
	headers: {
		'Content-Type': 'application/json'
	},
	body: JSON.stringify(body)
};

const url = `${webhookUrl}?wait=true`

try {
	const response = await fetch(url, options);
	const text = await response.text();
	return text;
} catch (error) {
	console.error(error);
	return '';
}
```
{% endtab %}
{% endtabs %}

### 함수에 변수 전달

경우에 따라 Custom Tool 함수에 변수를 전달하고 싶을 수 있습니다.

예를 들어 Custom Tool을 사용하는 Chatbot을 만들고 있습니다. Custom Tool은 HTTP POST 호출을 실행하고 성공적인 인증 요청을 위해 API 키가 필요합니다. 변수로 전달할 수 있습니다.

기본적으로 Custom Tool의 함수는 변수에 액세스할 수 있습니다:

```
$vars.<variable-name>
```

Flowise에서 API 및 Embedded를 사용하여 변수를 전달하는 방법의 예:

{% tabs %}
{% tab title="Javascript API" %}
```javascript
async function query(data) {
    const response = await fetch(
        "http://localhost:3000/api/v1/prediction/<chatflow-id>",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
    const result = await response.json();
    return result;
}

query({
    "question": "Hey, how are you?",
    "overrideConfig": {
        "vars": {
            "apiKey": "abc"
        }
    }
}).then((response) => {
    console.log(response);
});
```
{% endtab %}

{% tab title="Embed" %}
```html
<script type="module">
    import Chatbot from 'https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js';
    Chatbot.init({
        chatflowid: 'chatflow-id',
        apiHost: 'http://localhost:3000',
        chatflowConfig: {
          vars: {
            apiKey: 'def'
          }
        }
    });
</script>
```
{% endtab %}
{% endtabs %}

Example of how to receive the variables in custom tool:

{% tabs %}
{% tab title="Javascript" %}
```javascript
const fetch = require('node-fetch');
const webhookUrl = "https://discord.com/api/webhooks/1124783587267";
const content = $content; // captured from input schema
const sessionId = $flow.sessionId;
const apiKey = $vars.apiKey;

const body = {
	"content": `${mycontent} and the sessionid is ${sessionId}`
};

const options = {
	method: 'POST',
	headers: {
		'Content-Type': 'application/json',
		'Authorization': `Bearer ${apiKey}`
	},
	body: JSON.stringify(body)
};

const url = `${webhookUrl}?wait=true`

try {
	const response = await fetch(url, options);
	const text = await response.text();
	return text;
} catch (error) {
	console.error(error);
	return '';
}
```
{% endtab %}
{% endtabs %}

### Custom Tool 재정의

아래 매개변수를 재정의할 수 있습니다

| 매개변수           | 설명              |
| ------------------- | -------------------- |
| customToolName      | Tool 이름           |
| customToolDesc      | Tool 설명           |
| customToolSchema    | Tool Schema         |
| customToolFunc      | Tool 함수           |

Custom Tool 매개변수를 재정의하는 API 호출의 예:

{% tabs %}
{% tab title="Javascript API" %}
```javascript
async function query(data) {
    const response = await fetch(
        "http://localhost:3000/api/v1/prediction/<chatflow-id>",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
    );
    const result = await response.json();
    return result;
}

query({
    "question": "Hey, how are you?",
    "overrideConfig": {
        "customToolName": "example_tool",
        "customToolSchema": "z.object({title: z.string()})"
    }
}).then((response) => {
    console.log(response);
});
```
{% endtab %}
{% endtabs %}

### 외부 종속성 가져오기

모든 내장 NodeJS [모듈](https://www.w3schools.com/nodejs/ref_modules.asp)과 지원되는 [외부 라이브러리](https://github.com/FlowiseAI/Flowise/blob/main/packages/components/src/utils.ts#L289)를 함수로 가져올 수 있습니다.

1. 지원되지 않는 라이브러리를 가져오려면 `packages/components` 폴더의 `package.json`에 새로운 npm 패키지를 쉽게 추가할 수 있습니다.

```bash
cd Flowise && cd packages && cd components
pnpm add <your-library>
cd .. && cd ..
pnpm install
pnpm build
```

2. 그런 다음 가져온 라이브러리를 `TOOL_FUNCTION_EXTERNAL_DEP` 환경 변수에 추가합니다. 자세한 내용은 [#builtin-and-external-dependencies](../../../configuration/environment-variables.md#builtin-and-external-dependencies "mention")를 참조하십시오.
3. 앱 시작

```bash
pnpm start
```

4. 그런 다음 **JavaScript 함수**에서 새로 추가된 라이브러리를 다음과 같이 사용할 수 있습니다:

```javascript
const axios = require('axios')
```

외부 종속성을 추가하고 라이브러리를 가져오는 방법 보기

{% embed url="https://youtu.be/0H1rrisc0ok" %}
