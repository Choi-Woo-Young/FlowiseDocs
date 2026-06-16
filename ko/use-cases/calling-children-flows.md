---
description: Learn how to effectively use the Chatflow 도구 and the Custom 도구
---

# Calling Children Flows

***

One of the powerful features of Flowise is that you can turn flows into tools. For example, having a main flow to orchestrate which/when to use the necessary tools. And each tool is designed to perform a niece/specific thing.

This offers a few benefits:

* Each children flow as tool will execute on its own, with separate memory to allow cleaner output
* Aggregating detailed outputs from each children flow to a final agent, often results in higher quality output

You can achieve this by using the following tools:

* Chatflow 도구
* Custom 도구

## Chatflow 도구

1. Have a chatflow ready. In this case, we create a 체인 of Thought chatflow that can go through multiple chainings.

<figure><img src="../.gitbook/assets/image (169).png" alt=""><figcaption></figcaption></figure>

2. Create another chatflow with 도구 Agent + Chatflow 도구. Select the chatflow you want to call from the tool. In this case, it was 체인 of Thought chatflow. Give it a name, and an appropriate description to let LLM knows when to use this tool:

<figure><img src="../.gitbook/assets/image (35).png" alt="" width="245"><figcaption></figcaption></figure>

3. Test it out!

<figure><img src="../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

4. From the response, you can see the input and output from the Chatflow 도구:

<figure><img src="../.gitbook/assets/image (170).png" alt=""><figcaption></figcaption></figure>

## Custom 도구

With the same example as above, we are going to create a custom tool that will calls the [예측 API](broken-reference) of the 체인 of Thought chatflow.

1. Create a new tool:

<table><thead><tr><th width="180">도구 Name</th><th>도구 설명</th></tr></thead><tbody><tr><td>ideas_flow</td><td>Use this tool when you need to achieve certain objective</td></tr></tbody></table>

Input Schema:

<table><thead><tr><th>속성</th><th>타입</th><th>설명</th><th data-type="checkbox">필수</th></tr></thead><tbody><tr><td>input</td><td>string</td><td>input question</td><td>true</td></tr></tbody></table>

<figure><img src="../.gitbook/assets/image (95) (1).png" alt=""><figcaption></figcaption></figure>

Javascript 함수 of the tool:

```javascript
const fetch = require('node-fetch');
const url = 'http://localhost:3000/api/v1/prediction/<chatflow-id>'; // replace with specific chatflow id

const body = {
	"question": $input
};

const options = {
	method: 'POST',
	headers: {
		'Content-Type': 'application/json'
	},
	body: JSON.stringify(body)
};

try {
	const response = await fetch(url, options);
	const resp = await response.json();
	return resp.text;
} catch (error) {
	console.error(error);
	return '';
}
```

2. Create a 도구 Agent + Custom 도구. Specify the tool we've created in Step 1 in the Custom 도구.

<figure><img src="../.gitbook/assets/image (97).png" alt=""><figcaption></figcaption></figure>

3. From the response, you can see the input and output from the Custom 도구:

<figure><img src="../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>

## Conclusion

In this example, we have successfully demonstrate 2 ways of turning other chatflows into tools, via Chatflow 도구 and Custom 도구. Both are using the same code logic under the hood.
