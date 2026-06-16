---
description: Learn the Fundamentals of Sequential Agents in Flowise, written by @toi500
---

# Sequential Agents

This guide offers a complete overview of the Sequential Agent AI system architecture within Flowise, exploring its core components and workflow design principles.

{% hint style="warning" %}
**Disclaimer**: This documentation is intended to help Flowise users understand and build conversational workflows using the Sequential Agent system architecture. It is not intended to be a comprehensive technical reference for the LangGraph framework and should not be interpreted as defining industry standards or core LangGraph concepts.
{% endhint %}

## Concept

Built on top of [LangGraph](https://www.langchain.com/langgraph), Flowise's Sequential Agents architecture facilitates the **development of conversational agentic systems by structuring the workflow as a directed cyclic graph (DCG)**, allowing controlled loops and iterative processes.

This graph, composed of interconnected nodes, defines the sequential flow of information and actions, enabling the agents to process inputs, execute tasks, and generate responses in a structured manner.

<figure><img src="../../../.gitbook/assets/seq-21.svg" alt=""><figcaption></figcaption></figure>

### Understanding Sequential Agents' DCG 아키텍처

This architecture simplifies the management of complex conversational workflows by defining a clear and understandable sequence of operations through its DCG structure.

Let's explore some key elements of this approach:

{% tabs %}
{% tab title="Core Principles" %}
* **노드-based processing:** Each node in the graph represents a discrete processing unit, encapsulating its own functionality like language processing, tool execution, or conditional logic.
* **Data flow as connections:** Edges in the graph represent the flow of data between nodes, where the output of one node becomes the input for the subsequent node, enabling a chain of processing steps.
* **상태 management:** 상태 is managed as a shared object, persisting throughout the conversation. This allows nodes to access relevant information as the workflow progresses.
{% endtab %}

{% tab title="Terminology" %}
* **흐름:** The movement or direction of data within the workflow. It describes how information passes between nodes during a conversation.
* **워크플로우:** The overall design and structure of the system. It's the blueprint that defines the sequence of nodes, their connections, and the logic that orchestrates the conversation flow.
* **상태:** A shared data structure that represents the current snapshot of the conversation. It includes the conversation history `state.messages` and any custom 상태 variables defined by the user.
* **Custom 상태:** 사용자-defined key-value pairs added to the state object to store additional information relevant to the workflow.
* **도구:** An external system, API, or service that can be accessed and executed by the workflow to perform specific tasks, such as retrieving information, processing data, or interacting with other applications.
* **Human-in-the-루프 (HITL):** A feature that allows human intervention in the workflow, primarily during tool execution. It enables a human reviewer to approve or reject a tool call before it's executed.
* **병렬 node execution:** It refers to the ability to execute multiple nodes concurrently within a workflow by using a branching mechanism. This means that different branches of the workflow can process information or interact with tools simultaneously, even though the overall flow of execution remains sequential.
{% endtab %}
{% endtabs %}

***

## Sequential Agents vs Multi-Agents

While both Multi-Agent and Sequential Agent systems in Flowise are built upon the LangGraph framework and share the same fundamental principles, the Sequential Agent architecture provides a [lower level of abstraction](#user-content-fn-1)[^1], offering more granular control over every step of the workflow.

**Multi-Agent systems**, which are characterized by a hierarchical structure with a central supervisor agent delegating tasks to specialized worker agents, **excel at handling complex workflows by breaking them down into manageable sub-tasks**. This decomposition into sub-tasks is made possible by pre-configuring core system elements under the hood, such as condition nodes, which would require manual setup in a Sequential Agent system. As a result, users can more easily build and manage teams of agents.

In contrast, **Sequential Agent systems** operate like a streamlined assembly line, where data flows sequentially through a chain of nodes, making them ideal for tasks demanding a precise order of operations and incremental data refinement. Compared to the Multi-Agent system, its lower-level access to the underlying workflow structure makes it fundamentally more **flexible and customizable, offering parallel node execution and full control over the system logic**, incorporating conditions, state, and loop nodes into the workflow, allowing for the creation of new dynamic branching capabilities.

### Introducing 상태, 루프 and 조건 Nodes

Flowise's Sequential Agents offer new capabilities for creating conversational systems that can adapt to user input, make decisions based on context, and perform iterative tasks.

These capabilities are made possible by the introduction of four new core nodes; the 상태 노드, the 루프 노드, and two 조건 Nodes.

<figure><img src="../../../.gitbook/assets/seq-20.png" alt=""><figcaption></figcaption></figure>

* **상태 노드:** We define 상태 as a shared data structure that represents the current snapshot of our application or workflow. The 상태 노드 allows us to **add a custom 상태** to our workflow from the start of the conversation. This custom 상태 is accessible and modifiable by other nodes in the workflow, enabling dynamic behavior and data sharing.
* **루프 노드:** This node **introduces controlled cycles** within the Sequential Agent workflow, enabling iterative processes where a sequence of nodes can be repeated based on specific conditions. This allows agents to refine outputs, gather additional information from the user, or perform tasks multiple times.
* **조건 Nodes:** The 조건 and 조건 Agent 노드 provide the necessary control to **create complex conversational flows with branching paths**. The 조건 노드 evaluates conditions directly, while the 조건 Agent 노드 uses an agent's reasoning to determine the branching logic. This allows us to dynamically guide the flow's behavior based on user input, the custom 상태, or results of actions taken by other nodes.

### Choosing the right system

Selecting the ideal system for your application depends on understanding your specific workflow needs. Factors like task complexity, the need for parallel processing, and your desired level of control over data flow are all key considerations.

* **For simplicity:** If your workflow is relatively straightforward, where tasks can be completed one after the other and therefore does not require parallel node execution or Human-in-the-루프 (HITL), the Multi-Agent approach offers ease of use and quick setup.
* **For flexibility:** If your workflow needs parallel execution, dynamic conversations, custom 상태 management, and the ability to incorporate HITL, the **Sequential Agent** approach provides the necessary flexibility and control.

Here's a table comparing Multi-Agent and Sequential Agent implementations in Flowise, highlighting key differences and design considerations:

<table><thead><tr><th width="173.33333333333331"></th><th width="281">Multi-Agent</th><th>Sequential Agent</th></tr></thead><tbody><tr><td>Structure</td><td><strong>Hierarchical</strong>; Supervisor delegates to specialized Workers.</td><td><strong>Linear, cyclic and/or</strong> <strong>branching</strong>; nodes connect in a sequence, with conditional logic for branching.</td></tr><tr><td>워크플로우</td><td>Flexible; designed for breaking down a complex task into a <strong>sequence of sub-tasks</strong>, completed one after another.</td><td>Highly flexible; <strong>supports parallel node execution</strong>, complex dialogue flows, branching logic, and loops within a single conversation turn.</td></tr><tr><td>병렬 노드 실행</td><td><strong>No</strong>; Supervisor handles one task at a time.</td><td><strong>Yes</strong>; can trigger multiple actions in parallel within a single run.</td></tr><tr><td>상태 Management</td><td><strong>Implicit</strong>; 상태 is in place, but is not explicitly managed by the developer.</td><td><strong>Explicit</strong>; 상태 is in place, and developers can define and manage an initial or custom 상태 using the 상태 노드 and the "업데이트 상태" field in various nodes.</td></tr><tr><td>도구 사용법</td><td><strong>Workers</strong> can access and use tools as needed.</td><td>Tools are accessed and executed through <strong>Agent Nodes</strong> and <strong>도구 Nodes</strong>.</td></tr><tr><td>Human-in-the-루프 (HITL)</td><td>HITL is <strong>not supported.</strong></td><td><strong>Supported</strong> through the Agent 노드 and 도구 노드's "Require Approval" feature, allowing human review and approval or rejection of tool execution.</td></tr><tr><td>복잡도</td><td>Higher level of abstraction; <strong>simplifies workflow design.</strong></td><td>Lower level of abstraction; <strong>more complex workflow design</strong>, requiring careful planning of node interactions, custom 상태 management, and conditional logic.</td></tr><tr><td>Ideal Use Cases</td><td><ul><li>Automating linear processes (e.g., data extraction, lead generation).</li><li>Situations where sub-tasks need to be completed one after the other.</li></ul></td><td><ul><li>Building conversational systems with dynamic flows.</li><li>Complex workflows requiring parallel node execution or branching logic.</li><li>Situations where decision-making is needed at multiple points in the conversation.</li></ul></td></tr></tbody></table>

{% hint style="info" %}
**참고**: Even though Multi-Agent systems are technically a higher-level layer built upon the Sequential Agent architecture, they offer a distinct user experience and approach to workflow design. The comparison above treats them as separate systems to help you select the best option for your specific needs.
{% endhint %}

***

## Sequential Agents Nodes

Sequential Agents bring a whole new dimension to Flowise, **introducing 10 specialized nodes**, each serving a specific purpose, offering more control over how our conversational agents interact with users, process information, make decisions, and execute actions.

The following sections aim to provide a comprehensive understanding of each node's functionality, inputs, outputs, and best practices, ultimately enabling you to craft sophisticated conversational workflows for a variety of applications.

<figure><img src="../../../.gitbook/assets/seq-00.png" alt=""><figcaption></figcaption></figure>

***

## 1. Start 노드

As its name implies, the Start 노드 is the **entry point for all workflows in the Sequential Agent architecture**. It receives the initial user query, initializes the conversation 상태, and sets the flow in motion.

<figure><img src="../../../.gitbook/assets/seq-02.png" alt="" width="300"><figcaption></figcaption></figure>

### Understanding the Start 노드

The Start 노드 ensures that our conversational workflows have the necessary setup and context to function correctly. **It's responsible for setting up key functionalitie**s that will be used throughout the rest of the workflow:

* **Defining the default LLM:** The Start 노드 requires us to specify a Chat 모델 (LLM) compatible with function calling, enabling agents in the workflow to interact with tools and external systems. It will be the default LLM used under the hood in the workflow.
* **Initializing 메모리:** We can optionally connect an Agent 메모리 노드 to store and retrieve conversation history, enabling more context-aware responses.
* **설정 a custom 상태:** By default, the 상태 contains an immutable `state.messages` array, which acts as the transcript or history of the conversation between the user and the agents. The Start 노드 allows you to connect a custom 상태 to the workflow adding a 상태 노드, enabling the storage of additional information relevant to your workflow
* **Enabling moderation:** Optionally, we can connect Input Moderation to analyze the user's input and prevent potentially harmful content from being sent to the LLM.

### Inputs

<table><thead><tr><th width="212"></th><th width="102">필수</th><th>설명</th></tr></thead><tbody><tr><td>Chat 모델</td><td><strong>Yes</strong></td><td>The default LLM that will power the conversation. Only compatible with <strong>models that are capable of function calling</strong>.</td></tr><tr><td>Agent 메모리 노드</td><td>No</td><td>Connect an Agent 메모리 노드 to <strong>enable persistence and context preservation</strong>.</td></tr><tr><td>상태 노드</td><td>No</td><td>Connect a 상태 노드 to <strong>set a custom 상태</strong>, a shared context that can be accessed and modified by other nodes in the workflow.</td></tr><tr><td>Input Moderation</td><td>No</td><td>Connect a Moderation 노드 to <strong>filter content</strong> by detecting text that could generate harmful output, preventing it from being sent to the LLM.</td></tr></tbody></table>

### Outputs

The Start 노드 can connect to the following nodes as outputs:

* **Agent 노드:** Routes the conversation flow to an Agent 노드, which can then execute actions or access tools based on the conversation's context.
* **LLM 노드:** Routes the conversation flow to an LLM 노드 for processing and response generation.
* **조건 Agent 노드:** Connects to a 조건 Agent 노드 to implement branching logic based on the agent's evaluation of the conversation.
* **조건 노드:** Connects to a 조건 노드 to implement branching logic based on predefined conditions.

### 모범 사례

{% tabs %}
{% tab title="Pro Tips" %}
**Choose the right Chat 모델**

Ensure your selected LLM supports function calling, a key feature for enabling agent-tool interactions. Additionally, choose an LLM that aligns with the complexity and requirements of your application. You can override the default LLM by setting it at the Agent/LLM/조건 Agent node level when necessary.

**Consider context and persistence**

If your use case demands it, utilize Agent 메모리 노드 to maintain context and personalize interactions.
{% endtab %}

{% tab title="Potential Pitfalls" %}
**Incorrect Chat 모델 (LLM) selection**

* **문제:** The Chat 모델 selected in the Start 노드 is not suitable for the intended tasks or capabilities of the workflow, resulting in poor performance or inaccurate responses.
* **예제:** A workflow requires a Chat 모델 with strong summarization capabilities, but the Start 노드 selects a model optimized for code generation, leading to inadequate summaries.
* **솔루션:** Choose a Chat 모델 that aligns with the specific requirements of your workflow. Consider the model's strengths, weaknesses, and the types of tasks it excels at. Refer to the documentation and experiment with different models to find the best fit.

**Overlooking Agent 메모리 노드 configuration**

* **문제:** The Agent 메모리 노드 is not properly connected or configured, resulting in the loss of conversation history data between sessions.
* **예제:** You intend to use persistent memory to store user preferences, but the Agent 메모리 노드 is not connected to the Start 노드, causing preferences to be reset on each new conversation.
* **솔루션:** Ensure that the Agent 메모리 노드 is connected to the Start 노드 and configured with the appropriate database (SQLite). For most use cases, the default SQLite database will be sufficient.

**Inadequate Input Moderation**

* **문제:** The "Input Moderation" is not enabled or configured correctly, allowing potentially harmful or inappropriate user input to reach the LLM and generate undesirable responses.
* **예제:** A user submits offensive language, but the input moderation fails to detect it or is not set up at all, allowing the query to reach the LLM.
* **솔루션:** 추가 and configure an input moderation node in the Start 노드 to filter out potentially harmful or inappropriate language. Customize the moderation settings to align with your specific requirements and use cases.
{% endtab %}
{% endtabs %}

## 2. Agent 메모리 노드

The Agent 메모리 노드 **provides a mechanism for persistent memory storage**, allowing the Sequential Agent workflow to retain the conversation history `state.messages` and any custom 상태 previously defined across multiple interactions

This long-term memory is essential for agents to learn from previous interactions, maintain context over extended conversations, and provide more relevant responses.

<figure><img src="../../../.gitbook/assets/seq-03.png" alt="" width="299"><figcaption></figcaption></figure>

### Where the data is recorded

By default, Flowise utilizes its **built-in SQLite database** to store conversation history and custom state data, creating a "**checkpoints**" table to manage this persistent information.

#### Understanding the "checkpoints" table structure and data format

This table **stores snapshots of the system's 상태 at various points during a conversation**, enabling the persistence and retrieval of conversation history. Each row represents a specific point or "checkpoint" in the workflow's execution.

<figure><img src="../../../.gitbook/assets/seq-12.png" alt=""><figcaption></figcaption></figure>

#### 테이블 structure

* **thread\_id:** A unique identifier representing a specific conversation session, **our session ID**. It groups together all checkpoints related to a single workflow execution.
* **checkpoint\_id:** A unique identifier for each execution step (node execution) within the workflow. It helps track the order of operations and identify the 상태 at each step.
* **parent\_id:** Indicates the checkpoint\_id of the preceding execution step that led to the current checkpoint. This establishes a hierarchical relationship between checkpoints, allowing for the reconstruction of the workflow's execution flow.
* **checkpoint:** Contains a JSON string representing the current 상태 of the workflow at that specific checkpoint. This includes the values of variables, the messages exchanged, and any other relevant data captured at that point in the execution.
* **metadata:** Provides additional context about the checkpoint, specifically related to node operations.

#### How it works

As a Sequential Agent workflow executes, the system records a checkpoint in this table for each significant step. This mechanism provides several benefits:

* **실행 tracking:** Checkpoints enable the system to understand the execution path and the order of operations within the workflow.
* **상태 management:** Checkpoints store the 상태 of the workflow at each step, including variable values, conversation history, and any other relevant data. This allows the system to maintain contextual awareness and make informed decisions based on the current 상태.
* **워크플로우 resumption:** If the workflow is paused or interrupted (e.g., due to a system error or user request), the system can use the stored checkpoints to resume execution from the last recorded 상태. This ensures that the conversation or task continues from where it left off, preserving the user's progress and preventing data loss.

### **Inputs**

The Agent 메모리 노드 has **no specific input connections**.

### 노드 설정

<table><thead><tr><th width="189"></th><th width="107">필수</th><th>설명</th></tr></thead><tbody><tr><td>데이터베이스</td><td><strong>Yes</strong></td><td>The type of database used for storing conversation history. Currently, <strong>only SQLite is supported</strong>.</td></tr></tbody></table>

### Additional 매개변수

<table><thead><tr><th width="189"></th><th width="107">필수</th><th>설명</th></tr></thead><tbody><tr><td>데이터베이스 File 경로</td><td>No</td><td>The file path to the SQLite database file. <strong>If not provided, the system will use a default location</strong>.</td></tr></tbody></table>

### **Outputs**

The Agent 메모리 노드 interacts solely with the **Start 노드**, making the conversation history available from the very beginning of the workflow.

### **모범 사례**

{% tabs %}
{% tab title="Pro Tips" %}
**Strategic use**

Employ Agent 메모리 only when necessary. For simple, stateless interactions, it might be overkill. Reserve it for scenarios where retaining information across turns or sessions is essential.
{% endtab %}

{% tab title="Potential Pitfalls" %}
**Unnecessary overhead**

* **The 문제:** Using Agent 메모리 for every interaction, even when not needed, introduces unnecessary storage and processing overhead. This can slow down response times and increase resource consumption.
* **예제:** A simple weather chatbot that provides information based on a single user request doesn't need to store conversation history.
* **솔루션:** Analyze the requirements of your system and only utilize Agent 메모리 when persistent data storage is essential for functionality or user experience.
{% endtab %}
{% endtabs %}

***

## 3. 상태 노드

The 상태 노드, which can only be connected to the Start 노드, **provides a mechanism to set a user-defined or custom 상태** into our workflow from the start of the conversation. This custom 상태 is a JSON object that is shared and can be updated by nodes in the graph, passing from one node to another as the flow progresses.

<figure><img src="../../../.gitbook/assets/seq-04.png" alt="" width="299"><figcaption></figcaption></figure>

### Understanding the 상태 노드

By default, the 상태 includes a `state.messages` array, which acts as our conversation history. This array stores all messages exchanged between the user and the agents, or any other actors in the workflow, preserving it throughout the workflow execution.

Since by definition this `state.messages` array is immutable and cannot be modified, **the purpose of the 상태 노드 is to allow us to define custom key-value pairs**, expanding the state object to hold any additional information relevant to our workflow.

{% hint style="info" %}
When no **Agent 메모리 노드** is used, the 상태 operates in-memory and is not persisted for future use.
{% endhint %}

### Inputs

The 상태 노드 has **no specific input connections**.

### Outputs

The 상태 노드 can only connect to the **Start 노드**, allowing the setup of a custom 상태 from the beginning of the workflow and allowing other nodes to access and potentially modify this shared custom 상태.

### Additional 매개변수

<table><thead><tr><th width="157"></th><th width="113">필수</th><th>설명</th></tr></thead><tbody><tr><td>Custom 상태</td><td><strong>Yes</strong></td><td>A JSON object representing the <strong>initial custom 상태 of the workflow</strong>. This object can contain any key-value pairs relevant to the application.</td></tr></tbody></table>

### How to set a custom 상태 <a href="#alert-dialog-title" id="alert-dialog-title"></a>

Specify the **key**, **operation type**, and **default value** for the state object. The operation type can be either "교체" or "추가".

* **교체**
  1. 교체 the existing value with the new value.
  2. If the new value is null, the existing value will be retained.
* **추가**
  1. 추가 the new value to the existing value.
  2. 기본값 values can be empty or an array. Ex: \["a", "b"]
  3. Final value is an array.

#### 예제 using JS

{% code overflow="wrap" %}
```javascript
{
    aggregate: {
        value: (x, y) => x.concat(y), // here we append the new message to the existing messages
        default: () => []
    }
}
```
{% endcode %}

#### 예제 using 테이블

To define a custom 상태 using the table interface in the 상태 노드, follow these steps:

1. **추가 item:** Click the "+ 추가 항목" button to add rows to the table. Each row represents a key-value pair in your custom 상태.
2. **Specify keys:** In the "키" column, enter the name of each key you want to define in your state object. For example, you might have keys like "userName", "userLocation", etc.
3. **Choose operations:** In the "작업" column, select the desired operation for each key. You have two options:
   * **교체:** This will replace the existing value of the key with the new value provided by a node. If the new value is null, the existing value will be retained.
   * **추가:** This will append the new value to the existing value of the key. The final value will be an array.
4. **집합 default values:** In the "기본값 값" column, enter the initial value for each key. This value will be used if no other node provides a value for the key. The default value can be empty or an array.

#### 예제 테이블

| 키      | 작업 | 기본값 값 |
| -------- | --------- | ------------- |
| userName | 교체   | null          |

<figure><img src="../../../.gitbook/assets/seq-14.png" alt="" width="375"><figcaption></figcaption></figure>

1. This table defines one key in the custom 상태: `userName`.
2. The `userName` key will use the "교체" operation, meaning its value will be updated whenever a node provides a new value.
3. The `userName` key has a default value of _null,_ indicating that it has no initial value.

{% hint style="info" %}
Remember that this table-based approach is an alternative to defining the custom 상태 using JavaScript. Both methods achieve the same result.
{% endhint %}

#### 예제 using API

```json
{
    "question": "hello",
    "overrideConfig": {
        "stateMemory": [
            {
                "Key": "userName",
                "Operation": "Replace",
                "Default Value": "somevalue"
            }
        ]
    }
}
```

### 모범 사례

{% tabs %}
{% tab title="Pro-Tips" %}
**계획 your custom 상태 structure**

Before building your workflow, design the structure of your custom 상태. A well-organized custom 상태 will make your workflow easier to understand, manage, and debug.

**Use meaningful key names**

Choose descriptive and consistent key names that clearly indicate the purpose of the data they hold. This will improve the readability of your code and make it easier for others (or you in the future) to understand how the custom 상태 is being used.

**Keep custom 상태 minimal**

Only store information in the custom 상태 that is essential for the workflow's logic and decision-making.

**Consider 상태 persistence**

If you need to preserve 상태 across multiple conversation sessions (e.g., for user preferences, order history, etc.), use the Agent 메모리 노드 to store the 상태 in a persistent database.
{% endtab %}

{% tab title="Potential Pitfalls" %}
**Inconsistent 상태 Updates**

* **문제:** Updating the custom 상태 in multiple nodes without a clear strategy can lead to inconsistencies and unexpected behavior.
* **예제**
  1. Agent 1 updates `orderStatus` to "Payment Confirmed".
  2. Agent 2, in a different branch, updates `orderStatus` to "Order Complete" without checking the previous status.
* **솔루션:** Use 조건 Nodes to control the flow of the custom 상태 updates and ensure that custom 상태 transitions happen in a logical and consistent manner.
{% endtab %}
{% endtabs %}

***

## 4. Agent 노드

The Agent 노드 is a **core component of the Sequential Agent architecture.** It acts as a decision-maker and orchestrator within our workflow.

<figure><img src="../../../.gitbook/assets/sa-agent.png" alt="" width="268"><figcaption></figcaption></figure>

### Understanding the Agent 노드

Upon receiving input from preceding nodes, which always includes the full conversation history `state.messages` and any custom 상태 at that point in the execution, the Agent 노드 uses its defined "persona", established by the 시스템 Prompt, to determine if external tools are necessary to fulfill the user's request.

* If tools are required, the Agent 노드 autonomously selects and executes the appropriate tool. This execution can be automatic or, for sensitive tasks, require human approval (HITL) before proceeding. Once the tool completes its operation, the Agent 노드 receives the results, processes them using the designated Chat 모델 (LLM), and generates a comprehensive response.
* In cases where no tools are needed, the Agent 노드 directly leverages the Chat 모델 (LLM) to formulate a response based on the current conversation context.

### Inputs

<table><thead><tr><th width="195"></th><th width="107">필수</th><th>설명</th></tr></thead><tbody><tr><td>External Tools</td><td>No</td><td>Provides the Agent 노드 with <strong>access to a suite of external tools</strong>, enabling it to perform actions and retrieve information.</td></tr><tr><td>Chat 모델</td><td>No</td><td>추가 a new Chat 모델 to <strong>overwrite the default Chat 모델</strong> (LLM) of the workflow. Only compatible with models that are capable of function calling.</td></tr><tr><td>Start 노드</td><td><strong>Yes</strong></td><td>Receives the <strong>initial user input</strong>, along with the custom 상태 (if set up) and the rest of the default <code>state.messages</code> array from the Start 노드.</td></tr><tr><td>조건 노드</td><td><strong>Yes</strong></td><td>Receives input from a preceding 조건 노드, enabling the Agent 노드 to <strong>take actions or guide the conversation based on the outcome of the 조건 노드's evaluation</strong>.</td></tr><tr><td>조건 Agent 노드</td><td><strong>Yes</strong></td><td>Receives input from a preceding 조건 Agent 노드, enabling the Agent 노드 to <strong>take actions or guide the conversation based on the outcome of the 조건 Agent 노드's evaluation</strong>.</td></tr><tr><td>Agent 노드</td><td><strong>Yes</strong></td><td>Receives input from a preceding Agent 노드, <strong>enabling chained agent actions</strong> and maintaining conversational context</td></tr><tr><td>LLM 노드</td><td><strong>Yes</strong></td><td>Receives the output from LLM 노드, enabling the Agent 노드 to <strong>process the LLM's response</strong>.</td></tr><tr><td>도구 노드</td><td><strong>Yes</strong></td><td>Receives the output from a 도구 노드, enabling the Agent 노드 to <strong>process and integrate tool's outputs into its response</strong>.</td></tr></tbody></table>

{% hint style="info" %}
The **Agent 노드 requires at least one connection from the following nodes**: Start 노드, Agent 노드, 조건 노드, 조건 Agent 노드, LLM 노드, or 도구 노드.
{% endhint %}

### Outputs

The Agent 노드 can connect to the following nodes as outputs:

* **Agent 노드:** Passes control to a subsequent Agent 노드, enabling the chaining of multiple agent actions within a workflow. This allows for more complex conversational flows and task orchestration.
* **LLM 노드:** Passes the agent's output to an LLM 노드, enabling further language processing, response generation, or decision-making based on the agent's actions and insights.
* **조건 Agent 노드:** Directs the flow to a 조건 Agent 노드. This node evaluates the Agent 노드's output and its predefined conditions to determine the appropriate next step in the workflow.
* **조건 노드:** Similar to the 조건 Agent 노드, the 조건 노드 uses predefined conditions to assess the Agent 노드's output, directing the flow along different branches based on the outcome.
* **End 노드:** Concludes the conversation flow.
* **루프 노드:** Redirects the flow back to a previous node, enabling iterative or cyclical processes within the workflow. This is useful for tasks that require multiple steps or involve refining results based on previous interactions. For example, you might loop back to an earlier Agent 노드 or LLM 노드 to gather additional information or refine the conversation flow based on the current Agent 노드's output.

### 노드 설정

<table><thead><tr><th width="201"></th><th width="101">필수</th><th>설명</th></tr></thead><tbody><tr><td>Agent Name</td><td><strong>Yes</strong></td><td>추가 a descriptive name to the Agent 노드 to enhance workflow readability and easily <strong>target it back when using loops</strong> within the workflow.</td></tr><tr><td>시스템 Prompt</td><td>No</td><td>Defines the <strong>agent's 'persona'</strong> and <strong>guides its behavior</strong>. For example, "<em>You are a customer service agent specializing in technical support</em> [...]."</td></tr><tr><td>Require Approval</td><td>No</td><td><strong>Activates the Human-in-the-loop (HITL) feature</strong>. If set to '<strong>True</strong>,' the Agent 노드 will request human approval before executing any tool. This is particularly valuable for sensitive operations or when human oversight is desired. Defaults to '<strong>False</strong>,' allowing the Agent 노드 to execute tools autonomously.</td></tr></tbody></table>

### Additional 매개변수

<table><thead><tr><th width="200"></th><th width="102">필수</th><th>설명</th></tr></thead><tbody><tr><td>Human Prompt</td><td>No</td><td>This prompt is appended to the <code>state.messages</code> array as a human message. It allows us to <strong>inject a human-like message into the conversation flow</strong> after the Agent 노드 has processed its input and before the next node receives the Agent 노드's output.</td></tr><tr><td>Approval Prompt</td><td>No</td><td><strong>A customizable prompt presented to the human reviewer when the HITL feature is active</strong>. This prompt provides context about the tool execution, including the tool's name and purpose. The variable <code>{tools}</code> within the prompt will be dynamically replaced with the actual list of tools suggested by the agent, ensuring the human reviewer has all necessary information to make an informed decision.</td></tr><tr><td>Approve 버튼 Text</td><td>No</td><td>Customizes <strong>the text displayed on the button for approving tool execution</strong> in the HITL interface. This allows for tailoring the language to the specific context and ensuring clarity for the human reviewer.</td></tr><tr><td>Reject 버튼 Text</td><td>No</td><td>Customizes the <strong>text displayed on the button for rejecting tool execution</strong> in the HITL interface. Like the Approve 버튼 Text, this customization enhances clarity and provides a clear action for the human reviewer to take if they deem the tool execution unnecessary or potentially harmful.</td></tr><tr><td>업데이트 상태</td><td>No</td><td>Provides a <strong>mechanism to modify the shared custom 상태 object within the workflow</strong>. This is useful for storing information gathered by the agent or influencing the behavior of subsequent nodes.</td></tr><tr><td>Max 반복</td><td>No</td><td>Limits the <strong>number of iterations</strong> an Agent 노드 can make within a single workflow execution.</td></tr></tbody></table>

### 모범 사례

{% tabs %}
{% tab title="Pro Tips" %}
**삭제 system prompt**

Craft a concise and unambiguous 시스템 Prompt that accurately reflects the agent's role and capabilities. This guides the agent's decision-making and ensures it acts within its defined scope.

**Strategic tool selection**

Choose and configure the tools available to the Agent 노드, ensuring they align with the agent's purpose and the overall goals of the workflow.

**HITL for sensitive tasks**

Utilize the 'Require Approval' option for tasks involving sensitive data, requiring human judgment, or carrying a risk of unintended consequences.

**Leverage custom 상태 updates**

업데이트 the custom 상태 object strategically to store gathered information or influence the behavior of downstream nodes.
{% endtab %}

{% tab title="Potential Pitfalls" %}
**Agent inaction due to tool overload**

* **문제:** When an Agent 노드 has access to a large number of tools within a single workflow execution, it might struggle to decide which tool is the most appropriate to use, even when a tool is clearly necessary. This can lead to the agent failing to call any tool at all, resulting in incomplete or inaccurate responses.
* **예제:** Imagine a customer support agent designed to handle a wide range of inquiries. You've equipped it with tools for order tracking, billing information, product returns, technical support, and more. A user asks, "What's the status of my order?" but the agent, overwhelmed by the number of potential tools, responds with a generic answer like, "I can help you with that. What's your order number?" without actually using the order tracking tool.
* **솔루션**
  1. **Refine system prompts:** Provide clearer instructions and examples within the Agent 노드's 시스템 Prompt to guide it towards the correct tool selection. If needed, emphasize the specific capabilities of each tool and the situations in which they should be used.
  2. **Limit tool choices per node:** If possible, break down complex workflows into smaller, more manageable segments, each with a more focused set of tools. This can help reduce the cognitive load on the agent and improve its tool-selection accuracy.

**Overlooking HITL for sensitive tasks**

* **문제:** Failing to utilize the Agent 노드's "Require Approval" (HITL) feature for tasks involving sensitive information, critical decisions, or actions with potential real-world consequences can lead to unintended outcomes or damage to user trust.
* **예제:** Your travel booking agent has access to a user's payment information and can automatically book flights and hotels. Without HITL, a misinterpretation of user intent or an error in the agent's understanding could result in an incorrect booking or unauthorized use of the user's payment details.
* **솔루션**
  1. **Identify sensitive actions:** Analyze your workflow and identify any actions that involve accessing or processing sensitive data (e.g., payment info, personal details).
  2. **구현 "Require Approval":** For these sensitive actions, enable the "Require Approval" option within the Agent 노드. This ensures that a human reviews the agent's proposed action and the relevant context before any sensitive data is accessed or any irreversible action is taken.
  3. **설계 clear approval prompts:** Provide clear and concise prompts for human reviewers, summarizing the agent's intent, the proposed action, and the relevant information needed for the reviewer to make an informed decision.

**Unclear or incomplete system prompt**

* **문제:** The 시스템 Prompt provided to the Agent 노드 lacks the necessary specificity and context to guide the agent effectively in carrying out its intended tasks. A vague or overly general prompt can lead to irrelevant responses, difficulty in understanding user intent, and an inability to leverage tools or data appropriately.
* **예제:** You're building a travel booking agent, and your 시스템 Prompt simply states "_You are a helpful AI assistant._" This lacks the specific instructions and context needed for the agent to effectively guide users through flight searches, hotel bookings, and itinerary planning.
* **솔루션:** Craft a detailed and context-aware 시스템 Prompt:

{% code overflow="wrap" %}
```
You are a travel booking agent. Your primary goal is to assist users in planning and booking their trips. 
- Guide them through searching for flights, finding accommodations, and exploring destinations.
- Be polite, patient, and offer travel recommendations based on their preferences.
- Utilize available tools to access flight data, hotel availability, and destination information.
```
{% endcode %}
{% endtab %}
{% endtabs %}

***

## 5. LLM 노드

Like the Agent 노드, the LLM 노드 is a **core component of the Sequential Agent architecture**. Both nodes utilize the same Chat Models (LLMs) by default, providing the same basic language processing capabilities, but the LLM 노드 distinguishes itself in these key areas.

<figure><img src="../../../.gitbook/assets/sa-llm.png" alt="" width="341"><figcaption></figcaption></figure>

### 키 advantages of the LLM 노드

While a detailed comparison between the LLM 노드 and the Agent 노드 is available in [this section](./#agent-node-vs.-llm-node-selecting-the-optimal-node-for-conversational-tasks), here's a brief overview of the **LLM 노드's key advantages**:

* **Structured data:** The LLM 노드 provides a dedicated feature to define a JSON schema for its output. This makes it exceptionally easy to extract structured information from the LLM's responses and pass that data to consequent nodes in the workflow. The Agent 노드 does not have this built-in JSON schema feature
* **HITL:** While both nodes support HITL for tool execution, the LLM 노드 defers this control to the 도구 노드 itself, providing more flexibility in workflow design.

### Inputs

<table><thead><tr><th width="184"></th><th width="111">필수</th><th>설명</th></tr></thead><tbody><tr><td>Chat 모델</td><td>No</td><td>추가 a new Chat 모델 to <strong>overwrite the default Chat 모델</strong> (LLM) of the workflow. Only compatible with models that are capable of function calling.</td></tr><tr><td>Start 노드</td><td><strong>Yes</strong></td><td>Receives the <strong>initial user input</strong>, along with the custom 상태 (if set up) and the rest of the default <code>state.messages</code> array from the Start 노드.</td></tr><tr><td>Agent 노드</td><td><strong>Yes</strong></td><td>Receives output from an Agent 노드, which may include tool execution results or agent-generated responses.</td></tr><tr><td>조건 노드</td><td><strong>Yes</strong></td><td>Receives input from a preceding 조건 노드, enabling the LLM 노드 to <strong>take actions or guide the conversation based on the outcome of the 조건 노드's evaluation</strong>.</td></tr><tr><td>조건 Agent 노드</td><td><strong>Yes</strong></td><td>Receives input from a preceding 조건 Agent 노드, enabling the LLM 노드 to <strong>take actions or guide the conversation based on the outcome of the 조건 Agent 노드's evaluation</strong>.</td></tr><tr><td>LLM 노드</td><td><strong>Yes</strong></td><td>Receives output from another LLM 노드, <strong>enabling chained reasoning</strong> or information processing across multiple LLM Nodes.</td></tr><tr><td>도구 노드</td><td><strong>Yes</strong></td><td>Receives output from a 도구 노드, <strong>providing the results of tool execution for further processing</strong> or response generation.</td></tr></tbody></table>

{% hint style="info" %}
The **LLM 노드 requires at least one connection from the following nodes**: Start 노드, Agent 노드, 조건 노드, 조건 Agent 노드, LLM 노드, or 도구 노드.
{% endhint %}

### **노드 설정**

<table><thead><tr><th width="240"></th><th width="118">필수</th><th>설명</th></tr></thead><tbody><tr><td>LLM 노드 Name</td><td><strong>Yes</strong></td><td>추가 a descriptive name to the LLM 노드 to enhance workflow readability and easily <strong>target it back when using loops</strong> within the workflow.</td></tr></tbody></table>

### Outputs

The LLM 노드 can connect to the following nodes as outputs:

* **Agent 노드:** Passes the LLM's output to an Agent 노드, which can then use the information to decide on actions, execute tools, or guide the conversation flow.
* **LLM 노드:** Passes the output to a subsequent LLM 노드, enabling chaining of multiple LLM operations. This is useful for tasks like refining text generation, performing multiple analyses, or breaking down complex language processing into stages.
* **도구 노드**: Passes the output to a 도구 노드, enabling the execution of a specific tool based on the LLM 노드's instructions.
* **조건 Agent 노드:** Directs the flow to a 조건 Agent 노드. This node evaluates the LLM 노드's output and its predefined conditions to determine the appropriate next step in the workflow.
* **조건 노드:** Similar to the 조건 Agent 노드, the 조건 노드 uses predefined conditions to assess the LLM 노드's output, directing the flow along different branches based on the outcome.
* **End 노드:** Concludes the conversation flow.
* **루프 노드:** Redirects the flow back to a previous node, enabling iterative or cyclical processes within the workflow. This could be used to refine the LLM's output over multiple iterations.

### Additional 매개변수

<table><thead><tr><th width="200"></th><th width="141">필수</th><th>설명</th></tr></thead><tbody><tr><td>시스템 Prompt</td><td>No</td><td>Defines the <strong>agent's 'persona' and guides its behavior</strong>. For example, "<em>You are a customer service agent specializing in technical support</em> [...]."</td></tr><tr><td>Human Prompt</td><td>No</td><td>This prompt is appended to the <code>state.messages</code> array as a human message. It allows us to <strong>inject a human-like message into the conversation flow</strong> after the LLM 노드 has processed its input and before the next node receives the LLM 노드's output.</td></tr><tr><td>JSON Structured 출력</td><td>No</td><td>To instruct the LLM (Chat 모델) to <strong>provide the output in JSON structure schema</strong> (키, 타입, Enum Values, 설명).</td></tr><tr><td>업데이트 상태</td><td>No</td><td>Provides a <strong>mechanism to modify the shared custom 상태 object within the workflow</strong>. This is useful for storing information gathered by the LLM 노드 or influencing the behavior of subsequent nodes.</td></tr></tbody></table>

### 모범 사례

{% tabs %}
{% tab title="Pro Tips" %}
**삭제 system prompt**

Craft a concise and unambiguous 시스템 Prompt that accurately reflects the LLM 노드's role and capabilities. This guides the LLM 노드's decision-making and ensures it acts within its defined scope.

**Optimize for structured output**

Keep your JSON schemas as straightforward as possible, focusing on the essential data elements. Only enable JSON Structured 출력 when you need to extract specific data points from the LLM's response or when downstream nodes require JSON input.

**Strategic tool selection**

Choose and configure the tools available to the LLM 노드 (via the 도구 노드), ensuring they align with the application purpose and the overall goals of the workflow.

**HITL for sensitive tasks**

Utilize the 'Require Approval' option for tasks involving sensitive data, requiring human judgment, or carrying a risk of unintended consequences.

**Leverage 상태 updates**

업데이트 the custom 상태 object strategically to store gathered information or influence the behavior of downstream nodes.
{% endtab %}

{% tab title="Potential Pitfalls" %}
**Unintentional tool execution due to Incorrect HITL setup**

* **문제:** While the LLM 노드 can trigger 도구 Nodes, it relies on the 도구 노드's configuration for Human-in-the-루프 (HITL) approval. Failing to properly configure HITL for sensitive actions can lead to tools being executed without human review, potentially causing unintended consequences.
* **예제:** Your LLM 노드 is designed to interact with a tool that makes changes to user data. You intend to have a human review these changes before execution, but the connected 도구 노드's "Require Approval" option is not enabled. This could result in the tool automatically modifying user data based solely on the LLM's output, without any human oversight.
* **솔루션**
  1. **Double-Check tool node settings:** Always ensure that the "Require Approval" option is enabled within the settings of any 도구 노드 that handles sensitive actions.
  2. **Test HITL thoroughly:** Before deploying your workflow, test the HITL process to ensure that human review steps are triggered as expected and that the approval/rejection mechanism functions correctly.

**Overuse or misunderstanding of JSON structured output**

* **문제:** While the LLM 노드's JSON Structured 출력 feature is powerful, misusing it or not fully understanding its implications can lead to data errors.
* **예제:** You define a complex JSON schema for the LLM 노드's output, even though the downstream tasks only require a simple text response. This adds unnecessary complexity and makes your workflow harder to understand and maintain. Additionally, if the LLM's output doesn't conform to the defined schema, it can cause errors in subsequent nodes.
* **솔루션**
  1. **Use JSON output strategically:** Only enable JSON Structured 출력 when you have a clear need to extract specific data points from the LLM's response or when the downstream 도구 Nodes require JSON input.
  2. **Keep schemas simple:** 설계 your JSON schemas to be as simple and concise as possible, focusing only on the data elements that are absolutely necessary for the task.
{% endtab %}
{% endtabs %}

***

## 6. 도구 노드

The 도구 노드 is a valuable component of Flowise's Sequential Agent system, **enabling the integration and execution of external tools** within conversational workflows. It acts as a bridge between the language-based processing of LLM Nodes and the specialized functionalities of external tools, APIs, or services.

<figure><img src="../../../.gitbook/assets/seq-07.png" alt="" width="300"><figcaption></figcaption></figure>

### Understanding the 도구 노드

The 도구 노드's primary function is to **execute external tools** based on instructions received from an LLM 노드 and to **provide flexibility for Human-in-the-루프 (HITL)** intervention in the tool execution process.

#### Here's a step-by-step explanation of how it works

1. **도구 Call Reception:** The 도구 노드 receives input from an LLM 노드. If the LLM's output contains the `tool_calls` property, the 도구 노드 will proceed with tool execution.
2. **실행:** The 도구 노드 directly passes the LLM's `tool_calls` (which include the tool name and any required parameters) to the specified external tool. Otherwise, the 도구 노드 does not execute any tools in that particular workflow execution. It does not process or interpret the LLM's output in any way.
3. **Human-in-the-루프 (HITL):** The 도구 노드 allows for optional HITL, enabling human review and approval or rejection of tool execution before it occurs.
4. **출력 passing:** After the tool execution (either automatic or after HITL approval), the 도구 노드 receives the tool's output and passes it to the next node in the workflow. If the 도구 노드's output is not connected to a subsequent node, the tool's output is returned to the original LLM 노드 for further processing.

### Inputs

<table><thead><tr><th width="164"></th><th width="107">필수</th><th>설명</th></tr></thead><tbody><tr><td>LLM 노드</td><td><strong>Yes</strong></td><td>Receives the output from an LLM 노드, which may or may not contain <code>tool_calls</code> property. If it is present, the 도구 노드 will use them to execute the specified tool.</td></tr><tr><td>External Tools</td><td>No</td><td>Provides the 도구 노드 with <strong>access to a suite of external tools</strong>, enabling it to perform actions and retrieve information.</td></tr></tbody></table>

### 노드 설정

<table><thead><tr><th width="183"></th><th width="101">필수</th><th>설명</th></tr></thead><tbody><tr><td>도구 노드 Name</td><td><strong>Yes</strong></td><td>추가 a descriptive name to the 도구 노드 to enhance workflow readability.</td></tr><tr><td>Require Approval (HITL)</td><td>No</td><td><strong>Activates the Human-in-the-loop (HITL) feature</strong>. If set to '<strong>True</strong>,' the 도구 노드 will request human approval before executing any tool. This is particularly valuable for sensitive operations or when human oversight is desired. Defaults to '<strong>False</strong>,' allowing the 도구 노드 to execute tools autonomously.</td></tr></tbody></table>

### Outputs

The 도구 노드 can connect to the following nodes as outputs:

* **Agent 노드:** Passes the 도구 노드's output (the result of the executed tool) to an Agent 노드. The Agent 노드 can then use this information to decide on actions, execute further tools, or guide the conversation flow.
* **LLM 노드:** Passes the output to a subsequent LLM 노드. This enables the integration of tool results into the LLM's processing, allowing for further analysis or refinement of the conversation flow based on the tool's output.
* **조건 Agent 노드:** Directs the flow to a 조건 tool 노드. This node evaluates the 도구 노드's output and its predefined conditions to determine the appropriate next step in the workflow.
* **조건 노드:** Similar to the 조건 Agent 노드, the 조건 노드 uses predefined conditions to assess the 도구 노드's output, directing the flow along different branches based on the outcome.
* **End 노드:** Concludes the conversation flow.
* **루프 노드:** Redirects the flow back to a previous node, enabling iterative or cyclical processes within the workflow. This could be used for tasks that require multiple tool executions or involve refining the conversation based on tool results.

### Additional 매개변수

<table><thead><tr><th width="200"></th><th width="102">필수</th><th>설명</th></tr></thead><tbody><tr><td>Approval Prompt</td><td>No</td><td><strong>A customizable prompt presented to the human reviewer when the HITL feature is active</strong>. This prompt provides context about the tool execution, including the tool's name and purpose. The variable <code>{tools}</code> within the prompt will be dynamically replaced with the actual list of tools suggested by the LLM 노드, ensuring the human reviewer has all necessary information to make an informed decision.</td></tr><tr><td>Approve 버튼 Text</td><td>No</td><td>Customizes <strong>the text displayed on the button for approving tool execution</strong> in the HITL interface. This allows for tailoring the language to the specific context and ensuring clarity for the human reviewer.</td></tr><tr><td>Reject 버튼 Text</td><td>No</td><td>Customizes the <strong>text displayed on the button for rejecting tool execution</strong> in the HITL interface. Like the Approve 버튼 Text, this customization enhances clarity and provides a clear action for the human reviewer to take if they deem the tool execution unnecessary or potentially harmful.</td></tr><tr><td>업데이트 상태</td><td>No</td><td>Provides a <strong>mechanism to modify the custom 상태 object within the workflow</strong>. This is useful for storing information gathered by the 도구 노드 (after the tool execution) or influencing the behavior of subsequent nodes.</td></tr></tbody></table>

### 모범 사례

{% tabs %}
{% tab title="Pro Tips" %}
**Strategic HITL placement**

Consider which tools require human oversight (HITL) and enable the "Require Approval" option accordingly.

**Informative Approval Prompts**

When using HITL, design clear and informative prompts for human reviewers. Provide sufficient context from the conversation and summarize the tool's intended action.
{% endtab %}

{% tab title="Potential Pitfalls" %}
**Unhandled tool output formats**

* **문제:** The 도구 노드 outputs data in a format that is not expected or handled by subsequent nodes in the workflow, leading to errors or incorrect processing.
* **예제:** A 도구 노드 retrieves data from an API in JSON format, but the following LLM 노드 expects text input, causing a parsing error.
* **솔루션:** Ensure that the output format of the external tool is compatible with the input requirements of the nodes connected to the 도구 노드's output.
{% endtab %}
{% endtabs %}

***

## 7. 조건 노드

The 조건 노드 acts as a **decision-making point in Sequential Agent workflows**, evaluating a set of predefined conditions to determine the flow's next path.

<figure><img src="../../../.gitbook/assets/seq-08.png" alt="" width="299"><figcaption></figcaption></figure>

### Understanding the 조건 노드

The 조건 노드 is essential for building workflows that adapt to different situations and user inputs. It examines the current 상태 of the conversation, which includes all messages exchanged and any custom 상태 variables previously defined. Then, based on the evaluation of the conditions specified in the node setup, the 조건 노드 directs the flow to one of its outputs.

For instance, after an Agent or LLM 노드 provides a response, a 조건 노드 could check if the response contains a specific keyword or if a certain condition is met in the custom 상태. If it does, the flow might be directed to an Agent 노드 for further action. If not, it could lead to a different path, perhaps ending the conversation or prompting the user with additional questions.

This enables us to **create branches in our workflow**, where the path taken depends on the data flowing through the system.

#### Here's a step-by-step explanation of how it works

1. The 조건 노드 receives input from any preceding node: Start 노드, Agent 노드, LLM 노드, or 도구 노드.
2. It has access to the full conversation history and the custom 상태 (if any), giving it plenty of context to work with.
3. We define a condition that the node will evaluate. This could be checking for keywords, comparing values in the state, or any other logic we could implement via JavaScript.
4. Based on whether the condition evaluates to **true** or **false**, the 조건 노드 sends the flow down one of its predefined output paths. This creates a "fork in the road" or branch for our workflow.

### How to set up conditions

The 조건 노드 allows us to define dynamic branching logic in our workflow by choosing either a **table-based interface** or a **JavaScript code editor** to define the conditions that will control the conversation flow.

<figure><img src="../../../.gitbook/assets/seq-16 (1).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>조건 using CODE</summary>

The **조건 노드 uses JavaScript** to evaluate specific conditions within the conversation flow.

We can set up conditions based on keywords, 상태 changes, or other factors to dynamically guide the workflow to different branches based on the context of the conversation. Here are some examples:

**Keyword condition**

This checks if a specific word or phrase exists in the conversation history.

* **예제:** We want to check if the user said "yes" in their last message.

{% code overflow="wrap" %}
```javascript
const lastMessage = $flow.state.messages[$flow.state.messages.length - 1].content; 
return lastMessage.includes("yes") ? "Output 1" : "Output 2";
```
{% endcode %}

1. This code gets the last message from state.messages and checks if it contains "yes".
2. If "yes" is found, the flow goes to "출력 1"; otherwise, it goes to "출력 2".

**상태 change condition**

This checks if a specific value in the custom 상태 has changed to a desired value.

* **예제:** We're tracking an orderStatus variable our custom 상태, and we want to check if it has become "confirmed".

{% code overflow="wrap" %}
```javascript
return $flow.state.orderStatus === "confirmed" ? "Output 1" : "Output 2";
```
{% endcode %}

1. This code directly compares the orderStatus value in our custom 상태 to "confirmed".
2. If it matches, the flow goes to "출력 1"; otherwise, it goes to "출력 2".

</details>

<details>

<summary>조건 using TABLE</summary>

The 조건 노드 allows us to define conditions using a **user-friendly table interface**, making it easy to create dynamic workflows without writing JavaScript code.

You can set up conditions based on keywords, 상태 changes, or other factors to guide the conversation flow along different branches. Here are some examples:

**Keyword condition**

This checks if a specific word or phrase exists in the conversation history.

* **예제:** We want to check if the user said "yes" in their last message.
*   **설정**

    <table data-header-hidden><thead><tr><th width="294"></th><th width="116"></th><th width="99"></th><th></th></tr></thead><tbody><tr><td><strong>변수</strong></td><td><strong>작업</strong></td><td><strong>값</strong></td><td><strong>출력 Name</strong></td></tr><tr><td>$flow.state.messages[-1].content</td><td>Is</td><td>Yes</td><td>출력 1</td></tr></tbody></table>

    1. This table entry checks if the content (.content) of the last message (\[-1]) in `state.messages` is equal to "Yes".
    2. If the condition is met, the flow goes to "출력 1". Otherwise, the workflow is directed to a default "End" output.

**상태 change condition**

This checks if a specific value in our custom 상태 has changed to a desired value.

* **예제:** We're tracking an orderStatus variable in our custom 상태, and we want to check if it has become "confirmed".
*   **설정**

    <table data-header-hidden><thead><tr><th width="266"></th><th width="113"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>변수</strong></td><td><strong>작업</strong></td><td><strong>값</strong></td><td><strong>출력 Name</strong></td></tr><tr><td>$flow.state.orderStatus</td><td>Is</td><td>Confirmed</td><td>출력 1</td></tr></tbody></table>

    1. This table entry checks if the value of orderStatus in the custom 상태 is equal to "confirmed".
    2. If the condition is met, the flow goes to "출력 1". Otherwise, the workflow is directed to a default "End" output.

</details>

### Defining conditions using the table interface

This visual approach allows you to easily set up rules that determine the path of your conversational flow, based on factors like user input, the current state of the conversation, or the results of actions taken by other nodes.

<details>

<summary>테이블-Based: 조건 노드</summary>

*   **업데이트됨 on 09/08/2024**

    <table><thead><tr><th width="134"></th><th width="189">설명</th><th>Options/구문</th></tr></thead><tbody><tr><td><strong>변수</strong></td><td>The variable or data element to evaluate in the condition.</td><td>- <code>$flow.state.messages.length</code> (Total Messages)<br>- <code>$flow.state.messages[0].con</code> (First 메시지 Content)<br>- <code>$flow.state.messages[-1].con</code> (Last 메시지 Content)<br>- <code>$vars.&#x3C;variable-name></code> (전역 variable)</td></tr><tr><td><strong>작업</strong></td><td>The comparison or logical operation to perform on the variable.</td><td>- Contains<br>- Not Contains<br>- Start With<br>- End With<br>- Is<br>- Is Not<br>- Is Empty<br>- Is Not Empty<br>- Greater Than<br>- Less Than<br>- Equal To<br>- Not Equal To<br>- Greater Than or Equal To<br>- Less Than or Equal To</td></tr><tr><td><strong>값</strong></td><td>The value to compare the variable against.</td><td>- Depends on the data type of the variable and the selected operation.<br>- 예제: "yes", 10, "Hello"</td></tr><tr><td><strong>출력 Name</strong></td><td>The name of the output path to follow if the condition evaluates to <code>true</code>.</td><td>- 사용자-defined name (e.g., "Agent1", "End", "루프")</td></tr></tbody></table>

</details>

### Inputs

<table><thead><tr><th width="167"></th><th width="118">필수</th><th>설명</th></tr></thead><tbody><tr><td>Start 노드</td><td><strong>Yes</strong></td><td>Receives the 상태 from the Start 노드. This allows the 조건 노드 to <strong>evaluate conditions based on the initial context of the conversation</strong>, including any custom 상태.</td></tr><tr><td>Agent 노드</td><td><strong>Yes</strong></td><td>Receives the Agent 노드's output. This enables the 조건 노드 to <strong>make decisions based on the agent's actions</strong> and the conversation history, including any custom 상태.</td></tr><tr><td>LLM 노드</td><td><strong>Yes</strong></td><td>Receives the LLM 노드's output. This allows the 조건 노드 to <strong>evaluate conditions based on the LLM's response</strong> and the conversation history, including any custom 상태.</td></tr><tr><td>도구 노드</td><td><strong>Yes</strong></td><td>Receives the 도구 노드's output. This enables the 조건 노드 to <strong>make decisions based on the results of tool execution</strong> and the conversation history, including any custom 상태.</td></tr></tbody></table>

{% hint style="info" %}
The **조건 노드 requires at least one connection from the following nodes**: Start 노드, Agent 노드, LLM 노드, or 도구 노드.
{% endhint %}

### Outputs

The 조건 노드 **dynamically determines its output path based on the predefined conditions**, using either the table-based interface or JavaScript. This provides flexibility in directing the workflow based on condition evaluations.

#### 조건 evaluation logic

* **테이블-Based conditions:** The conditions in the table are evaluated sequentially, from top to bottom. The first condition that evaluates to true triggers its corresponding output. If none of the predefined conditions are met, the workflow is directed to the default "End" output.
* **Code-Based conditions:** When using JavaScript, we must explicitly return the name of the desired output path, including a name for the default "End" output.
* **Single output path:** Only one output path is activated at a time. Even if multiple conditions could be true, only the first matching condition determines the flow.

#### Connecting outputs

Each predefined output, including the default "End" output, can be connected to any of the following nodes:

* **Agent 노드:** To continue the conversation with an agent, potentially taking actions based on the condition's outcome.
* **LLM 노드:** To process the current 상태 and conversation history with an LLM, generating responses or making further decisions.
* **End 노드:** To terminate the conversation flow. If any output, including the default "End" output, is connected to an End 노드, the 조건 노드 will output the last response from the preceding node and end the workflow.
* **루프 노드:** To redirect the flow back to a previous sequential node, enabling iterative processes based on the condition's outcome.

### 노드 설정

<table><thead><tr><th width="178"></th><th width="110">필수</th><th>설명</th></tr></thead><tbody><tr><td>조건 노드 Name</td><td>No</td><td>An optional, <strong>human-readable name</strong> for the condition being evaluated. This is helpful for understanding the workflow at a glance.</td></tr><tr><td>조건</td><td><strong>Yes</strong></td><td>This is where we <strong>define the logic that will be evaluated to determine the output paths</strong>.</td></tr></tbody></table>

### 모범 사례

{% tabs %}
{% tab title="Pro Tips" %}
**삭제 condition naming**

Use descriptive names for your conditions (e.g., "If user is under 18, then 정책 Advisor Agent", "If order is confirmed, then End 노드") to make your workflow easier to understand and debug.

**Prioritize simple conditions**

Start with simple conditions and gradually add complexity as needed. This makes your workflow more manageable and reduces the risk of errors.
{% endtab %}

{% tab title="Potential Pitfalls" %}
**Mismatched condition logic and workflow design**

* **문제:** The conditions you define in the 조건 노드 do not accurately reflect the intended logic of your workflow, leading to unexpected branching or incorrect execution paths.
* **예제:** You set up a condition to check if the user's age is greater than 18, but the output path for that condition leads to a section designed for users under 18.
* **솔루션:** Review your conditions and ensure that the output paths associated with each condition match the intended workflow logic. Use clear and descriptive names for your outputs to avoid confusion.

**Insufficient 상태 management**

* **문제:** The 조건 노드 relies on a custom state variable that is not updated correctly, leading to inaccurate condition evaluations and incorrect branching.
* **예제:** You're tracking a "userLocation" variable in the custom 상태, but the variable is not updated when the user provides their location. The 조건 노드 evaluates the condition based on the outdated value, leading to an incorrect path.
* **솔루션:** Ensure that any custom state variables used in your conditions are updated correctly throughout the workflow.
{% endtab %}
{% endtabs %}

***

## 8. 조건 Agent 노드

The 조건 Agent 노드 provides **dynamic and intelligent routing within Sequential Agent flows**. It combines the capabilities of the **LLM 노드** (LLM and JSON Structured 출력) and the **조건 노드** (user-defined conditions), allowing us to leverage agent-based reasoning and conditional logic within a single node.

<figure><img src="../../../.gitbook/assets/seq-09.png" alt="" width="299"><figcaption></figcaption></figure>

### 키 functionalities

* **Unified agent-based routing:** Combines agent reasoning, structured output, and conditional logic in a single node, simplifying workflow design.
* **Contextual awareness:** The agent considers the entire conversation history and any custom 상태 when evaluating conditions.
* **Flexibility:** Provides both table-based and code-based options for defining conditions, when catering to different user preferences and skill levels.

### 설정 up the 조건 Agent 노드

The 조건 Agent 노드 acts as a specialized agent that can both **process information and make routing decisions**. Here's how to configure it:

1. **정의 the agent's persona**
   * In the "시스템 Prompt" field, provide a clear and concise description of the agent's role and the task it needs to perform for conditional routing. This prompt will guide the agent's understanding of the conversation and its decision-making process.
2. **Structure the Agent's 출력 (선택 사항)**
   * If you want the agent to produce structured output, use the "JSON Structured 출력" feature. 정의 the desired schema for the output, specifying the keys, data types, and any enum values. This structured output will be used by the agent when evaluating conditions.
3. **정의 conditions**
   * Choose either the table-based interface or the JavaScript code editor to define the conditions that will determine the routing behavior.
     * **테이블-Based interface:** 추가 rows to the table, specifying the variable to check, the comparison operation, the value to compare against, and the output name to follow if the condition is met.
     * **JavaScript code:** Write custom JavaScript snippets to evaluate conditions. Use the `return` statement to specify the name of the output path to follow based on the condition's result.
4. **Connect outputs**
   * Connect each predefined output, including the default "End" output, to the appropriate subsequent node in the workflow. This could be an Agent 노드, LLM 노드, 루프 노드, or an End 노드.

### How to set up conditions

The 조건 Agent 노드 allows us to define dynamic branching logic in our workflow by choose either a **table-based interface** or a **JavaScript code editor** to define the conditions that will control the conversation flow.

<figure><img src="../../../.gitbook/assets/seq-16 (1).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>조건 using CODE</summary>

The 조건 Agent 노드, like the 조건 노드, **uses JavaScript code to evaluate specific conditions** within the conversation flow.

However, the 조건 Agent 노드 can evaluate conditions based on a wider range of factors, including keywords, state changes, and the content of its own output (either as free-form text or structured JSON data). This allows for more nuanced and context-aware routing decisions. Here are some examples:

**Keyword condition**

This checks if a specific word or phrase exists in the conversation history.

* **예제:** We want to check if the user said "yes" in their last message.

{% code overflow="wrap" %}
```javascript
const lastMessage = $flow.state.messages[$flow.state.messages.length - 1].content; 
return lastMessage.includes("yes") ? "Output 1" : "Output 2";
```
{% endcode %}

1. This code gets the last message from state.messages and checks if it contains "yes".
2. If "yes" is found, the flow goes to "출력 1"; otherwise, it goes to "출력 2".

**상태 change condition**

This checks if a specific value in the custom 상태 has changed to a desired value.

* **예제:** We're tracking an orderStatus variable our custom 상태, and we want to check if it has become "confirmed".

{% code overflow="wrap" %}
```javascript
return $flow.state.orderStatus === "confirmed" ? "Output 1" : "Output 2";
```
{% endcode %}

1. This code directly compares the orderStatus value in our custom 상태 to "confirmed".
2. If it matches, the flow goes to "출력 1"; otherwise, it goes to "출력 2".

</details>

<details>

<summary>조건 using TABLE</summary>

The 조건 Agent 노드 also provides a **user-friendly table interface for defining conditions**, similar to the 조건 노드. You can set up conditions based on keywords, state changes, or the agent's own output, allowing you to create dynamic workflows without writing JavaScript code.

This table-based approach simplifies condition management and makes it easier to visualize the branching logic. Here are some examples:

**Keyword condition**

This checks if a specific word or phrase exists in the conversation history.

* **예제:** We want to check if the user said "yes" in their last message.
*   **설정**

    <table data-header-hidden><thead><tr><th width="305"></th><th width="116"></th><th width="99"></th><th></th></tr></thead><tbody><tr><td><strong>변수</strong></td><td><strong>작업</strong></td><td><strong>값</strong></td><td><strong>출력 Name</strong></td></tr><tr><td>$flow.state.messages[-1].content</td><td>Is</td><td>Yes</td><td>출력 1</td></tr></tbody></table>

    1. This table entry checks if the content (.content) of the last message (\[-1]) in `state.messages` is equal to "Yes".
    2. If the condition is met, the flow goes to "출력 1". Otherwise, the workflow is directed to a default "End" output.

**상태 change condition**

This checks if a specific value in our custom 상태 has changed to a desired value.

* **예제:** We're tracking an orderStatus variable in our custom 상태, and we want to check if it has become "confirmed".
*   **설정**

    <table data-header-hidden><thead><tr><th width="266"></th><th width="113"></th><th></th><th></th></tr></thead><tbody><tr><td><strong>변수</strong></td><td><strong>작업</strong></td><td><strong>값</strong></td><td><strong>출력 Name</strong></td></tr><tr><td>$flow.state.orderStatus</td><td>Is</td><td>Confirmed</td><td>출력 1</td></tr></tbody></table>

    1. This table entry checks if the value of orderStatus in the custom 상태 is equal to "confirmed".
    2. If the condition is met, the flow goes to "출력 1". Otherwise, the workflow is directed to a default "End" output.

</details>

### Defining conditions using the table interface

This visual approach allows you to easily set up rules that determine the path of your conversational flow, based on factors like user input, the current state of the conversation, or the results of actions taken by other nodes.

<details>

<summary>테이블-Based: 조건 Agent 노드</summary>

*   **업데이트됨 on 09/08/2024**

    <table><thead><tr><th width="125"></th><th width="186">설명</th><th>Options/구문</th></tr></thead><tbody><tr><td><strong>변수</strong></td><td>The variable or data element to evaluate in the condition. This can include data from the agent's output.</td><td>- <code>$flow.output.content</code> (Agent 출력 - string)<br>- <code>$flow.output.&#x3C;replace-with-key></code> (Agent's JSON 키 출력 - string/number)<br>- <code>$flow.state.messages.length</code> (Total Messages)<br>- <code>$flow.state.messages[0].con</code> (First 메시지 Content)<br>- <code>$flow.state.messages[-1].con</code> (Last 메시지 Content)<br>- <code>$vars.&#x3C;variable-name></code> (전역 variable)</td></tr><tr><td><strong>작업</strong></td><td>The comparison or logical operation to perform on the variable.</td><td>- Contains<br>- Not Contains<br>- Start With<br>- End With<br>- Is<br>- Is Not<br>- Is Empty<br>- Is Not Empty<br>- Greater Than<br>- Less Than<br>- Equal To<br>- Not Equal To<br>- Greater Than or Equal To<br>- Less Than or Equal To</td></tr><tr><td><strong>값</strong></td><td>The value to compare the variable against.</td><td>- Depends on the data type of the variable and the selected operation.<br>- 예제: "yes", 10, "Hello"</td></tr><tr><td><strong>출력 Name</strong></td><td>The name of the output path to follow if the condition evaluates to <code>true</code>.</td><td>- 사용자-defined name (e.g., "Agent1", "End", "루프")</td></tr></tbody></table>

</details>

### Inputs

<table><thead><tr><th width="167"></th><th width="118">필수</th><th>설명</th></tr></thead><tbody><tr><td>Start 노드</td><td>Yes</td><td>Receives the 상태 from the Start 노드. This allows the 조건 Agent 노드 to <strong>evaluate conditions based on the initial context</strong> of the conversation, including any custom 상태.</td></tr><tr><td>Agent 노드</td><td>Yes</td><td>Receives the Agent 노드's output. This enables the 조건 Agent 노드 to <strong>make decisions based on the agent's actions</strong> and the conversation history, including any custom 상태.</td></tr><tr><td>LLM 노드</td><td>Yes</td><td>Receives LLM 노드's output. This allows the 조건 Agent 노드 to <strong>evaluate conditions based on the LLM's response</strong> and the conversation history, including any custom 상태.</td></tr><tr><td>도구 노드</td><td>Yes</td><td>Receives the 도구 노드's output. This enables the 조건 Agent 노드 to <strong>make decisions based on the results of tool execution</strong> and the conversation history, including any custom 상태.</td></tr></tbody></table>

{% hint style="info" %}
The **조건 Agent 노드 requires at least one connection from the following nodes**: Start 노드, Agent 노드, LLM 노드, or 도구 노드.
{% endhint %}

### 노드 설정

<table><thead><tr><th width="178">매개변수</th><th width="110">필수</th><th>설명</th></tr></thead><tbody><tr><td>Name</td><td>No</td><td>추가 a descriptive name to the 조건 Agent 노드 to enhance workflow readability and easily.</td></tr><tr><td>조건</td><td><strong>Yes</strong></td><td>This is where we <strong>define the logic that will be evaluated to determine the output paths</strong>.</td></tr></tbody></table>

### Outputs

The 조건 Agent 노드, like the 조건 노드, **dynamically determines its output path based on the conditions defined**, using either the table-based interface or JavaScript. This provides flexibility in directing the workflow based on condition evaluations.

#### 조건 evaluation logic

* **테이블-Based conditions:** The conditions in the table are evaluated sequentially, from top to bottom. The first condition that evaluates to true triggers its corresponding output. If none of the predefined conditions are met, the workflow is directed to the default "End" output.
* **Code-Based conditions:** When using JavaScript, we must explicitly return the name of the desired output path, including a name for the default "End" output.
* **Single output path:** Only one output path is activated at a time. Even if multiple conditions could be true, only the first matching condition determines the flow.

#### Connecting outputs

Each predefined output, including the default "End" output, can be connected to any of the following nodes:

* **Agent 노드:** To continue the conversation with an agent, potentially taking actions based on the condition's outcome.
* **LLM 노드:** To process the current 상태 and conversation history with an LLM, generating responses or making further decisions.
* **End 노드:** To terminate the conversation flow. If the default "End" output is connected to an End 노드, the 조건 노드 will output the last response from the preceding node and end the conversation.
* **루프 노드:** To redirect the flow back to a previous sequential node, enabling iterative processes based on the condition's outcome.

#### 키 differences from the 조건 노드

* The 조건 **Agent 노드 incorporates an agent's reasoning** and structured output into the condition evaluation process.
* It provides a more integrated approach to agent-based condition routing.

### Additional 매개변수

<table><thead><tr><th width="180"></th><th width="111">필수</th><th>설명</th></tr></thead><tbody><tr><td>시스템 Prompt</td><td>No</td><td><strong>Defines the 조건 Agent's 'persona' and guides its behavior for making routing decisions.</strong> For example: "You are a customer service agent specializing in technical support. Your goal is to help customers with technical issues related to our product. Based on the user's query, identify the specific technical issue (e.g., connectivity problems, software bugs, hardware malfunctions)."</td></tr><tr><td>Human Prompt</td><td>No</td><td>This prompt is appended to the <code>state.messages</code> array as a human message. It allows us to <strong>inject a human-like message into the conversation flow</strong> after the 조건 Agent 노드 has processed its input and before the next node receives the 조건 Agent 노드's output.</td></tr><tr><td>JSON Structured 출력</td><td>No</td><td>To instruct the 조건 Agent 노드 to <strong>provide the output in JSON structure schema</strong> (키, 타입, Enum Values, 설명).</td></tr></tbody></table>

### 모범 사례

{% tabs %}
{% tab title="Pro Tips" %}
**Craft a clear and focused system prompt**

Provide a well-defined persona and clear instructions to the agent in the 시스템 Prompt. This will guide its reasoning and help it generate relevant output for the conditional logic.

**Structure output for reliable conditions**

Use the JSON Structured 출력 feature to define a schema for the 조건 Agent's output. This will ensure that the output is consistent and easily parsable, making it more reliable for use in conditional evaluations.
{% endtab %}

{% tab title="Potential Pitfalls" %}
**Unreliable routing due to unstructured output**

* **문제:** The 조건 Agent 노드 is not configured to output structured JSON data, leading to unpredictable output formats that can make it difficult to define reliable conditions.
* **예제:** The 조건 Agent 노드 is asked to determine user sentiment (positive, negative, neutral) but outputs its assessment as a free-form text string. The variability in the agent's language makes it challenging to create accurate conditions in the conditional table or code.
* **솔루션:** Use the JSON Structured 출력 feature to define a schema for the agent's output. For example, specify a "sentiment" key with an enum of "positive," "negative," and "neutral." This will ensure that the agent's output is consistently structured, making it much easier to create reliable conditions.
{% endtab %}
{% endtabs %}

***

## 9. 루프 노드

The 루프 노드 allows us to create loops within our conversational flow, **redirecting the conversation back to a specific point**. This is useful for scenarios where we need to repeat a certain sequence of actions or questions based on user input or specific conditions.

<figure><img src="../../../.gitbook/assets/sa-loop.png" alt="" width="335"><figcaption></figcaption></figure>

### Understanding the 루프 노드

The 루프 노드 acts as a connector, redirecting the flow back to a specific point in the graph, allowing us to create loops within our conversational flow. **It passes the current 상태, which includes the output of the node preceding the 루프 노드 to our target node.** This data transfer allows our target node to process information from the previous iteration of the loop and adjust its behavior accordingly.

For instance, let's say we're building a chatbot that helps users book flights. We might use a loop to iteratively refine the search criteria based on user feedback.

#### Here's how the 루프 노드 could be used

1. **LLM 노드 (Initial 검색):** The LLM 노드 receives the user's initial flight request (e.g., "찾기 flights from Madrid to New York in July"). It queries a flight search API and returns a list of possible flights.
2. **Agent 노드 (Present Options):** The Agent 노드 presents the flight options to the user and asks if they would like to refine their search (e.g., "would you like to filter by price, airline, or departure time?").
3. **조건 Agent 노드:** The 조건 Agent 노드 checks the user's response and has two outputs:
   * **If the user wants to refine:** The flow goes to the "Refine 검색" LLM 노드.
   * **If the user is happy with the results:** The flow proceeds to the booking process.
4. **LLM 노드 (Refine 검색):** This LLM 노드 gathers the user's refinement criteria (e.g., "Show me only flights under $500") and updates the 상태 with the new search parameters.
5. **루프 노드:** The 루프 노드 redirects the flow back to the initial LLM 노드 ("Initial 검색"). It passes the updated 상태, which now includes the refined search criteria.
6. **반복:** The initial LLM 노드 performs a new search using the refined criteria, and the process repeats from step 2.

**In this example, the 루프 노드 enables an iterative search refinement process.** The system can continue to loop back and refine the search results until the user is satisfied with the options presented.

### Inputs

<table><thead><tr><th width="197"></th><th width="104">필수</th><th>설명</th></tr></thead><tbody><tr><td>Agent 노드</td><td><strong>Yes</strong></td><td>Receives the output of a preceding Agent 노드. This data is then sent back to the target node specified in the "루프 To" parameter.</td></tr><tr><td>LLM 노드</td><td><strong>Yes</strong></td><td>Receives the output of a preceding LLM 노드. This data is then sent back to the target node specified in the "루프 To" parameter.</td></tr><tr><td>도구 노드</td><td><strong>Yes</strong></td><td>Receives the output of a preceding 도구 노드. This data is then sent back to the target node specified in the "루프 To" parameter.</td></tr><tr><td>조건 노드</td><td><strong>Yes</strong></td><td>Receives the output of a preceding 조건 노드. This data is then sent back to the target node specified in the "루프 To" parameter.</td></tr><tr><td>조건 Agent 노드</td><td><strong>Yes</strong></td><td>Receives the output of a preceding 조건 Agent 노드. This data is then sent back to the target node specified in the "루프 To" parameter.</td></tr></tbody></table>

{% hint style="info" %}
The **루프 노드 requires at least one connection from the following nodes**: Agent 노드, LLM 노드, 도구 노드, 조건 노드, or 조건 Agent 노드.
{% endhint %}

### 노드 설정

<table><thead><tr><th width="125"></th><th width="109">필수</th><th>설명</th></tr></thead><tbody><tr><td>루프 To</td><td><strong>Yes</strong></td><td>The 루프 노드 requires us to <strong>specify the target node</strong> ("루프 To") where the conversational flow should be redirected. This target node must be an <strong>Agent 노드</strong> or <strong>LLM 노드</strong>.</td></tr></tbody></table>

### Outputs

The **루프 노드 does not have any direct output connections**. It redirects the flow back to the specific sequential node in the graph.

### 모범 사례

{% tabs %}
{% tab title="Pro Tips" %}
**삭제 loop purpose**

정의 a clear purpose for each loop in your workflow. If possible, document with a sticky note what you're trying to achieve with the loop.
{% endtab %}

{% tab title="Potencial Pitfalls" %}
**Confusing workflow structure**

* **문제:** Excessive or poorly designed loops make the workflow difficult to understand and maintain.
* **예제:** You use multiple nested loops without clear purpose or labels, making it hard to follow the flow of the conversation.
* **솔루션:** Use loops sparingly and only when necessary. Clearly document your 루프 Nodes and the nodes they connect to.

**Infinite loops due to missing or incorrect exit conditions**

* **문제:** The loop never terminates because the condition that should trigger the loop's exit is either missing or incorrectly defined.
* **예제:** A 루프 노드 is used to iteratively gather user information. However, the workflow lacks a Conditional Agent 노드 to check if all required information has been collected. As a result, the loop continues indefinitely, repeatedly asking the user for the same information.
* **솔루션:** Always define clear and accurate exit conditions for loops. Use 조건 Nodes to check state variables, user input, or other factors that indicate when the loop should terminate.
{% endtab %}
{% endtabs %}

***

## 10. End 노드

The End 노드 marks the definitive **termination point of the conversation** in a Sequential Agent workflow. It signifies that no further processing, actions, or interactions are required.

<figure><img src="../../../.gitbook/assets/seq-end-node.png" alt="" width="375"><figcaption></figcaption></figure>

### Understanding the End 노드

The End 노드 serves as a signal within Flowise's Sequential Agent architecture, **indicating that the conversation has reached its intended conclusion**. Upon reaching the End 노드, the system "understands" that the conversational objective has been met, and no further actions or interactions are required within the flow.

### Inputs

<table><thead><tr><th width="212"></th><th width="103">필수</th><th>설명</th></tr></thead><tbody><tr><td>Agent 노드</td><td><strong>Yes</strong></td><td>Receives the final output from a preceding Agent 노드, indicating the end of the agent's processing.</td></tr><tr><td>LLM 노드</td><td><strong>Yes</strong></td><td>Receives the final output from a preceding LLM 노드, indicating the end of the LLM 노드's processing.</td></tr><tr><td>도구 노드</td><td><strong>Yes</strong></td><td>Receives the final output from a preceding 도구 노드, indicating the completion of the 도구 노드's execution.</td></tr><tr><td>조건 노드</td><td><strong>Yes</strong></td><td>Receives the final output from a preceding 조건 노드, indicating the end of the 조건 노드's execution.</td></tr><tr><td>조건 Agent 노드</td><td><strong>Yes</strong></td><td>Receives the final output from a preceding 조건 노드, indicating the completion of the 조건 Agent 노드's processing.</td></tr></tbody></table>

{% hint style="info" %}
The **End 노드 requires at least one connection from the following nodes**: Agent 노드, LLM 노드, or 도구 노드.
{% endhint %}

### Outputs

The **End 노드 does not have any output** connections as it signifies the termination of the information flow.

### 모범 사례

{% tabs %}
{% tab title="Pro Tips" %}
**Provide a final response**

If appropriate, connect the End 노드 to an dedicated LLM or Agent 노드 to generate a final message or summary for the user, providing closure to the conversation.
{% endtab %}

{% tab title="Potencial Pitfalls" %}
**Premature conversation termination**

* **문제:** The End 노드 is placed too early in the workflow, causing the conversation to end before all necessary steps are completed or the user's request is fully addressed.
* **예제:** A chatbot designed to collect user feedback ends the conversation after the user provides their first comment, without giving them an opportunity to provide additional feedback or ask questions.
* **솔루션:** Review your workflow logic and ensure that the End 노드 is placed only after all essential steps have been completed or the user has explicitly indicated their intent to end the conversation.

**Lack of closure for the user**

* **문제:** The conversation ends abruptly without a clear signal to the user or a final message that provides a sense of closure.
* **예제:** A customer support chatbot ends the conversation immediately after resolving an issue, without confirming the resolution with the user or offering further assistance.
* **솔루션:** Connect the End 노드 to a dedicate LLM or Agent 노드 to generate a final response that summarizes the conversation, confirms any actions taken, and provides a sense of closure for the user.
{% endtab %}
{% endtabs %}

***

## 조건 노드 vs. 조건 Agent 노드

The 조건 and 조건 Agent Nodes are essential in Flowise's Sequential Agent architecture for creating dynamic conversational experiences.

These nodes enable adaptive workflows, responding to user input, context, and complex decisions, but differ in their approach to condition evaluation and sophistication.

<details>

<summary><strong>조건 노드</strong></summary>

**Purpose**

To create branches based on simple, predefined logical conditions.

**조건 evaluation**

Uses a table-based interface or JavaScript code editor to define conditions that are checked against the custom 상태 and/or the full conversation history.

**출력 behavior**

* Supports multiple output paths, each associated with a specific condition.
* 조건 are evaluated in order. The first matching condition determines the output.
* If no conditions are met, the flow follows a default "End" output.

**Best suited for**

* Straightforward routing decisions based on easily definable conditions.
* Workflows where the logic can be expressed using simple comparisons, keyword checks, or custom state variable values.

</details>

<details>

<summary><strong>조건 Agent 노드</strong></summary>

**Purpose**

To create dynamic routing based on an agent's analysis of the conversation and its structured output.

**조건 evaluation**

* If no Chat 모델 is connected, it uses the default system LLM (from the Start 노드) to process the conversation history and any custom 상태.
* It can generate structured output, which is then used for condition evaluation.
* Uses a table-based interface or JavaScript code editor to define conditions that are checked against the agent's own output, structured or not.

**출력 behavior**

Same as the 조건 노드:

* Supports multiple output paths, each associated with a specific condition.
* 조건 are evaluated in order. The first matching condition determines the output.
* If no conditions are met, the flow follows the default "End" output.

**Best suited for**

* More complex routing decisions that require an understanding of conversation context, user intent, or nuanced factors.
* Scenarios where simple logical conditions are insufficient to capture the desired routing logic.
* **예제:** A chatbot needs to determine if a user's question is related to a specific product category. A 조건 Agent 노드 could be used to analyze the user's query and output a JSON object with a "category" field. The 조건 Agent 노드 can then use this structured output to route the user to the appropriate product specialist.

</details>

### Summarizing

<table><thead><tr><th width="218"></th><th width="258">조건 노드</th><th>조건 Agent 노드</th></tr></thead><tbody><tr><td><strong>Decision 논리</strong></td><td>Based on predefined logical conditions.</td><td>Based on agent's reasoning and structured output.</td></tr><tr><td><strong>Agent Involvement</strong></td><td>No agent involved in condition evaluation.</td><td>Uses an agent to process context and generate output for conditions.</td></tr><tr><td><strong>Structured 출력</strong></td><td>Not possible.</td><td>Possible and encouraged for reliable condition evaluation.</td></tr><tr><td><strong>조건 Evaluation</strong></td><td>Only define conditions that are checked against the full conversation history.</td><td>can define conditions that are checked against the agent's own output, structured or not.</td></tr><tr><td><strong>복잡도</strong></td><td>Suitable for simple branching logic.</td><td>Handles more nuanced and context-aware routing.</td></tr><tr><td><strong>Ideal Uses Cases</strong></td><td><ul><li>Routing based on user's age or a keyword in the conversation.</li></ul></td><td><ul><li>Routing based on user sentiment, intent, or complex contextual factors.</li></ul></td></tr></tbody></table>

### Choosing the right node

* **조건 노드:** Use the 조건 노드 when your routing logic involves straightforward decisions based on easily definable conditions. For instance, it's perfect for checking for specific keywords, comparing values in the 상태, or evaluating other simple logical expressions.
* **조건 Agent 노드:** However, when your routing demands a deeper understanding of the conversation's nuances, the 조건 Agent 노드 is the better choice. This node acts as your intelligent routing assistant, leveraging an LLM to analyze the conversation, make judgments based on context, and provide structured output that drives more sophisticated and dynamic routing.

***

## Agent 노드 vs. LLM 노드

It's important to understand that both the **LLM 노드 and the Agent 노드 can be considered agentic entities within our system**, as they both leverage the capabilities of a large language model (LLM) or Chat 모델.

However, while both nodes can process language and interact with tools, they are designed for different purposes within a workflow.

<details>

<summary>Agent 노드</summary>

**Focus**

The primary focus of the Agent 노드 to simulate the actions and decision-making of a human agent within a conversational context.

It acts as a high-level coordinator within the workflow, bringing together language understanding, tool execution, and decision-making to create a more human-like conversational experience.

**Strengths**

* Effectively manages the execution of multiple tools and integrates their results.
* Offers built-in support for Human-in-the-루프 (HITL), enabling human review and approval for sensitive operations.

**Best Suited For**

* Workflows where the agent needs to guide the user, gather information, make choices, and manage the overall conversation flow.
* Scenarios requiring integration with multiple external tools.
* Tasks involving sensitive data or actions where human oversight is beneficial, like approving financial transaction

</details>

<details>

<summary>LLM 노드</summary>

**Focus**

Similar to the Agent 노드, but it provides more flexibility when using tools and Human-in-the-루프 (HITL), both via the 도구 노드.

**Strengths**

* Enables the definition of JSON schemas to structure the LLM's output, making it easier to extract specific information.
* Offers flexibility in tool integration, allowing for more complex sequences of LLM and tool calls, and providing fine-grained control over the HITL feature.

**Best Suited For**

* Scenarios where structured data needs to be extracted from the LLM's response.
* Workflows requiring a mix of automated and human-reviewed tool executions. For example, an LLM 노드 might call a tool to retrieve product information (automated), and then a different tool to process a payment, which would require HITL approval.

</details>

### Summarizing

<table><thead><tr><th width="206"></th><th width="253">Agent 노드</th><th>LLM 노드</th></tr></thead><tbody><tr><td><strong>도구 Interaction</strong></td><td>Directly calls and manages multiple tools, built-in HITL.</td><td>Triggers tools via the 도구 노드, granular HITL control at the tool level.</td></tr><tr><td><strong>Human-in-the-루프 (HITL)</strong></td><td>HITL controlled at the Agent 노드 level (all connected tools affected).</td><td>HITL managed at the individual 도구 노드 level (more flexibility).</td></tr><tr><td><strong>Structured 출력</strong></td><td>Relies on the LLM's natural output format.</td><td>Relies on the LLM's natural output format, but, if needed, provides JSON schema definition to structure LLM output.</td></tr><tr><td><strong>Ideal Use Cases</strong></td><td><ul><li>Workflows with complex tool orchestration.</li><li>Simplified HITL at the Agent Level.</li></ul></td><td><ul><li>Extracting structured data from LLM output</li><li>Workflows with complex LLM and tool interactions, requiring mixed HITL levels.</li></ul></td></tr></tbody></table>

### Choosing the right node

* **Choose the Agent 노드:** Use the Agent 노드 when you need to create a conversational system that can manage the execution of multiple tools, all of which share the same HITL setting (enabled or disabled for the entire Agent 노드). The Agent 노드 is also well-suited for handling complex multi-step conversations where consistent agent-like behavior is desired.
* **Choose the LLM 노드:** On the other hand, use the LLM 노드 when you need to extract structured data from the LLM's output using the JSON schema feature, a capability not available in the Agent 노드. The LLM 노드 also excels at orchestrating tool execution with fine-grained control over HITL at the individual tool level, allowing you to mix automated and human-reviewed tool executions by using multiple 도구 Nodes connected to the LLM 노드.

[^1]: In our current context, a lower level of abstraction refers to a system that exposes a greater degree of implementation detail to the developer.
