import sqlite3 as sql
import os

db_path = os.path.join(os.path.dirname(__file__), "..", "sampledata", "student.db")

# import pyodbc - this for hosted database connections

"""
DNS Service
| IP Address   | Name           |
---------------------------------   -
| 10.44.24.150 | RithvikDB.ac.us|
"""

if __name__ == "__main__":
    # Establish Connection
    """
    Host/ServerName: domain name like sqlserver.microsoft.ac.uk (FQDN) or Ip address - 10.25.44.138 FQDN - Fully Qulified Domain Name - Alias to a target IP address - DNS (Domain Naming Service)
    FQDN for local server - localhost
    IP address for local server - 127.0.0.1
    Port: 1532 - InBound OutBound Connection - Door to your server
    Username
    Password

    localhost:9001
    sys
    admin@123
    """
    conn = sql.connect(db_path)

    # Get Cursor from connection
    cursor = conn.cursor()

    # ToDo SQL Sections
    # cursor.execute("""CREATE TABLE STUDENTS (ID INTEGER, NAME TEXT, SCORE INTEGER)""")

    """Insert a single row"""
    # cursor.execute("""INSERT INTO STUDENTS (ID, NAME, SCORE) VALUES (1, 'Rithvik', 80)""")

    """Insert mulitple records"""
    # cursor.executemany("""INSERT INTO STUDENTS (ID, NAME, SCORE) VALUES (?,?,?)""", [(1, 'Ritvik', 85), (2, 'Gayatri', 80), (3, 'Uday', 80)])

    """Commits DB Changes i.e. Finalize all changes and saves them"""
    # conn.commit()

    """FETCH ONE RECORD FROM CURSOR"""
    cursor.execute("""SELECT * FROM STUDENTS""")
    rows = cursor.fetchone()

    """FETCH ALL RECORDS FROM CURSOR"""
    cursor.execute("""SELECT * FROM STUDENTS""")
    rows = cursor.fetchall()  # all rows in the table

    print(rows)

    """Closes the DB Connection"""
    conn.close()
