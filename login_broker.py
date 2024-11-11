import tkinter
from tkinter import *
from tkinter import messagebox
import os
import sqlite3

window = tkinter.Tk()
window.title("Login- Real Estate Management System | Developed by Era")
window.geometry('480x440')
window.state('zoomed')
window.configure(bg='#5e503f')

use=tkinter.StringVar()
password=tkinter.StringVar()

def login():
    conn = sqlite3.connect('Personal_info.db')
    cursor= conn.cursor()
    cursor.execute("SELECT password FROM Employee WHERE user_name=?",(use.get(),))
    row=cursor.fetchone()
    pas=row[0]
    

    if  password_entry.get()==password:
        #messagebox.showinfo(title="Login Successful!", message="You have successfully logged in.")
        window.destroy()
        os.system(" D:/Python/python.exe E:\REMS\dashboard_broker.py")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def back():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\log.py")

frame = tkinter.Frame(bg='#5e503f')

login_label = tkinter.Label(frame, text="  Login as Broker  ", bg='#5e503f', fg="#a9927d",relief=RIDGE,width=20, font=("times new roman", 22, 'bold'))
username_label = tkinter.Label(frame, text="Username", bg='#5e503f', fg="#FFFFFF", font=("times new roman", 14, 'bold'))
password_label = tkinter.Label(frame, text="Password", bg='#5e503f', fg="#FFFFFF", font=("times new roman", 14, 'bold'))

username_entry = tkinter.Entry(frame, borderwidth=3,font=("Arial", 12),textvariable=use)
password_entry = tkinter.Entry(frame,borderwidth=3, show="*", font=("Arial", 12),textvariable=password)

login_button = tkinter.Button(frame, text="  Login  ",width=10, bg="#a9927d", fg="#49111a",borderwidth=3, font=("times new roman", 14,"bold"), command=login)
back_button = tkinter.Button(frame, text= "  Back  ",width=10, bg="#a9927d", fg="#49111a", borderwidth=3,font=("times new roman", 14,"bold"), command=back)

login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=3, pady=10)
back_button.grid(row=4, column=0, columnspan=3, pady=10)

frame.pack()
window.mainloop()