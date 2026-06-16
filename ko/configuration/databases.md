---
description: Flowise 인스턴스를 데이터베이스에 연결하는 방법을 알아봅시다
---

# 데이터베이스

---

## 설정

Flowise는 4가지 데이터베이스 유형을 지원합니다:

- SQLite
- MySQL
- PostgreSQL
- MariaDB

### SQLite (기본값)

SQLite가 기본 데이터베이스가 됩니다. 이러한 데이터베이스는 다음 환경 변수로 구성할 수 있습니다:

```sh
DATABASE_TYPE=sqlite
DATABASE_PATH=/root/.flowise #your preferred location
```

`database.sqlite` 파일이 생성되어 `DATABASE_PATH`로 지정된 경로에 저장됩니다. 지정하지 않으면 기본 저장 경로는 홈 디렉토리 -> .flowise가 됩니다.

**참고:** 환경 변수가 지정되지 않으면 SQLite가 fallback 데이터베이스 선택이 됩니다.

### MySQL

```sh
DATABASE_TYPE=mysql
DATABASE_PORT=3306
DATABASE_HOST=localhost
DATABASE_NAME=flowise
DATABASE_USER=user
DATABASE_PASSWORD=123
```

### PostgreSQL

```sh
DATABASE_TYPE=postgres
DATABASE_PORT=5432
DATABASE_HOST=localhost
DATABASE_NAME=flowise
DATABASE_USER=user
DATABASE_PASSWORD=123
PGSSLMODE=require
```

### MariaDB

```bash
DATABASE_TYPE="mariadb"
DATABASE_PORT="3306"
DATABASE_HOST="localhost"
DATABASE_NAME="flowise"
DATABASE_USER="flowise"
DATABASE_PASSWORD="mypassword"
```

### Flowise 데이터베이스 SQLite 및 MySQL/MariaDB 사용 방법

{% embed url="https://youtu.be/R-6uV1Cb8I8" %}

## 백업

1. FlowiseAI 애플리케이션을 종료합니다.
2. 다른 애플리케이션에 대한 데이터베이스 연결이 꺼져 있는지 확인합니다.
3. 데이터베이스를 백업합니다.
4. 백업 데이터베이스를 테스트합니다.

### SQLite

1. 파일 이름을 변경합니다.

   Windows:

   ```bash
   rename "DATABASE_PATH\database.sqlite" "DATABASE_PATH\BACKUP_FILE_NAME.sqlite"
   ```

   Linux:

   ```bash
   mv DATABASE_PATH/database.sqlite DATABASE_PATH/BACKUP_FILE_NAME.sqlite
   ```

2. 데이터베이스를 백업합니다.

   Windows:

   ```bash
   copy DATABASE_PATH\BACKUP_FILE_NAME.sqlite DATABASE_PATH\database.sqlite
   ```

   Linux:

   ```bash
   cp DATABASE_PATH/BACKUP_FILE_NAME.sqlite DATABASE_PATH/database.sqlite
   ```

3. Flowise를 실행하여 백업 데이터베이스를 테스트합니다.

### PostgreSQL

1. 데이터베이스를 백업합니다.

   ```bash
   pg_dump -U USERNAME -h HOST -p PORT -d DATABASE_NAME -f /PATH/TO/BACKUP_FILE_NAME.sql
   ```

2. 데이터베이스 암호를 입력합니다.
3. 테스트 데이터베이스를 생성합니다.
   ```bash
   psql -U USERNAME -h HOST -p PORT -d TEST_DATABASE_NAME -f /PATH/TO/BACKUP_FILE_NAME.sql
   ```
4. `.env` 파일을 수정하여 백업 데이터베이스를 가리키도록 하여 Flowise를 실행함으로써 백업 데이터베이스를 테스트합니다.

### MySQL & MariaDB

1. 데이터베이스를 백업합니다.

   ```bash
   mysqldump -u USERNAME -p DATABASE_NAME > BACKUP_FILE_NAME.sql
   ```

2. 데이터베이스 암호를 입력합니다.
3. 테스트 데이터베이스를 생성합니다.
   ```bash
   mysql -u USERNAME -p TEST_DATABASE_NAME < BACKUP_FILE_NAME.sql
   ```

4. `.env` 파일을 수정하여 백업 데이터베이스를 가리키도록 하여 Flowise를 실행함으로써 백업 데이터베이스를 테스트합니다.
