from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:

    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bq = BigQuery.with_config(ConfigFileLoader(config_path, config_profile))

    # Loop through all tables
    for table_name, df in data.items():
        table_id = f'data-with-rishi.uber_data_engineering_dataset_rishi.{table_name}'
        
        print(f"Exporting {table_name} with shape {df.shape}...")

        bq.export(
            df,
            table_id,
            if_exists='replace',
        )

    print("All tables exported successfully!")
