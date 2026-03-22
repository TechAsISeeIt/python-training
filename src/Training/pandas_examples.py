import pandas as pd
import os

df = pd.read_csv(
    os.path.join(os.path.dirname(__file__), "sampledata/students_training_dataset.csv")
)  # relative path
# For ex: Base Path: C:\Users\UdayDoppalapudi\Training\PythonTraining\src\Training
# Relartive: sampledata/csv

# print(
#     df.head()
# )  # By default reads 5 rows. if number is passed as parameter then that many rows will be printed

# print(df)  # Fetches all rows

# print(df.info()) # Schema Information

# print(df.describe()) # statistical information

# print(df['name']) # to pick single column

# print(df[['name', 'age', 'score']]) # to pick mulitple columns

# print(df[df['attendance'] > 90]) # Condition to the df - Filter data

# print(df.sort_values(by=['attendance', 'score'], ascending=True))

# Derived Columns
df["passed"] = df["score"] >= 80
df["result"] = "fail"
df.loc[df["score"] >= 80, "result"] = "pass"
# print(df)

# print(df.groupby("department")['score'].sum()) # Grouping and Aggregating - mean, sum, count

# print(df.dropna()) # Drops NUll values
# print(df.fillna('NA')) # Replace null with default values

df.to_csv(os.path.join(os.path.dirname(__file__), "sampledata/result.csv"), index=False)
df.to_json(
    os.path.join(os.path.dirname(__file__), "sampledata/result.json"), index=False
)
