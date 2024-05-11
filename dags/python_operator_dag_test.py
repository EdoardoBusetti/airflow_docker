from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {'owner':'edo',
'retries':5,
'retry_delay':timedelta(minutes=2),
}

def make_hello(task_instance,age):
    first_name = task_instance.xcom_pull(task_ids = 'get_name',key = 'first_name')
    last_name = task_instance.xcom_pull(task_ids = 'get_name',key = 'last_name')
    print(f'hello my name is {first_name} {last_name} snake mate. and age is {age}')


def get_name(task_instance):
    task_instance.xcom_push(key = 'first_name',value='bob') # Note, the max size for Xcom is 48kb
    task_instance.xcom_push(key = 'last_name',value='marley')

with DAG(dag_id  = 'python_test_dag_v06',
    description = 'my first python day yeeee',
    default_args = default_args,
    start_date = datetime(2024,5,10),
    schedule_interval = '@daily'

) as dag:
    task1 = PythonOperator(task_id = 'greet',
                           python_callable = make_hello,
                           op_kwargs = {'age':20}
                           )
    
    task2 = PythonOperator(task_id = 'get_name',
                           python_callable = get_name,
                           )
    
    task2 >> task1