import os

# VARIABLES
ENVIRONMENT = os.getenv("ENVIRONMENT")

ML_OPS_ENVIRONMENT = os.getenv("ML_OPS_ENVIRONMENT")

CATALOG_NAME = f"pr_unrestricted_{ENVIRONMENT}"

PR_PLATFORM_SCHEMA_NAME = "platform"

SCHEMA_NAME = "prt"

ISO = "ercot"

TRIGGER_INTERVAL_SECONDS = 30
DELETE_DELTA_TABLES = True

#################### BUCKETS VARIABLES ####################
RAW_BUCKET_NAME = "enverus-pr-ue1-cdr-unrestricted-mu-ingested-prod"
APP_BUCKET_NAME = f"enverus-pr-ue1-cdr-unrestricted-prt-app-{ML_OPS_ENVIRONMENT}"


CHECKPOINT_LOCATION_PATH = f"_checkpoints/7da_data_ingest/{ML_OPS_ENVIRONMENT}"
DELTA_FORMAT = "delta"

FILE_FORMAT = "parquet"  # parquet
