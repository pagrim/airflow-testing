from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'tutorial',
    default_args=default_args,
    description='A simple DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    bash_start = BashOperator(task_id='print_date',
                              bash_command='echo starting dag')

    api_call = SimpleHttpOperator(
        task_id="is_it_light",
        http_conn_id="sun_conn",
        data={"lat": 51.5072, "lng": 0.1276},
        endpoint="json",
        method="GET",
    )

    bash_start >> api_call

