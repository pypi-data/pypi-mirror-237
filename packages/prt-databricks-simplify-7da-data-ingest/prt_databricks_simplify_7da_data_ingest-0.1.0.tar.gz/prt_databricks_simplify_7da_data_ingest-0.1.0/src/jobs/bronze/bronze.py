from pyspark.sql import SparkSession
import time

from src.schemas.bronze_schema import schema
from src.params import (
    TRIGGER_INTERVAL_SECONDS,
    ISO,
    RAW_BUCKET_NAME,
    CATALOG_NAME,
    SCHEMA_NAME,
    APP_BUCKET_NAME,
    CHECKPOINT_LOCATION_PATH
)


class BronzeLayer:
    """
    Bronze Layer class
    """
    def __init__(self):
        self.spark = SparkSession.builder.getOrCreate()

    def launch(self, model_data_name: str) -> None:
        """
        read n write stream from s3 bucket
        """
        simplify_raw_data_path, full_table_name, full_checkpoint_location = self._get_params(model_data_name)

        stream_df = self.spark.readStream.format("cloudFiles")\
            .option("cloudFiles.format", "parquet")\
            .option("cloudFiles.useIncrementalListing", "auto")\
            .schema(schema)\
            .load(simplify_raw_data_path)\
            .writeStream.format("delta")\
            .trigger(once=True)\
            .option(
                "checkpointLocation",
                full_checkpoint_location
            )\
            .toTable(full_table_name)

        time.sleep(TRIGGER_INTERVAL_SECONDS)

        while stream_df.isActive:
            is_data_available = stream_df.status["isDataAvailable"]
            if not is_data_available:
                stream_df.stop()
                time.sleep(1)

        print("awaiting termination")
        stream_df.awaitTermination(10)
        print("streaming done")

    @staticmethod
    def _get_params(model_data_name: str) -> tuple:
        simplify_raw_data_path = (
            f"s3://{RAW_BUCKET_NAME}/{ISO}/{model_data_name}"
        )
        simplify_bronze_table_name = f"{ISO}_{model_data_name}_bronze"

        full_table_name = f"{CATALOG_NAME}/{SCHEMA_NAME}/{simplify_bronze_table_name}"
        full_checkpoint_location = f"s3://{APP_BUCKET_NAME}/{CHECKPOINT_LOCATION_PATH}/{simplify_bronze_table_name}"

        return simplify_raw_data_path, full_table_name, full_checkpoint_location
