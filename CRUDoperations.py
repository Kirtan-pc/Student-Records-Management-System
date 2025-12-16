import csv
from Database import sqlite3

def export_to_csv():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    with open("students_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "RollNo", "Department", "Year", "PhoneNo", "EmailID"])
        writer.writerows(rows)

    conn.close()


def add_student(Name, RollNo, Department, Year, PhoneNo, EmailID):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (Name, RollNo, Department, Year, PhoneNo, EmailID)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (Name, RollNo, Department, Year, PhoneNo, EmailID))

    conn.commit()
    conn.close()


def search_student(RollNo):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE RollNo = ?",
        (RollNo,)
    )

    result = cursor.fetchone()
    conn.close()
    return result


def count_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    total = cursor.fetchone()[0]

    conn.close()
    return total
