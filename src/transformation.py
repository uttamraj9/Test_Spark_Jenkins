from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder \
        .appName("Sample Jenkins Spark Job") \
        .getOrCreate()

    data = [("Uttam", 30), ("Raj", 28), ("DataEng", 5)]
    df = spark.createDataFrame(data, ["name", "experience"])

    result_df = df.filter(df.experience > 10)

    result_df.show()

    # Example write (can be HDFS/S3)
    result_df.write.mode("overwrite").csv("/tmp/output/sample_job")

    spark.stop()