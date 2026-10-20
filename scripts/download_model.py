import mlflow
import os

# mlflow.set_tracking_uri("azureml://spaincentral.api.azureml.ms/mlflow/v1.0/subscriptions/84261411-9013-44d1-b8e1-6ba904def1d1/resourceGroups/rg-alberto-pontia/providers/Microsoft.MachineLearningServices/workspaces/aml-curso-devops-2026")
# EXPERIMENT_NAME = "hola5-adult-income"

MLFLOW_URL = os.getenv("MLFLOW_URL","http://localhost:5001/")
EXPERIMENT_NAME = os.getenv("EXPERIMENT_NAME", "limbergrivera-adult-income")
mlflow.set_tracking_uri(MLFLOW_URL)

local_path = mlflow.artifacts.download_artifacts(
    artifact_uri=f"models:/{EXPERIMENT_NAME}/latest",
    dst_path="./models"
)

print(f"Modelo descargado en: {local_path}")