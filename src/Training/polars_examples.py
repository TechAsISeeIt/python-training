import polars as pl
import os

if __name__ == "__main__":
    df = pl.read_csv(
        os.path.join(
            os.path.dirname(__file__), "sampledata/students_large_training_dataset.csv"
        )
    )
    # df[['name', 'exam_score']] -> pd
    # df.select(['name', 'exam_score']) -> pl
    # print(df.select(['name', 'exam_score']))

    # df[df['exam_score']>80]
    # df.filter(pl.col('exam_sxore')>80)
    # pl.col -> gives column values are series
    print(df.filter(pl.col("exam_score") == 100))

    # df.groupby("department")['score'].sum()
    # df.group_by("department").agg(pl.col("attendance_percent").mean())
    print(df.group_by("department").agg(pl.col("attendance_percent").mean()))

    # df.sort_values(by=['attendance', 'score'], ascending=True)
    # df.sort(by=pl.col("exam_score"), descending=True)
    print(df.sort(by=pl.col("exam_score"), descending=False))
