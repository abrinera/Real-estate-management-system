import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3
from datetime import date

window = Tk()
# window config
window.title('Broker Registration  | Devoloped By Murad')
window.state('zoomed')
window.config(bg="#0a0908")

empid=tkinter.StringVar()
name=tkinter.StringVar   
uname=tkinter.StringVar()
gender=tkinter.StringVar()
dob=tkinter.StringVar()
email=tkinter.StringVar()
pas=tkinter.StringVar()
# need edit

#clear
def clear():
    empid.set("")
    name.set("")
    uname.set("")
    gender.set("")
    email.set("")
    pas.set("")
    dob.set("")

def fetch_client_info():
    conn = sqlite3.connect('Personal_info.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute("SELECT * FROM Employee")
        rows=cursor.fetchall()
        if len(rows)!=0:
            empTable.delete(*empTable.get_children())
            for row in rows:
                empTable.insert('',tkinter.END,values=row)
            conn.commit()

def add(): #database
    conn = sqlite3.connect('Personal_info.db')
    with conn:
        cursor= conn.cursor()
    #cursor.execute('CREATE TABLE IF NOT EXISTS Client (client_id VARCHAR(50) , first_name TEXT, last_name TEXT, gender TEXT, email TEXT ,contact TEXT, date_of_birth TEXT, address TEXT, occupation TEXT, property_id VARCHAR(50) ,date TEXT,CONSTRAINT client_pk PRIMARY KEY (client_id,property_id))')
#    if empid.get()=="" or name.get()=="" or uname.get()=="" or email.get()=="" or pas.get()=="" :
#            messagebox.showerror("Error!","   All fields are required   ") 
#    else:
        cursor.execute("SELECT * FROM Employee WHERE emp_id=?",(empid.get(),))
        row=cursor.fetchone()
        print(row)
        if row!=None:
            messagebox.showerror("Error!","Already exist.") 
        else:
            title="broker"
            day=date.today()
            cursor.execute('INSERT INTO Employee (emp_id, name, user_name, gender, date_of_birth, title, email, password, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (empid.get() , name.get() , uname.get() , gender.get() , dob.get() ,title , email.get()  ,pas.get() , day))  
            conn.commit()
            messagebox.showinfo(title="Client added", message="You have successfully added new Broker information.")
            clear()
            fetch_client_info()
            conn.close()

def back():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\dashboard_admin.py")

# Create Frame widget
left_frame = Frame(window, width=560, height=550, borderwidth=5, bg='#5e503f')
left_frame.place(x=30, y=30)

right_frame = Frame(window, borderwidth=5,bg='#5e503f')
right_frame.place(x=600,y=30,width=650, height=550,)

# label and entry for left
Label(left_frame, text=" Enter New Broker Information  ", relief=SOLID, bg='#0a0908', fg="#a9927d",font=("times new roman", 15, 'bold')).place(x=200, y=0)

Label(left_frame, text="Employee ID:", bg='#5e503f', fg="#a9927d",font=("times new roman", 13,'bold')).place(x=50, y=70)
employee_id_entry = Entry(left_frame,borderwidth=5,width=30, font=("Arial", 12),textvariable=empid)
employee_id_entry.place(x=200, y=70)

Label(left_frame, text="Name:", bg='#5e503f', fg="#a9927d",font=("times new roman", 13,'bold')).place(x=50, y=130)
first_name_entry = Entry(left_frame,borderwidth=5,width=30, font=("Arial", 12),textvariable=name)
first_name_entry.place(x=200, y=130)

Label(left_frame, text="User Name:", bg='#5e503f', fg="#a9927d",font=("times new roman", 13,'bold')).place(x=50, y=190)
last_name_entry = Entry(left_frame,borderwidth=5,width=30, font=("Arial", 12),textvariable=uname)
last_name_entry.place(x=200, y=190)

Label(left_frame, text="Gender:", bg='#5e503f', fg="#a9927d",font=("times new roman", 13,'bold')).place(x=50, y=250)
gender_entry  = ttk.Combobox(left_frame,width=28, font=("Arial", 12),state='readonly', textvariable = gender) 
gender_entry ['values'] = ('Male','Female','Transgender','Non-binary')
gender_entry.place(x=200, y=250)

Label(left_frame, text="Date of Birth:", bg='#5e503f', fg="#a9927d",font=("times new roman", 13,'bold')).place(x=50, y=310)
dob_entry = Entry(left_frame,borderwidth=5,width=30, font=("Arial", 12),textvariable=dob)
dob_entry.place(x=200, y=310)

Label(left_frame, text="Email:", bg='#5e503f', fg="#a9927d",font=("times new roman", 13, 'bold')).place(x=50, y=370)
email_entry = Entry(left_frame,borderwidth=5,width=30, font=("Arial", 12),textvariable=email)
email_entry.place(x=200, y=370)

Label(left_frame, text="Password:", bg='#5e503f', fg="#a9927d",font=("times new roman", 13,'bold')).place(x=50, y=430)
password_entry = Entry(left_frame,borderwidth=5,width=30, font=("Arial", 12),textvariable=pas)
password_entry.place(x=200, y=430)


# Right frame from emp view data

scrolly=Scrollbar(right_frame, orient=VERTICAL)
scrollx=Scrollbar(right_frame, orient=HORIZONTAL)

empTable=ttk.Treeview(right_frame, columns=('emp_id' , 'name' , 'user_name', 'gender', 'date_of_birth' ,
                                             'title','email'  ,'password'  , 'date' ),
                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,padding=2,takefocus=5)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

scrollx.config(command=empTable.xview)
scrolly.config(command=empTable.yview)

empTable.heading("emp_id", text="Employee ID")
empTable.heading("title", text="Title")
empTable.heading("name", text="Name")
empTable.heading("user_name", text="User Name")
empTable.heading("gender", text="Gender")
empTable.heading("date_of_birth", text="Date of Birth")
empTable.heading("email", text="Email")
empTable.heading("password", text="Password")
empTable.heading("date", text="Registration Date")

empTable["show"] = 'headings'

empTable.column("emp_id", width=100,anchor="center")
empTable.column("title", width=100,anchor="center")
empTable.column("name", width=100,anchor="center")
empTable.column("user_name", width=100,anchor="center")
empTable.column("gender", width=100,anchor="center")
empTable.column("date_of_birth", width=100,anchor="center")
empTable.column("email", width=100,anchor="center")
empTable.column("password", width=100,anchor="center")
empTable.column("date", width=100,anchor="center")

empTable.pack(fill=BOTH, expand=True)
fetch_client_info()


# buttons


add_button = Button(window, text="Add Details", relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,
                    font=("times new roman", 14,), command=add)
add_button.place(x=60, y=600)

back_button = Button(window, text="Back ↩", relief=GROOVE, bg="#5e503f", fg="#FFFFFF", borderwidth=3,
                     font=("times new roman", 12,), command=back)
back_button.place(x=1160, y=600)

window.mainloop()
