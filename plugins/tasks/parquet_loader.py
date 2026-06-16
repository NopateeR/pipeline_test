from transformers.duckdb import DuckDBEngine
from typing import Dict


def load_parquet_into_postgres(
    folder_path: str,
    database_name:str,
    schema_name:str,
    table_name:str,
    connection_configs:Dict[str,str],
):
    """
    Load parquet files into PostgreSQL database via DuckDB

    Args:
        folder_path (str): Path to the folder containing parquet files
        database_name (str): Name of the database
        schema_name (str): Name of the schema
        table_name (str): Name of the table
        connection_configs (dict): Dictionary of connection configurations
    """

    host = connection_configs['host']
    port = connection_configs['port']
    user = connection_configs['user']
    password = connection_configs['password']
    database = connection_configs['database']
    conn_type = connection_configs['conn_type']

    connection_string = f"{conn_type}://{user}:{password}@{host}:{port}/{database}"

    engine = DuckDBEngine()
    engine.set_db_connection(connection_string)

    engine.connection().execute(f"""
    CREATE SCHEMA IF NOT EXISTS {database_name}.{schema_name}
    """)

    engine.create_table_from_query(f"{database_name}.{schema_name}.{table_name}",f"""
        SELECT *
        FROM read_parquet('{folder_path}/*.parquet')
        """)
