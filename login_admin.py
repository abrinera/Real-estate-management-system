import tkinter
from tkinter import *
from tkinter import messagebox
import os

window = tkinter.Tk()
window.title("Login- Real Estate Management System | Developed by Era")
window.geometry('480x440')
window.state('zoomed')
window.configure(bg='#0a0908')

def login():
    username = "abrin_era"
    password = "era3116"

    if username_entry.get()==username and password_entry.get()==password:
        #messagebox.showinfo(title="Login Successful!", message=" You have successfully logged in.")
        window.destroy()
        os.system(" D:/Python/python.exe E:\REMS\dashboard_admin.py")
    else:
        messagebox.showerror(title="  Error  ", message="  Invalid login.  ")

def back():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\log.py")
    
frame = tkinter.Frame(bg='#0a0908',relief=RIDGE)

login_label = tkinter.Label(frame, text="Login as Admin", bg='#0a0908', fg="#a9927d",relief=RIDGE,width=20, font=("times new roman", 22, 'bold'))
username_label = tkinter.Label(frame, text="Username", bg='#0a0908', fg="#a9927d", font=("times new roman", 14, 'bold'))
password_label = tkinter.Label(frame, text="Password", bg='#0a0908', fg="#a9927d", font=("times new roman", 14, 'bold'))

username_entry = tkinter.Entry(frame,borderwidth=3, font=("Arial", 12))
password_entry = tkinter.Entry(frame, borderwidth=3,show="*", font=("Arial", 12))

login_button = tkinter.Button(frame, text="  Login  ", bg="#49111c",width=10, fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,"bold"), command=login)
back_button = tkinter.Button(frame, text= "  Back  ", bg="#49111c",width=10, fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,"bold"), command=back)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)

login_button.grid(row=3, column=0, columnspan=3, pady=20)
back_button.grid(row=4, column=0, columnspan=3, pady=20)

frame.pack()
window.mainloop()