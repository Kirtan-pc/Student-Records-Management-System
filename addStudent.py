import sqlite3
from tkinter import *
from tkinter import messagebox

def save():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students (Name, RollNo, Department, Year, PhoneNo, EmailID)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        Name.get(), RollNo.get(), Department.get(),
        Year.get(), PhoneNo.get(), EmailID.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Student Added")

root = Tk()
root.title("Add Student")
root.geometry("300x400")

Name = Entry(root); RollNo = Entry(root)
Department = Entry(root); Year = Entry(root)
PhoneNo = Entry(root); EmailID = Entry(root)

for label, field in [
    ("Name", Name), ("Roll", RollNo), ("Department", Department),
    ("Year", Year), ("Phone", PhoneNo), ("Email", EmailID)
]:
    Label(root, text=label).pack()
    field.pack()

Button(root, text="Save", command=save).pack(pady=10)

root.mainloop()
