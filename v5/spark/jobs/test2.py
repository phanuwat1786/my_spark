from pyspark.sql import SparkSession
spark = (
    SparkSession.builder.appName("generate").getOrCreate()
)
print("Spark version:", spark.version)
df = spark.createDataFrame([(1, "test"), (2, "spark")], ["id", "value"])
df.show()