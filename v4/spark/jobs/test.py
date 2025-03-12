

from pyspark.sql import SparkSession
spark = (
    SparkSession.builder.appName("generate").getOrCreate()
)

from faker import Faker
fake = Faker()
name = fake.name()           # e.g., "John Doe"
email = fake.email()         # e.g., "john.doe@example.com"
address = fake.address()     # e.g., "123 Main St, Springfield, IL 62701"
phone = fake.phone_number()

fake_users = [{
    'name': fake.name(),
    'email': fake.email(),
    'birthdate': fake.date_of_birth(minimum_age=18, maximum_age=90)
} for _ in range(10)]
df = spark.createDataFrame(fake_users)
df.write.parquet("s3a://test/fake_users", mode="overwrite")

# df = spark.read.csv("s3a://test/idc_btt.csv", header=True, inferSchema=True)

# Show the DataFrame
# df.show()