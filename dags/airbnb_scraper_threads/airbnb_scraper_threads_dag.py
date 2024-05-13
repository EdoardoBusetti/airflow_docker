from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# from scripts.test import main
from scripts.test import main

default_args = {'owner':'edo',
'retries':5,
'retry_delay':timedelta(minutes=2),
}



with DAG(dag_id  = 'airbnb_scraper_threads_dag_v11',
    description = 'test 123',
    default_args = default_args,
    start_date = datetime(2024,5,11),
    schedule_interval = '@daily'

) as dag:
    
    task1 = PythonOperator(
               task_id='my_first_task',
               python_callable=main)

    
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    task1
