# SQL 에이전트

이 튜토리얼은 데이터베이스와 상호 작용하고, SQL 쿼리를 생성하고, 검증하고, 실행하고, 오류 발생 시 자체 수정할 수 있는 지능형 SQL 에이전트를 구축하는 방법을 안내합니다.

## 개요

SQL 에이전트 플로우는 다음을 수행하는 강력한 데이터베이스 상호 작용 시스템을 구현합니다:

1. 데이터베이스 스키마 정보를 검색합니다.
2. 사용자 질문을 기반으로 SQL 쿼리를 생성합니다.
3. 일반적인 실수가 있는지 생성된 쿼리를 검증합니다.
4. 데이터베이스에 대해 쿼리를 실행합니다.
5. 결과 오류를 확인하고 필요할 때 자체 수정합니다.
6. 쿼리 결과를 기반으로 자연어 응답을 제공합니다.

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### 단계 1: 시작 노드 설정

캔버스에 **시작** 노드를 추가하여 시작합니다. 이것이 SQL 에이전트의 진입점입니다.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **입력 유형**: "채팅 입력"을 선택하여 사용자 질문을 허용합니다.
* **플로우 상태**: 키 "`sqlQuery`"와 빈 값이 있는 상태 변수를 추가합니다.

시작 노드는 프로세스 전체에서 생성된 SQL 쿼리를 저장할 빈 `sqlQuery` 변수로 플로우 상태를 초기화합니다.

### 단계 2: 데이터베이스 스키마 검색

**사용자 정의 함수** 노드를 추가하고 시작 노드에 연결합니다.

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **JavaScript 함수**: 이것은 데이터베이스에 연결하고 테이블 구조, 열 정의 및 샘플 데이터를 포함한 완전한 스키마를 검색하는 예제 함수입니다.

```javascript
const { DataSource } = require('typeorm');

const HOST = 'localhost';
const USER = 'testuser';
const PASSWORD = 'testpwd';
const DATABASE = 'testdatabase';
const PORT = 5432;

let sqlSchemaPrompt = '';

const AppDataSource = new DataSource({
  type: 'postgres',
  host: HOST,
  port: PORT,
  username: USER,
  password: PASSWORD,
  database: DATABASE,
  synchronize: false,
  logging: false,
});

async function getSQLPrompt() {
  try {
    await AppDataSource.initialize();
    const queryRunner = AppDataSource.createQueryRunner();

    // 모든 사용자 정의 테이블 가져오기
    const tablesResult = await queryRunner.query(`
      SELECT table_name
      FROM information_schema.tables
      WHERE table_schema = 'public' AND table_type = 'BASE TABLE'
    `);

    for (const tableRow of tablesResult) {
      const tableName = tableRow.table_name;
      const schemaInfo = await queryRunner.query(`
        SELECT column_name, data_type, is_nullable
        FROM information_schema.columns
        WHERE table_name = '${tableName}'
      `);

      const createColumns = [];
      const columnNames = [];

      for (const column of schemaInfo) {
        const name = column.column_name;
        const type = column.data_type.toUpperCase();
        const notNull = column.is_nullable === 'NO' ? 'NOT NULL' : '';
        columnNames.push(name);
        createColumns.push(`${name} ${type} ${notNull}`);
      }

      const sqlCreateTableQuery = `CREATE TABLE ${tableName} (${createColumns.join(', ')})`;
      const sqlSelectTableQuery = `SELECT * FROM ${tableName} LIMIT 3`;

      let allValues = [];
      try {
        const rows = await queryRunner.query(sqlSelectTableQuery);
        allValues = rows.map(row =>
          columnNames.map(col => row[col]).join(' ')
        );
      } catch (err) {
        allValues.push('[ERROR FETCHING ROWS]');
      }

      sqlSchemaPrompt +=
        sqlCreateTableQuery + '\n' +
        sqlSelectTableQuery + '\n' +
        columnNames.join(' ') + '\n' +
        allValues.join('\n') + '\n\n';
    }

    await queryRunner.release();
  } catch (err) {
    console.error(err);
    throw err;
  }
}

await getSQLPrompt();
return sqlSchemaPrompt;
```

### 단계 3: SQL 쿼리 생성

"Get DB Schema" 노드에 연결된 **LLM** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **메시지**: 시스템 메시지를 추가합니다:

