import pandas as pd
import random
import os

names = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eva",
    "Frank",
    "Grace",
    "Helen",
    "Ivan",
    "Julia",
    "Kevin",
    "Laura",
    "Michael",
    "Nina",
    "Oscar",
    "Paula",
    "Quentin",
    "Rachel",
    "Steve",
    "Tina",
]

surnames = [
    "Smith",
    "Johnson",
    "Brown",
    "Williams",
    "Miller",
    "Davis",
    "Garcia",
    "Martinez",
    "Anderson",
    "Taylor",
]

departments = [
    "Computer Science",
    "Information Technology",
    "Electronics",
    "Mechanical",
    "Civil",
    "Data Science",
]

rows = []

for i in range(1, 10001):
    rows.append(
        {
            "student_id": i,
            "name": random.choice(names) + " " + random.choice(surnames),
            "department": random.choice(departments),
            "age": random.randint(18, 25),
            "exam_score": random.randint(50, 100),
            "attendance_percent": random.randint(60, 100),
            "assignment_score": random.randint(50, 100),
        }
    )

df = pd.DataFrame(rows)
df.to_csv(
    os.path.join(
        os.path.dirname(__file__), "sampledata/students_large_training_dataset.csv"
    ),
    index=False,
)
