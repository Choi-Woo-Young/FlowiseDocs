---
description: Conversational agent for a chat model. It will utilize chat specific prompts.
---

# 대화형 에이전트

<figure><img src="../../../.gitbook/assets/image (10) (1) (1) (1) (1) (1) (1).png" alt="" width="271"><figcaption><p>대화형 에이전트 Node</p></figcaption></figure>

## Set Up the 대화형 에이전트

## Prerequisites:
* Set up Flowise.
* Download and install Docker.
* Download and install the Ollama language model locally on your machine.
    * https://ollama.com/
* Download and install Redis for AI.
    * https://redis.io/redis-for-ai/

## Context:
Unlike standard large language models (LLMs), which provide general-purpose models for performing language-based tasks, conversational agents are more sophisticated as they are designed specifically for managing conversations effectively.

You can use Flowise 대화형 에이전트 to create a comprehensive and interactive conversation experience.

## Steps:
1. Access the 챗플로우 menu.
    1. Open your browser and go to http://localhost:3000.
    2. In Flowise, click **챗플로우**.

2. Create a new chatflow:
    1. Click **Add New**.
    2. Enter a name for your chatflow and click **Save**.

3. Add a 대화형 에이전트 node:
    1. Click **Add Node**.
    2. Search for the 대화형 에이전트.
    3. Drag and drop the conversational agent node into your chatflow workspace.

4. Add a SearchAPI node. This node enables the agent to fetch data from Google search results:
    1. Click **Add Node**.
    2. Search for the SearchAPI node. It displays in the **Tools** section of the search results.
    3. Drag and drop the SearchAPI node into your chatflow workspace.
    4. Create a free SearchAPI account and retrieve your SearchAPI API key. The SearchAPI node needs this key to authenticate and perform search queries.
    5. On the SearchAPI node, click **Connect Credentials > Create New**.
    6. Enter a name for your credentials e.g. SearchAPI Credentials, copy and paste your SearchAPI API key into the SearchAPI API Key field and click **Add**.
    7. Connect the SearchAPI node to the Conversational Agent node by drawing a line from the Output section of the SearchAPI node to the Allowed Tools Inputs section of the Conversational Agent node.
    8. Click **Save Chatflow** to save your progress.

5. Add a ChatOllama chat model node. This node enables the agent to use Ollama language models to generate responses:
    1. Click **Add Node**.
    2. Search for the ChatOllama node. It displays in the **Chat Models** section of the search results.
    3. Drag and drop the ChatOllama node into your chatflow workspace.
    4. On the **Model Name** field, enter the model you’d like to use. We recommend llama3.2.
    5. On the **Temperature** field, set a temperature value between 0 and 1. The temperature parameter controls the randomness of the model's responses. Low temperature produces deterministic and focused responses. High temperature produces creative and varied responses. We recommend a temperature value of 0.5.
    6. Connect the ChatOllama node to the Conversational Agent node by drawing a line from the Output section of the ChatOllama node to the Chat Model Inputs section of the Conversational Agent node.
    7. Click **Save Chatflow** to save your progress.

6. Add a Redis chat memory node. This node enables the agent to remember previous interactions and store them in the chat history, enhancing the overall user experience:
    1. Click **Add Node**.
    2. Search for the Redis-Backed Chat Memory node. It displays in the **Memory** section of the search results.
    3. Drag and drop the Redis-Backed Chat Memory node into your chatflow workspace.
    4. On the Redis-Backed Chat Memory node, click **Connect Credentials > Create New**.
    5. Enter either your Redis API username and password or your Redis credential name and URL and click **Add**.
    6. Connect the Redis-Backed Chat Memory node to the Conversational Agent node by drawing a line from the Output section of the Redis node to the Memory Inputs section of the Conversational Agent node.
    7. Click **Save Chatflow** to save your progress.

## Result:
By following these steps, you will have successfully created a conversational agent that you can chat with and ask questions.

## Next Steps:
Click the chat icon to interact with your newly created conversational agent. If you are running Redis locally, ensure that your Docker container for Redis is running before you start the chat.

## Related Links and 문제 해결:
For additional information and 문제 해결, see https://redis.io/tutorials/howtos/solutions/flowise/conversational-agent/.


