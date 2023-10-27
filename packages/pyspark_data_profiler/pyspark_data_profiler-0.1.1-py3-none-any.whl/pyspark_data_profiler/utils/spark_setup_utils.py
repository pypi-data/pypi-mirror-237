from pyspark.sql import SparkSession


# initialize spark session
spark = SparkSession.builder.appName("SparkProfiler").getOrCreate()
sc = spark.sparkContext
sc.setLogLevel('OFF')
