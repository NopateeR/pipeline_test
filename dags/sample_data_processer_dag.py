from dagfactory import load_yaml_dags
from airflow import DAG
from pathlib import Path

_CONFIG_PATH = Path(__file__).parent.resolve()

load_yaml_dags(
    globals_dict=globals(),
    config_filepath=str(_CONFIG_PATH / "configs/sample_data_processer_configs.yaml")
)


