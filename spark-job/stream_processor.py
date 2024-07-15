from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("AutoScalingDemo") \
    .config("spark.dynamicAllocation.enabled", "true") \
    .getOrCreate()

df = spark.range(10000000)  # Test workload
df.write.parquet("output/processed_data")
