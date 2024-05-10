from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {'owner':'edo',
'retries':5,
'retry_delay':timedelta(minutes=2),
}

with DAG(dag_id  = 'my_first_dag',
    description = 'my first day yeeee',
    default_args = default_args,
    start_date = datetime(2024,5,8),
    scheduler_interval = '@daily'

) as dag:
    task1 = BashOperator(task_id = 'my_first_task',
                         bash_command = 'echo hellow ppl'
                          )