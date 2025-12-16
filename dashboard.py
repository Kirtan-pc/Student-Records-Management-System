from tkinter import *
from tkinter import messagebox
from CRUDoperations import count_students
import os
from CRUDoperations import export_to_csv
import graph


def export_data():
    export_to_csv()
    messagebox.showinfo("Export", "Student data exported to CSV file")

def open_add_student():
    os.system("python addStudent.py")

def show_total_students():
    total = count_students()
    messagebox.showinfo("Total Students", f"Total Students: {total}")

root = Tk()
root.title("Dashboard")
root.geometry("400x300")

Label(root, text="Student Record System", font=("Arial", 16)).pack(pady=20)

Button(root, text="Add Student", width=20, command=open_add_student).pack(pady=5)

Button(root, text="Export to CSV", width=20, command=export_data).pack(pady=5)

Button(root, text="Show Graph", width=20, command=lambda: __import__("graph")).pack(pady=5)
