from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.operators.bash import BashOperator
from airflow.providers.http.operators.http import SimpleHttpOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="ettore-dag-1", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:

    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()
    
with DAG(dag_id="esempio-dag-2", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:

    # Tasks are represented as operators
    get_dir = BashOperator(task_id="get-dir", bash_command="echo $(ls -1 ~)")

    print = BashOperator(task_id="print", bash_command="echo hello world")

    # search_google = SimpleHttpOperator(
    #     task_id="search-google",
    #     endpoint="http://www.google.com"
    # )

    get_dir >> print # >> search_google 