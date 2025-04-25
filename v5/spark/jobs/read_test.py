from pyspark.sql import SparkSession
spark = (
    SparkSession.builder.appName("read_parq").getOrCreate()
)

df = spark.read.parquet("s3a://test/fake_users")
df.show()
df.write.csv("s3a://test/fake_users.csv", mode="overwrite")