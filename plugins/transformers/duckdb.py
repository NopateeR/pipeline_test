import duckdb
from typing import Optional,Self

class DuckDBEngine:
    def __init__(self,config:Optional[dict]=None):
        self.config = config
        self.con = duckdb.connect()
        self.con.execute("SET memory_limit='8GiB'")
        self.con.execute("SET temp_directory='/tmp/duckdb';")
    def connection(self):
        return self.con
    
    def close(self):
        return self.con.close()
    
    def set_db_connection(self,conn_str:str)-> Self:
        if conn_str.split(":")[0] == "postgresql":
            attached_type = 'POSTGRES'
        else:
            raise ValueError(f"Not support database type : {conn_str.split(":")[0]}")
        self.con.execute(f"INSTALL {attached_type};")
        self.con.execute(f"LOAD {attached_type};")
        self.con.execute(f"ATTACH '{conn_str}' AS datalake (TYPE {attached_type});")
        return self
    
    def is_table_exists(self,schema: str,table: str) -> bool:
        return self.con.execute(f"""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_schema = '{schema}'
        AND table_name = '{table}'
        """).fetchone()[0] > 0
    
    def create_table_from_query(self,table: str,query:str) -> Self:
        self.con.execute(f"""
        CREATE OR REPLACE TABLE {table} AS
        {query}
        """)
        return self
    
    def merge_table_from_query(self,table: str,query:str,key:list) -> Self:
        self.con.execute(f"""
        MERGE INTO {table}
        USING ({query}) AS source
        ON {' AND '.join([f'target.{k} = source.{k}' for k in key])}
        WHEN MATCHED THEN
            UPDATE SET
                {''.join([f'{k} = source.{k}, ' for k in key])}
        WHEN NOT MATCHED THEN
            INSERT ({', '.join(key)})
            VALUES ({', '.join([f'source.{k}' for k in key])})
        """)
        return self