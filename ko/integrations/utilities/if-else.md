# If Else

Flowise allows you to split your chatflow into different branches depending on If/Else condition.

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1).png" alt=""><figcaption></figcaption></figure>

### Input Variables

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

As noticed from the image above, it takes in any nodes that has `json` output. Some examples are: Custom 함수, LLM 체인 출력 예측, Get/집합 Variables.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

You can then give a variable name:

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

This variable can then be used in the [If 함수](if-else.md#if-function) and [Else 함수](if-else.md#else-function) with the prefix `$`. For example:

```
$output
```

### If Else Name

You can name the node for easier visualization of what it does.

### If 함수

This is a piece of JS code that is ran on 노드 sandbox. It must:

* Contains the `if` statement
* 반환 a value within `if` statement

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (2) (1) (1).png" alt="" width="312"><figcaption></figcaption></figure>

This gives much more flexibility for users to do complex comparison like regex, date comparsion and many more.

### Else 함수

Similar to If 함수, it must returns a value. This function will only be ran if the [If 함수](if-else.md#if-function) does not return a value.

<figure><img src="../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (2) (1) (1).png" alt="" width="317"><figcaption></figcaption></figure>

### 출력

<figure><img src="../../.gitbook/assets/image (8) (1) (1) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

When the [If 함수](if-else.md#if-function) successfully returns a value, it will be passed to the **True** output dot as shown above. This allow users to pass the value to the next node.

Otherwise, the returned value from [Else 함수](if-else.md#else-function) will be passed to the **False** output dot.

사용자 can also take a look at the If Else template in the marketplace:

<figure><img src="../../.gitbook/assets/image (9) (1) (1) (1) (1) (2) (1) (1).png" alt=""><figcaption></figcaption></figure>