```
당신은 SQL 데이터베이스와 상호 작용하도록 설계된 에이전트입니다. 입력 질문이 주어지면 실행할 구문적으로 올바른 SQLite 쿼리를 작성합니다. 그런 다음 쿼리 결과를 보고 답변을 반환합니다. 사용자가 원하는 특정 수의 예를 지정하지 않으면 항상 쿼리를 최대 5개 결과로 제한합니다. 결과를 관련 열로 정렬하여 데이터베이스에서 가장 흥미로운 예를 반환할 수 있습니다. 특정 테이블의 모든 열을 쿼리하지 마세요. 질문에 주어진 관련 열만 요청하세요. 데이터베이스에 대해 DML 문(INSERT, UPDATE, DELETE, DROP 등)을 만들지 마세요.

다음은 관련 테이블 정보입니다:
{{ customFunctionAgentflow_0 }}

참고:
- 하나의 SQL 쿼리만 생성하세요.
```

* **JSON 구조화된 출력**: 여기서 LLM이 SQL 쿼리 이외의 다른 텍스트를 포함하지 않도록 구조화된 출력만 반환하도록 지시합니다.
  * 키: "`sql_query`"
  * 유형: "string"
  * 설명: "SQL 쿼리"
* **플로우 상태 업데이트**: 키 "`sqlQuery`"를 값 `{{ output.sql_query }}`로 설정합니다.

이 노드는 사용자의 자연어 질문을 데이터베이스 스키마 정보를 사용하여 구조화된 SQL 쿼리로 변환합니다.

### 단계 4: SQL 쿼리 구문 검증

"Generate SQL Query" LLM에 연결된 **조건 에이전트** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **지침**:

```
당신은 세부 사항에 주의를 기울이는 SQL 전문가입니다. SQL 쿼리가 일반적인 실수가 있는지 다시 확인합니다. 다음을 포함합니다:
- NULL 값과 함께 NOT IN 사용
- UNION ALL을 사용해야 할 때 UNION 사용
- 독점 범위에 BETWEEN 사용
- 술어에서 데이터 유형 불일치
- 식별자를 올바르게 인용
- 함수에 올바른 수의 인수 사용
- 올바른 데이터 유형으로 캐스팅
- 조인을 위해 올바른 열 사용
```

* **입력**: `{{ $flow.state.sqlQuery }}`
* **시나리오**:
  * 시나리오 1: "SQL 쿼리가 올바르고 실수가 없습니다."
  * 시나리오 2: "SQL 쿼리에 실수가 있습니다."

이 검증 단계는 실행 전에 일반적인 SQL 오류를 포착합니다.

### 단계 5: 쿼리 재생성 처리 (오류 경로)

이전 조건 에이전트 노드의 올바르지 않은 쿼리(출력 1)의 경우 **루프** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (6) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

#### 구성:

<figure><img src="../.gitbook/assets/image (7) (1) (1) (1) (1) (1).png" alt="" width="526"><figcaption></figcaption></figure>

* **루프 백 대상**: "Generate SQL Query"
* **최대 루프 카운트**: 5로 설정합니다.

이것은 검증이 실패할 때 시스템이 쿼리 생성을 다시 시도할 수 있도록 하는 피드백 루프를 만듭니다.

### 단계 6: 올바른 SQL 쿼리 실행

올바른 쿼리(출력 0)의 경우 **사용자 정의 함수** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (8) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

#### 구성:

<figure><img src="../.gitbook/assets/image (9) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

* **입력 변수**: 여기서 생성된 SQL 쿼리를 함수에서 사용할 변수로 전달합니다.
  * 변수명: "sqlQuery"
  * 변수 값: `{{ $flow.state.sqlQuery }}`
* **JavaScript 함수**: 이 함수는 검증된 SQL 쿼리를 데이터베이스에 대해 실행하고 결과를 형식화합니다.

```javascript
const { DataSource } = require('typeorm');

const HOST = 'localhost';
const USER = 'testuser';
const PASSWORD = 'testpwd';
const DATABASE = 'testdatabase';
const PORT = 5432;

const sqlQuery = $sqlQuery;

const AppDataSource = new DataSource({
  type: 'postgres',
  host: HOST,
  port: PORT,
  username: USER,
  password: PASSWORD,
  database: DATABASE,
  synchronize: false,
  logging: false,
});

let formattedResult = '';

async function runSQLQuery(query) {
  try {
    await AppDataSource.initialize();
    const queryRunner = AppDataSource.createQueryRunner();

    const rows = await queryRunner.query(query);
    console.log('rows =', rows);

    if (rows.length === 0) {
      formattedResult = '[결과 없음]';
    } else {
      const columnNames = Object.keys(rows[0]);
      const header = columnNames.join(' ');
      const values = rows.map(row =>
        columnNames.map(col => row[col]).join(' ')
      );

      formattedResult = query + '\n' + header + '\n' + values.join('\n');
    }

    await queryRunner.release();
  } catch (err) {
    console.error('[ERROR]', err);
    formattedResult = `[쿼리 실행 오류]: ${err}`;
  }

  return formattedResult;
}

await runSQLQuery(sqlQuery);
return formattedResult;
```

