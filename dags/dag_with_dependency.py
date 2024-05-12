from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {'owner':'edo',
'retries':5,
'retry_delay':timedelta(minutes=2),
}

@dag(dag_id = 'dag_with_dependency_v02',
     default_args=default_args,
     start_date = datetime(2024,5,10),
    schedule_interval = '0 0 * * *'
     )
def hello_world_etl():

    @task()
    def get_import_stuff():
        import selenium
        print(f'selenium version: {selenium.__version__}')
    
    get_import_stuff()

import_dag = hello_world_etl()