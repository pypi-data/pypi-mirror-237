from pyspark.sql.types import StructType, StructField, TimestampType, StringType, DoubleType


schema = StructType(
    [
        StructField('interval_1h', TimestampType(), True),
        StructField('forecast_zone', StringType(), True),
        StructField('load', DoubleType(), True),
        StructField('published_timestamp', TimestampType(), True),
        StructField('parent_dataset', StringType(), True),
        StructField('parent_environment', StringType(), True),
        StructField('parent_location', StringType(), True),
        StructField('parent_version', StringType(), True)
    ]
)
