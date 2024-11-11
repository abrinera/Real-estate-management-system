import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3


window=Tk()
window.title('View client information| Developed by Era ')
window.state('zoomed')
window.config(bg="#0a0908")


#need edit
def home():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\dashboard_admin.py")
#need edid    
def trans_info():
    window.destroy()
    os.system(" D:/Python/python.exe  new_trans.py")
def back():
    window.destroy()
    os.system(" D:/Python/python.exe  new_client.py")


#shows data from database
def fetch_client_info():
    conn = sqlite3.connect('Personal_info.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute("SELECT * FROM Client")
        rows=cursor.fetchall()
        if len(rows)!=0:
            clientTable.delete(*clientTable.get_children())
            for row in rows:
                clientTable.insert('',tkinter.END,values=row)
            conn.commit()
        
    
    
Label(window,text=" 🏠 Real Estate Management System Client Information ", border=5, relief=GROOVE,bg='#0a0908', fg="#a9927d", font=("goudy old style", 15, 'bold'),pady=10).pack()

#view frame
all_Frame=Frame(window, bd=10, relief=RIDGE)
all_Frame.place(x=50, y=60, width=1180, height=520)

scrolly=Scrollbar(all_Frame, orient=VERTICAL)
scrollx=Scrollbar(all_Frame, orient=HORIZONTAL)

clientTable=ttk.Treeview(all_Frame, columns=('client_id' , 'first_name' , 'last_name', 'gender' ,
                                             'email'  ,'contact' , 'date_of_birth' , 'address' ,
                                             'occupation', 'property_id','date' ),
                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,padding=2,takefocus=5)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

scrollx.config(command=clientTable.xview)
scrolly.config(command=clientTable.yview)

clientTable.heading("client_id", text="Client ID")
clientTable.heading("first_name", text="First Name")
clientTable.heading("last_name", text="Last Name")
clientTable.heading("gender", text="Gender")
clientTable.heading("email", text="Email")
clientTable.heading("contact", text="Contact")
clientTable.heading("date_of_birth", text="Date of Birth")
clientTable.heading("address", text="Address")
clientTable.heading("occupation", text="Occupation")
clientTable.heading("property_id", text="Property ID")
clientTable.heading("date", text="Registration Date")

clientTable["show"] = 'headings'

clientTable.column("client_id", width=100,anchor="center")
clientTable.column("first_name", width=150,anchor="center")
clientTable.column("last_name", width=150,anchor="center")
clientTable.column("gender", width=100,anchor="center")
clientTable.column("email", width=150,anchor="center")
clientTable.column("contact", width=100,anchor="center")
clientTable.column("date_of_birth", width=70,anchor="center")
clientTable.column("address", width=250,anchor="center")
clientTable.column("occupation", width=100,anchor="center")
clientTable.column("property_id", width=100,anchor="center")
clientTable.column("date", width=100,anchor="center")

clientTable.pack(fill=BOTH, expand=True)
fetch_client_info()

#buttons
home_button = Button(window,text="Home 🏚",relief=GROOVE, bg="#a9927d", fg="#0a0908", borderwidth=3,font=("times new roman", 14,),command= home)
home_button.place(x=50,y=600)

update_client_button = Button(window,text="New Transaction",relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,),command= trans_info)
update_client_button.place(x=580,y=600)

back_button = Button(window, text="Back ↩",relief=GROOVE, bg="#5e503f", fg="#FFFFFF", borderwidth=3,font=("times new roman", 12,),command= back)
back_button.place(x=1160,y=600)


window.mainloop()