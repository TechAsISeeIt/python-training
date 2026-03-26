import duckdb as ddb
import os

if __name__ == "__main__":
    path = os.path.join(
        os.path.dirname(__file__), "sampledata/students_large_training_dataset.csv"
    )
    df = ddb.sql(f""" SELECT * FROM '{path}' """)  # fetches all data

    df = ddb.sql(
        f""" SELECT * FROM '{path}' WHERE exam_score = 100 """
    )  # Filters rows where exam_score = 100

    df = ddb.sql(
        f""" SELECT name, exam_score FROM '{path}' """
    )  # fetches specified columns data

    df = ddb.sql(
        f""" SELECT department, AVG(attendance_percent) FROM '{path}' GROUP BY department"""
    )  # Group by And Aggregations

    print(df)
