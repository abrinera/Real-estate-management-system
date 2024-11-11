import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3
from datetime import date


window=tkinter.Tk()
window.title('Add New Client | Developed by Era')
window.state('zoomed')
window.config(bg="#0a0908")

fname=tkinter.StringVar()   
lname=tkinter.StringVar()
gender=tkinter.StringVar()
email=tkinter.StringVar()
contact=tkinter.StringVar()
address=tkinter.StringVar()

nid=tkinter.StringVar() #nid=client_id
dob=tkinter.StringVar()
job=tkinter.StringVar()
pid=tkinter.StringVar()


#need edit
def show_client():
    window.destroy()
    os.system("D:/Python/python.exe  view_client.py")
    
def back():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\dashboard_admin.py")
    
def clear():
    fname.set("")
    lname.set("")
    gender.set("")
    email.set("")
    contact.set("")
    address.set("")
    nid.set("")
    dob.set("")
    job.set("")
    pid.set("")
    print("clear")

def add_cid_to_prop_db():
    conn = sqlite3.connect('Property_info.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute('UPDATE Property SET client_id =? WHERE property_id=?',(nid.get(),pid.get()))
        conn.commit
        cursor.execute('UPDATE Property SET status ="Booked" WHERE client_id IS NOT NULL')
        conn.commit
     
# add to database Personal_info   
def add(): #database
    conn = sqlite3.connect('Personal_info.db')
    with conn:
        cursor= conn.cursor()
    #cursor.execute('CREATE TABLE IF NOT EXISTS Client (client_id VARCHAR(50) , first_name TEXT, last_name TEXT, gender TEXT, email TEXT ,contact TEXT, date_of_birth TEXT, address TEXT, occupation TEXT, property_id VARCHAR(50) ,date TEXT,CONSTRAINT client_pk PRIMARY KEY (client_id,property_id))')
    if fname.get()=="" or lname.get()=="" or gender.get()=="" or email.get()=="" or contact.get()=="" or address.get()=="" or nid.get()=="" or dob.get()=="" or job.get()=="" or pid.get()=="" :
            messagebox.showerror("Error!","   All fields are required   ") 
    else:
        cursor.execute("SELECT * FROM Client WHERE property_id=?",(pid.get(),))
        row=cursor.fetchone()
        print(row)
        if row!=None:
            messagebox.showerror("Error!","This property already has been sold.") 
        else:
            day=date.today()
            cursor.execute('INSERT INTO Client (client_id , first_name , last_name , gender , email  ,contact , date_of_birth , address , occupation, property_id,date ) VALUES(?,?,?, ?,?,?, ?,?,?, ?,?)',
                           (nid.get() , fname.get() , lname.get() , gender.get() , email.get()  ,contact.get() , dob.get() , address.get() , job.get(), pid.get(),day))  
            conn.commit()
            messagebox.showinfo(title="Client added", message="You have successfully added new client information.")
            add_cid_to_prop_db()
            clear()
            fetch_property_info()

#view from Property_info
def fetch_property_info():
    conn = sqlite3.connect('Property_info.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute("SELECT property_id,area,sqfeet,price,room FROM Property WHERE status=' Available for sell'AND client_id IS NULL")
        rows=cursor.fetchall()
        if len(rows)!=0:
            propertyTable.delete(*propertyTable.get_children())
            for row in rows:
                propertyTable.insert('',tkinter.END,values=row)
            conn.commit()
    
#main label   
Label(window,text=" Enter New Client Information 📜",bg='#0a0908', fg="#a9927d", font=("goudy old style", 16, 'bold'),pady=5).pack()

# Create Frame widget
left_frame = Frame(window, width=570, height=530, bd=7, relief=RIDGE,bg='#5e503f')
left_frame.place(x=50,y=50)

right_frame = Frame(window, width=580, height=530, bd=7, relief=RIDGE,bg='#5e503f')
right_frame.place(x=650,y=50)

#label and entry for left
fname_label = tkinter.Label(left_frame, text="First name ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
lname_label = tkinter.Label(left_frame, text="Last name ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
gender_label = tkinter.Label(left_frame, text="Gender ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
email_label = tkinter.Label(left_frame, text="Email", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
contact_label =tkinter.Label(left_frame, text="Contact no. ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
address_label = tkinter.Label(left_frame, text="Address ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
nid_label=tkinter.Label(left_frame, text="NID ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))

fname_entry = tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable= fname)
lname_entry = tkinter.Entry(left_frame, borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=lname)
gender_entry  = ttk.Combobox(left_frame,width=28, font=("Arial", 12),state='readonly', textvariable = gender) 
gender_entry ['values'] = ('Male','Female','Transgender','Non-binary')
email_entry = tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=email)
contact_entry = tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=contact)
address_entry= tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=address) 
nid_entry=tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=nid)

fname_label.place(x=30,y=30)
lname_label.place(x=30,y=100)
gender_label.place(x=30,y=170)
email_label.place(x=30,y=240)
contact_label.place(x=30,y=310)
address_label.place(x=30,y=380)
nid_label.place(x=30,y=450)

fname_entry.place(x=160,y=30)
lname_entry.place(x=160,y=100)
gender_entry.place(x=160,y=170)
email_entry.place(x=160,y=240)
contact_entry.place(x=160,y=310)
address_entry.place(x=160,y=380)
nid_entry.place(x=160,y=450)


#label and entry for right and view box

dob_label=tkinter.Label(right_frame, text="Birth Date ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
job_label=tkinter.Label(right_frame, text="Occupation", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
pid_label=tkinter.Label(right_frame, text="Property ID ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))

dob_entry=tkinter.Entry(right_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=dob)
job_entry=tkinter.Entry(right_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=job)
pid_entry=tkinter.Entry(right_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=pid)

dob_label.place(x=30,y=30)
job_label.place(x=30,y=100)
pid_label.place(x=30,y=170)

dob_entry.place(x=160,y=30)
job_entry.place(x=160,y=100)
pid_entry.place(x=160,y=170)


#show frame and database....................
view_frame = Frame(right_frame, width=540, height=280, bd=7, relief=RIDGE,bg='#5e503f')
view_frame.place(x=15,y=230)

scrolly=Scrollbar(view_frame, orient=VERTICAL)
scrollx=Scrollbar(view_frame, orient=HORIZONTAL)

propertyTable=ttk.Treeview(view_frame, columns=("property_id", "area", "sqfeet", "price","room"),
                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,padding=2,takefocus=5)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

scrollx.config(command=propertyTable.xview)
scrolly.config(command=propertyTable.yview)

propertyTable.heading("property_id", text="Property ID")
propertyTable.heading("area", text="Area")
propertyTable.heading("sqfeet", text="Sq feet")
propertyTable.heading("price", text="Selling Price")
propertyTable.heading("room", text="Room")


propertyTable["show"] = 'headings'

propertyTable.column("property_id", width=100,anchor="center")
propertyTable.column("area", width=100,anchor="center")
propertyTable.column("sqfeet", width=100,anchor="center")
propertyTable.column("price", width=100,anchor="center")
propertyTable.column("room", width=100,anchor="center")

propertyTable.pack(fill=BOTH, expand=True)
fetch_property_info()


#buttons
show_button = Button(window,text="View Clients",relief=GROOVE, bg="#a9927d", fg="#0a0908", borderwidth=3,font=("times new roman", 14,),command= show_client)
show_button.place(x=50,y=600)

add_button = Button(window,text=" Add Client ",relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,),command= add)
add_button.place(x=580,y=600)

back_button = Button(window, text="Back ↩",relief=GROOVE, bg="#5e503f", fg="#FFFFFF", borderwidth=3,font=("times new roman", 12,),command= back)
back_button.place(x=1160,y=600)


window.mainloop()