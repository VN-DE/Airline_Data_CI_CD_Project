from datetime import datetime, timedelta
import uuid  # Import UUID for unique batch IDs
from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import DataprocCreateClusterOperator
from airflow.providers.google.cloud.operators.dataproc import DataprocDeleteClusterOperator
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
from airflow.providers.google.cloud.sensors.gcs import GCSObjectExistenceSensor
from airflow.utils.trigger_rule import TriggerRule
from airflow.models import Variable

# DAG default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 3, 14),
}

# Define the DAG
with DAG(
    dag_id="flight_booking_dataproc_bq_dag",
    default_args=default_args,
    schedule_interval=None,  # Trigger manually or on-demand
    catchup=False,
) as dag:

    # Fetch environment variables
    env = Variable.get("env", default_var="dev")
    gcs_bucket = Variable.get("gcs_bucket", default_var="airflow-projects-airline")
    bq_project = Variable.get("bq_project", default_var="sincere-venture-445815-s9")
    bq_dataset = Variable.get("bq_dataset", default_var=f"flight_data_{env}")
    tables = Variable.get("tables", deserialize_json=True)

    # Extract table names from the 'tables' variable
    transformed_table = tables["transformed_table"]
    route_insights_table = tables["route_insights_table"]
    origin_insights_table = tables["origin_insights_table"]

    # Generate a unique batch ID using UUID
    batch_id = f"flight-booking-batch-{env}"  # Shortened UUID for brevity

    # # Task 1: File Sensor for GCS
    file_sensor = GCSObjectExistenceSensor(
        task_id="check_file_arrival",
        bucket=gcs_bucket,
        object=f"airflow-project-1/source-{env}/flight_booking.csv",  # Full file path in GCS
        google_cloud_conn_id="google_cloud_default",  # GCP connection
        timeout=300,  # Timeout in seconds
        poke_interval=30,  # Time between checks
        mode="poke",  # Blocking mode
    )

    # # Task 2: Submit PySpark job to Dataproc Serverless
    # batch_details = {
    #     "pyspark_batch": {
    #         "main_python_file_uri": f"gs://{gcs_bucket}/airflow-project-1/spark-job/spark_transformation_job.py",
    #         "python_file_uris": [],
    #         "jar_file_uris": [],
    #         "args": [
    #             f"--env={env}",
    #             f"--bq_project={bq_project}",
    #             f"--bq_dataset={bq_dataset}",
    #             f"--transformed_table={transformed_table}",
    #             f"--route_insights_table={route_insights_table}",
    #             f"--origin_insights_table={origin_insights_table}",
    #         ]
    #     },
    #     "runtime_config": {
    #         "version": "2.2",
    #         "properties": {
    #             # Reduce executor memory and cores to fit within your quota
    #             "spark.executor.instances": "2",
    #             "spark.executor.cores": "4",
    #             "spark.executor.memory": "16g",
    #             "spark.driver.cores": "4",
    #             "spark.driver.memory": "16g"
    #         }
    #     },
    #     "environment_config": {
    #         "execution_config": {
    #             "service_account": "315169430143-compute@developer.gserviceaccount.com",
    #             "network_uri": "projects/sincere-venture-445815-s9/global/networks/default",
    #             "subnetwork_uri": "projects/sincere-venture-445815-s9/regions/us-central1/subnetworks/default",
    #         }
    #     },
    # }
    # batch_details = {
    #     "pyspark_batch": {
    #         "main_python_file_uri": f"gs://{gcs_bucket}/airflow-project-1/spark-job/spark_transformation_job.py",  # Main Python file
    #         "python_file_uris": [],  # Python WHL files
    #         "jar_file_uris": [],  # JAR files
    #         "args": [
    #             f"--env={env}",
    #             f"--bq_project={bq_project}",
    #             f"--bq_dataset={bq_dataset}",
    #             f"--transformed_table={transformed_table}",
    #             f"--route_insights_table={route_insights_table}",
    #             f"--origin_insights_table={origin_insights_table}",
    #         ]
    #     },
    #     "runtime_config": {
    #         "version": "2.2",  # Specify Dataproc version (if needed)
    #     },
    #     "environment_config": {
    #         "execution_config": {
    #             "service_account": "315169430143-compute@developer.gserviceaccount.com",
    #             "network_uri": "projects/sincere-venture-445815-s9/global/networks/default",
    #             "subnetwork_uri": "projects/sincere-venture-445815-s9/regions/us-central1/subnetworks/default",
    #         }
    #     },
    #     "compute_config": {
    #         "scaling_config": {
    #             "worker_count": 2,  # Minimum number of workers
    #             "max_worker_count": 4  # Maximum number of workers
    #         },
    #         "worker_config": {
    #             "machine_type": "n1-standard-2"  # Smaller machine type with 2 vCPUs
    #         }
    #     }
    # }

    # pyspark_task = DataprocCreateBatchOperator(
    #     task_id="run_spark_job_on_dataproc_serverless",
    #     batch=batch_details,
    #     batch_id=batch_id,
    #     project_id="sincere-venture-445815-s9",
    #     region="us-central1",
    #     gcp_conn_id="google_cloud_default",
    # )

