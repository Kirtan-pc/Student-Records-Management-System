import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    RollNo TEXT,
    Department TEXT,
    Year TEXT,
    PhoneNo  TEXT,
    EmailID TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully")
