from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AutoScalingDemo") \
    .config("spark.dynamicAllocation.enabled", "true") \
    .getOrCreate()

df = spark.range(10000000)  # Test workload
df.write.parquet("output/processed_data")

# Enhanced aggregations
from pyspark.sql.functions import window, col

def time_buckets(df, interval="1 hour"):
    return df.groupBy(
        window("timestamp", interval),
        col("currency")
    ).agg(
        {"amount": "avg", "quantity": "sum"}
    ).withColumnRenamed("avg(amount)", "avg_price")
