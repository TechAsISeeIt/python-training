from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from models import StudentResponse, Students
from deps import verify_token, rate_limiter, verify_basic_auth

import sqlite3 as sql
import httpx
import os

app = FastAPI(title="ETL API", version="1.0")

db_path = os.path.join(os.path.dirname(__file__), "..", "sampledata", "student.db")

# ✅ CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


def get_db():
    conn = sql.connect(db_path)
    return conn


# Root path
@app.get("/")
def root():
    return "Welcome to ETL API!!!"


# ✅ Health Check
@app.get("/health")  # decorator used to create API endpoint or Route
def health():
    return {"status": "ok"}


@app.post("/post")
def post():
    return {"status": "ok"}


@app.get("/student", response_model=Students)
def get_students(db=Depends(get_db), creds=Depends(verify_token)):
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM STUDENTS""")
    columns = [desc[0] for desc in cursor.description]
    # Convert rows to a list of dictionaries
    results = [dict(zip(columns, row)) for row in cursor.fetchall()]
    db.close()
    return {"items": results}


@app.get("/student/{id}", response_model=StudentResponse)
def get_student(
    id: int,
    db=Depends(get_db),
    creds=Depends(verify_basic_auth),
    rate_limiting=Depends(rate_limiter),
):
    cursor = db.cursor()
    cursor.execute(f"""SELECT * FROM STUDENTS WHERE ID = {id}""")
    columns = [desc[0] for desc in cursor.description]
    # Convert rows to a list of dictionaries
    row = cursor.fetchone()
    results = dict(zip(columns, row))
    db.close()
    return results


# DB (Source) -> API -> Expose

# API (Source) -> OUR API -> Expose


# ✅ Async External Call Example
@app.get("/jsonplaceholder")
async def fetch_external():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://jsonplaceholder.typicode.com/posts")
        return response.json()
