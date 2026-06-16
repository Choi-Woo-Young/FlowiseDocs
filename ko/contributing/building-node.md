# Node 빌드하기

### Git 설치

먼저 Git을 설치하고 Flowise 저장소를 클론합니다. [시작하기](/broken/pages/nuiTj70UthEELOvhLrSb#for-developers) 가이드의 단계를 따를 수 있습니다.

### 구조

Flowise는 모든 node 통합을 `packages/components/nodes` 폴더 아래에 분리합니다. 간단한 Tool을 만들어 봅시다!

### Calculator Tool 만들기

`packages/components/nodes/tools` 폴더 아래에 `Calculator`라는 새 폴더를 만듭니다. 그런 다음 `Calculator.ts`라는 새 파일을 만듭니다. 파일 내부에서 먼저 기본 class를 작성합니다.

```javascript
import { INode } from '../../../src/Interface'
import { getBaseClasses } from '../../../src/utils'

class Calculator_Tools implements INode {
    label: string
    name: string
    version: number
    description: string
    type: string
    icon: string
    category: string
    author: string
    baseClasses: string[]

    constructor() {
        this.label = 'Calculator'
        this.name = 'calculator'
        this.version = 1.0
        this.type = 'Calculator'
        this.icon = 'calculator.svg'
        this.category = 'Tools'
        this.author = 'Your Name'
        this.description = 'Perform calculations on response'
        this.baseClasses = [this.type, ...getBaseClasses(Calculator)]
    }
}

module.exports = { nodeClass: Calculator_Tools }
```

모든 node는 `INode` 기본 class를 구현합니다. 각 property가 의미하는 바는 다음과 같습니다:

<table><thead><tr><th width="271">Property</th><th>Description</th></tr></thead><tbody><tr><td>label</td><td>UI에 표시되는 node의 이름</td></tr><tr><td>name</td><td>코드에서 사용되는 이름. 반드시 <strong>camelCase</strong>여야 합니다</td></tr><tr><td>version</td><td>node의 version</td></tr><tr><td>type</td><td>보통 label과 동일합니다. UI에서 어떤 node가 이 특정 type에 연결될 수 있는지 정의합니다</td></tr><tr><td>icon</td><td>node의 아이콘</td></tr><tr><td>category</td><td>node의 category</td></tr><tr><td>author</td><td>node의 제작자</td></tr><tr><td>description</td><td>node 설명</td></tr><tr><td>baseClasses</td><td>node가 기본 component에서 확장될 수 있으므로, node의 기본 class입니다. UI에서 어떤 node가 이 node에 연결될 수 있는지 정의하는 데 사용됩니다</td></tr></tbody></table>

### Class 정의

이제 component class가 부분적으로 완성되었으므로, 실제 Tool class(이 경우 `Calculator`)를 정의할 수 있습니다.

동일한 `Calculator` 폴더 아래에 `core.ts`라는 새 파일을 만듭니다.

```javascript
import { Parser } from "expr-eval"
import { Tool } from "@langchain/core/tools"

export class Calculator extends Tool {
    name = "calculator"
    description = `Useful for getting the result of a math expression. The input to this tool should be a valid mathematical expression that could be executed by a simple calculator.`
 
    async _call(input: string) {
        try {
            return Parser.evaluate(input).toString()
        } catch (error) {
            return "I don't know how to do that."
        }
    }
}
```

### 마무리

다시 `Calculator.ts` 파일로 돌아가서, `async init` 함수를 추가하여 이를 마무리할 수 있습니다. 이 함수에서는 위에서 만든 Calculator class를 초기화합니다. flow가 실행될 때 각 node의 `init` 함수가 호출되고, LLM이 이 tool을 호출하기로 결정하면 `_call` 함수가 실행됩니다.

```javascript
import { INode } from '../../../src/Interface'
import { getBaseClasses } from '../../../src/utils'
import { Calculator } from './core'

class Calculator_Tools implements INode {
    label: string
    name: string
    version: number
    description: string
    type: string
    icon: string
    category: string
    author: string
    baseClasses: string[]

    constructor() {
        this.label = 'Calculator'
        this.name = 'calculator'
        this.version = 1.0
        this.type = 'Calculator'
        this.icon = 'calculator.svg'
        this.category = 'Tools'
        this.author = 'Your Name'
        this.description = 'Perform calculations on response'
        this.baseClasses = [this.type, ...getBaseClasses(Calculator)]
    }
    
 
    async init() {
        return new Calculator()
    }
}

module.exports = { nodeClass: Calculator_Tools }
```

### 빌드 및 실행

`packages/server` 내부의 `.env` 파일에 새 env variable을 만듭니다:

```javascript
SHOW_COMMUNITY_NODES=true
```

이제 `pnpm build`와 `pnpm start`를 사용하여 component를 동작시킬 수 있습니다!

<figure><img src="../.gitbook/assets/image (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>
