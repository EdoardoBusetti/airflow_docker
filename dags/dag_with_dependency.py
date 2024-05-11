from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {'owner':'edo',
'retries':5,
'retry_delay':timedelta(minutes=2),
}

@dag(dag_id = 'dag_with_dependency_v01',
     default_args=default_args,
     start_date = datetime(2024,5,10),
    schedule_interval = '0 0 * * *'
     )
def hello_world_etl():

    @task()
    def get_sklearn():
        import sklearn
        print(f'sklearn version: {sklearn.__version__}')
    
    get_sklearn()

greet_dag = hello_world_etl()