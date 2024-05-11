from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {'owner':'edo',
'retries':5,
'retry_delay':timedelta(minutes=2),
}

@dag(dag_id = 'dag_with_taskflow_v06',
     default_args=default_args,
     start_date = datetime(2024,5,10),
    schedule_interval = '0 0 * * *'
     )
def hello_world_etl():

    @task(multiple_outputs = True)
    def get_name():
        return {'name':'bob',
                'surname':'neih'}
    
    @task 
    def get_age():
        return 21
    
    @task
    def greet(name,surname,age):
        print(f'you ma mate {name} {surname}'
              f'ye only {age} yo'
              
              )
        
    name_dict = get_name()
    age = get_age()
    greet(name=name_dict['name'],
          surname = name_dict['surname'],
          age=age)

greet_dag = hello_world_etl()