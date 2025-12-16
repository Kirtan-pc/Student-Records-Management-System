import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
SELECT Department, COUNT(*) 
FROM students 
GROUP BY Department
""")

data = cursor.fetchall()
conn.close()

departments = [row[0] for row in data]
counts = [row[1] for row in data]

plt.bar(departments, counts)
plt.xlabel("Department")
plt.ylabel("Number of Students")
plt.title("Students per Department")
plt.show()
