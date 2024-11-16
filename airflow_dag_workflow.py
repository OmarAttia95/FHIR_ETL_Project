import sys
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Ensure the path is correct for the Data_Extraction module
sys.path.insert(0, '/home/omarattia/Take_Home_Assesment/worflow_scripts')

# Import the data_extraction function from Data_Extraction
from Data_Extraction import data_extraction
from Data_Transformation_One import data_transformation_one
from Data_Transformation_Two import data_transformation_two
from Data_Transformation_Three import data_transformation_three
from Data_Transformation_Four import data_transformation_four
from Data_Transformation_Five import data_transformation_five
from Data_Transformation_Six import data_transformation_six
from Data_Loading_SQL import data_loading

# Define default_args for the DAG
default_args = {
    'owner': 'omarattia',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 11, 16),  
}

# Define the DAG
dag = DAG(
    'FHIR_ETL_Workflow',
    default_args=default_args,
    description='ETL workflow for processing FHIR data',
    schedule_interval='@daily',  
    catchup=False,
)

# Task 1: Data Extraction (Data Extraction from JSON dump files)
data_extraction_task = PythonOperator(
    task_id='data_extraction',
    python_callable=data_extraction,  
    dag=dag,
)

# Task 2: Data Transformation (Step 1: Data Transformation 1 Patient Information Dimension)
data_transformation_one_task = PythonOperator(
    task_id='data_transformation_one',
    python_callable=data_transformation_one, 
    dag=dag,
)

# Task 3: Data Transformation (Step 2: Data Transformation 2 Encounter Events Dimension)
data_transformation_two_task = PythonOperator(
    task_id='data_transformation_two',
    python_callable=data_transformation_two,  
    dag=dag,
)

# Task 4: Data Transformation (Step 3: Data Transformation 3 Dignosis Report Events Dimension)
data_transformation_three_task = PythonOperator(
    task_id='data_transformation_three',
    python_callable=data_transformation_three,  
    dag=dag,
)

# Task 5: Data Transformation (Step 4: Data Transformation 4 Condition Events Dimension)
data_transformation_four_task = PythonOperator(
    task_id='data_transformation_four',
    python_callable=data_transformation_four,
    dag=dag,
)

# Task 6: Data Transformation (Step 5: Data Transformation 5 Claims, EOBs, and Medicine Requests Dimensions)
data_transformation_five_task = PythonOperator(
    task_id='data_transformation_five',
    python_callable=data_transformation_five, 
    dag=dag,
)

# Task 7: Data Transformation (Step 6: Data Transformation 6 Medicine Descriptive Dimension - Overwrite)
data_transformation_six_task = PythonOperator(
    task_id='data_transformation_six',
    python_callable=data_transformation_six,  
    dag=dag,
)

# Task 8: Data Loading into SQL
data_loading_task = PythonOperator(
    task_id='data_loading',
    python_callable=data_loading,
    dag=dag,
)

# Task Dependencies
data_extraction_task >> data_transformation_one_task >> data_transformation_two_task >> data_transformation_three_task >> data_transformation_four_task >> data_transformation_five_task >> data_transformation_six_task >> data_loading_task