### 단계 7: 쿼리 실행 결과 확인

"Run SQL Query" 함수에 연결된 **조건 에이전트** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (10) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **지침**: "당신은 SQL 전문가입니다. 쿼리 결과가 올바른지 또는 오류가 있는지 확인합니다."
* **입력**: `{{ customFunctionAgentflow_1 }}`
* **시나리오**:
  * 시나리오 1: "결과가 올바르고 오류가 없습니다."
  * 시나리오 2: "결과 쿼리에 오류가 있습니다."

이 단계는 실행 결과를 검증하고 추가 수정이 필요한지 여부를 결정합니다.

### 단계 8: 최종 응답 생성 (성공 경로)

성공한 결과(조건 에이전트의 출력 0)의 경우 **LLM** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (11) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

#### 구성:

* **입력 메시지**: `{{ customFunctionAgentflow_1 }}`

이 노드는 성공한 쿼리 결과를 기반으로 자연어 응답을 생성합니다.

### 단계 9: 쿼리 재생성 처리 (런타임 오류 경로)

실패한 실행(조건 에이전트의 출력 1)의 경우 **LLM** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (12) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

#### 구성:

<figure><img src="../.gitbook/assets/image (13) (1) (1) (1).png" alt="" width="399"><figcaption></figcaption></figure>

* **메시지**: 단계 3과 동일한 시스템 메시지를 추가합니다.
* **입력 메시지**:

```
생성된 SQL 쿼리가 주어졌습니다: {{ $flow.state.sqlQuery }}
다음 오류가 있습니다: {{ customFunctionAgentflow_1 }}
오류를 수정할 새로운 SQL 쿼리를 재생성합니다.
```

* **JSON 구조화된 출력**: 단계 3과 동일합니다.
* **플로우 상태 업데이트**: 키 "`sqlQuery`"를 값 `{{ output.sql_query }}`로 설정합니다.

이 노드는 런타임 오류를 분석하고 수정된 SQL 쿼리를 생성합니다.

### 단계 10: 두 번째 루프 백 추가

"Regenerate SQL Query" LLM에 연결된 **루프** 노드를 추가합니다.

<figure><img src="../.gitbook/assets/image (14) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

#### 구성:

* **루프 백 대상**: "Check SQL Query"
* **최대 루프 카운트**: 5로 설정합니다.

이것은 런타임 오류 수정을 위한 두 번째 피드백 루프를 만듭니다.

***

## 완전한 플로우 구조

{% file src="../.gitbook/assets/SQL Agent.json" %}

***

## 요약

1. 시작 → DB 스키마 가져오기
2. DB 스키마 가져오기 → SQL 쿼리 생성
3. SQL 쿼리 생성 → SQL 쿼리 확인
4. SQL 쿼리 확인 (올바름) → SQL 쿼리 실행
5. SQL 쿼리 확인 (올바르지 않음) → 쿼리 재생성 (루프 백)
6. SQL 쿼리 실행 → 결과 확인
7. 결과 확인 (성공) → 응답 반환
8. 결과 확인 (오류) → SQL 쿼리 재생성
9. SQL 쿼리 재생성 → SQL 쿼리 다시 확인 (루프 백)

***

## SQL 에이전트 테스트

다양한 유형의 데이터베이스 질문으로 에이전트를 테스트합니다:

* 간단한 쿼리: "모든 고객을 보여줍니다."
* 복잡한 쿼리: "판매량 상위 5개 제품은 무엇입니까?"
* 분석 쿼리: "월별 평균 주문 가치를 계산합니다."

<figure><img src="../.gitbook/assets/image (15) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

이 SQL 에이전트 플로우는 자연어로 SQL 쿼리를 처리할 수 있는 강력하고 자체 수정 가능한 데이터베이스 상호 작용 시스템을 제공합니다.