# Not using dataproc serverless because of quota constraints

    # Task 2: Create a Dataproc cluster - optimized for free tier
    create_cluster = DataprocCreateClusterOperator(
        task_id="create_dataproc_cluster",
        project_id="sincere-venture-445815-s9",
        cluster_name=batch_id,
        region="us-central1",
        cluster_config={
            "master_config": {
                "num_instances": 1,
                "machine_type_uri": "n1-standard-2",  # Small machine type, good for free tier
                "disk_config": {
                    "boot_disk_type": "pd-standard",
                    "boot_disk_size_gb": 30
                }
            },
            "worker_config": {
                "num_instances": 2,  # Minimum number of workers needed
                "machine_type_uri": "n1-standard-2",  # Small machine type, good for free tier
                "disk_config": {
                    "boot_disk_type": "pd-standard",
                    "boot_disk_size_gb": 30
                }
            },
            "software_config": {
                "image_version": "2.0-debian10"  # Choose an appropriate version
            },
            "gce_cluster_config": {
                "service_account_scopes": [
                    "https://www.googleapis.com/auth/cloud-platform"
                ],
                "service_account": "315169430143-compute@developer.gserviceaccount.com"
            }
        }
    )

    # Task 3: Submit PySpark job to Dataproc cluster
    pyspark_job = {
        "reference": {"project_id": "sincere-venture-445815-s9"},
        "placement": {"cluster_name": batch_id},
        "pyspark_job": {
            "main_python_file_uri": f"gs://{gcs_bucket}/airflow-project-1/spark-job/spark_transformation_job.py",
            "args": [
                f"--env={env}",
                f"--bq_project={bq_project}",
                f"--bq_dataset={bq_dataset}",
                f"--transformed_table={transformed_table}",
                f"--route_insights_table={route_insights_table}",
                f"--origin_insights_table={origin_insights_table}",
            ]
        }
    }

    submit_pyspark_job = DataprocSubmitJobOperator(
        task_id="submit_pyspark_job",
        project_id="sincere-venture-445815-s9",
        region="us-central1",
        job=pyspark_job,
        gcp_conn_id="google_cloud_default"
    )

    # Task 4: Delete the Dataproc cluster (important to save costs!)
    delete_cluster = DataprocDeleteClusterOperator(
        task_id="delete_dataproc_cluster",
        project_id="sincere-venture-445815-s9",
        cluster_name=batch_id,
        region="us-central1",
        trigger_rule=TriggerRule.ALL_DONE,  # Delete the cluster even if the job fails
    )

    # Task Dependencies
    file_sensor >> create_cluster >> submit_pyspark_job >> delete_cluster


    # Task Dependencies
    # file_sensor >> pyspark_task