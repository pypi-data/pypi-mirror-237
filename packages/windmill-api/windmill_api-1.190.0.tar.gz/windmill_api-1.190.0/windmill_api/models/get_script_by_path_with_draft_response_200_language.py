from enum import Enum


class GetScriptByPathWithDraftResponse200Language(str, Enum):
    BASH = "bash"
    BIGQUERY = "bigquery"
    BUN = "bun"
    DENO = "deno"
    GO = "go"
    GRAPHQL = "graphql"
    MYSQL = "mysql"
    NATIVETS = "nativets"
    POSTGRESQL = "postgresql"
    POWERSHELL = "powershell"
    PYTHON3 = "python3"
    SNOWFLAKE = "snowflake"

    def __str__(self) -> str:
        return str(self.value)
