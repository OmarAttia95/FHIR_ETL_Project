FROM apache/airflow:2.5.0-python3.8

# Set up Airflow environment variables
ENV AIRFLOW_HOME=/home/omarattia/airflow
ENV AIRFLOW__CORE__DAGS_FOLDER=/home/omarattia/airflow/dags
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:////home/omarattia/airflow/airflow.db
ENV AIRFLOW__CORE__EXECUTOR=SequentialExecutor

# Install necessary Python packages
RUN pip install --no-cache-dir pandas requests sqlalchemy apache-airflow

# Expose the web server port (default is 8080)
EXPOSE 8080

# Copy your DAG files from your local machine to the container
COPY airflow_dag_workflow.py /home/omarattia/airflow/dags/airflow_dag_workflow.py


# Default command to initialize the database and start the Airflow webserver
CMD ["bash", "-c", "airflow db init && airflow webserver"]
