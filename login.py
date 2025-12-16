from tkinter import *
from tkinter import messagebox

def login():
    if username.get() == "admin" and password.get() == "admin123":
        messagebox.showinfo("Login", "Login Successful")
        root.destroy()
        import dashboard
    else:
        messagebox.showerror("Login", "Invalid Credentials")

root = Tk()
root.title("Login")
root.geometry("300x200")

Label(root, text="Username").pack()
username = Entry(root)
username.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
