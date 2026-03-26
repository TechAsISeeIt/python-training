from pyspark.sql import SparkSession  # SparkSession class import
from pyspark.sql.functions import (
    col,
)  # Col Function used to work with DataFrame columns
import os  # os functions - path, env variables

if __name__ == "__main__":

    """Initialize Spark Session"""
    spark = SparkSession.builder.appName("pyspark_examples").getOrCreate()

    df = spark.read.csv(
        os.path.join(
            os.path.dirname(__file__), "sampledata/students_large_training_dataset.csv"
        ),
        header=True,
        inferSchema=True,
    )

    """Filtering Data"""
    df.filter(col("exam_score") >= 85).show()

    """Group By and Aggregation"""
    df.groupBy(col("department")).count().show()
