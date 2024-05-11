from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {'owner':'edo',
'retries':5,
'retry_delay':timedelta(minutes=2),
}

with DAG(dag_id  = 'my_first_dag_v3',
    description = 'my first day yeeee',
    default_args = default_args,
    start_date = datetime(2024,5,8),
    schedule_interval = '@daily'

) as dag:
    task1 = BashOperator(task_id = 'my_first_task',
                         bash_command = 'echo hellow ppl'
                          )

    task2 = BashOperator(task_id = 'task2',
                         bash_command = 'echo second one matey'
                          )

    task3 = BashOperator(task_id = 'task3',
                         bash_command = 'echo third one matey'
                          )
    
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    task1 >> [task2,task3]

