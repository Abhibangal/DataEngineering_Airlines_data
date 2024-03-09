#import all the required libraries for dag creation
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email import EmailOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from airflow.models import Variable,TaskInstance
from airflow.providers.microsoft.azure.operators.data_factory import AzureDataFactoryRunPipelineOperator
from airflow.providers.microsoft.azure.sensors.data_factory import AzureDataFactoryPipelineRunStatusSensor
from airflow.utils.edgemodifier import Label
from airflow.operators.empty import EmptyOperator
from airflow.providers.microsoft.azure.sensors.wasb import WasbBlobSensor
from airflow.providers.microsoft.azure.operators.wasb_delete_blob import WasbDeleteBlobOperator
from airflow.utils.email import send_email
#set variable for database name and schema name
default_args = {
        "email_on_failure" : True,
        "email" : ['abhijit.bangal92@gmail.com']
}




dag = DAG(
    dag_id= 'AIRLINES_ETL_PIPELINE',
    start_date=days_ago(1),
    schedule='0 12 28 * *',
    default_args=default_args,
    catchup=False
    

)

begin =  EmptyOperator(task_id = 'begin',dag = dag)

end = EmptyOperator(task_id = 'end',dag = dag)

ADF_pipeline  = AzureDataFactoryRunPipelineOperator(
    task_id='ADF_pipeline',
    pipeline_name = 'mysql_to_blob',
    resource_group_name = 'databricks_course_rg',
    factory_name = 'ADFSQL2ICEBERG',
    azure_data_factory_conn_id='azure_data_factory',
    wait_for_termination=False,
    dag = dag
                )

# from airflow.providers.microsoft.azure.sensors.data_factory import AzureDataFactoryPipelineRunStatusSensor
ADF_pipeline_status = AzureDataFactoryPipelineRunStatusSensor(
    task_id = 'ADF_pipeline_status',
    run_id=ADF_pipeline.output["run_id"],
    azure_data_factory_conn_id='azure_data_factory',
    resource_group_name = 'databricks_course_rg',
    factory_name = 'ADFSQL2ICEBERG',
    deferrable = True,
    dag = dag
    )
# from airflow.providers.microsoft.azure.sensors.wasb import WasbBlobSensor
Check_for_airlines_file = WasbBlobSensor(
    task_id = 'Check_for_airlines_file',
    container_name = 'raw' ,
    blob_name = 'csv/Airlines_Data.csv.gz',
    wasb_conn_id='azure_blob_storage',
    check_options=None,
    deferrable = True
    )


blob_to_snowflake_stg = SnowflakeOperator(
                task_id = 'blob_to_snowflake_stg',
                snowflake_conn_id = 'snowflake_conn_id',
                sql= './sql/Airlines_ingest_query.sql', # use a query file instead of adding query here. Clean code Policy
                params={"database_name":Variable.get('TEST_ANALYTICS'), "schema_name" : Variable.get('AIRLINES')}, #this parameters will be used in query written in text file
                dag = dag

)

merge_obt_airlines = SnowflakeOperator(
    task_id = 'merge_obt_airlines',
    snowflake_conn_id = 'snowflake_conn_id',
    sql = './sql/Merge_into_obt_airlines.sql',
    params = {"database_name":Variable.get('TEST_ANALYTICS'), "schema_name" : Variable.get('AIRLINES')},
    dag=dag
)

# from airflow.providers.microsoft.azure.operators.wasb_delete_blob import WasbDeleteBlobOperator
remove_airlines_file = WasbDeleteBlobOperator(
    task_id='remove_airlines_file',
    container_name='raw',
    blob_name='csv/Airlines_Data.csv.gz',
    wasb_conn_id='azure_blob_storage',
    check_options=None,
    is_prefix=False,
    ignore_if_missing=False,
    )


# trigger the tasks
begin >> Label('Do async operation') >> ADF_pipeline
[ADF_pipeline_status, Check_for_airlines_file] >> blob_to_snowflake_stg >> merge_obt_airlines >>  remove_airlines_file >> end