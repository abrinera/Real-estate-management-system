import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3
from datetime import date


window=tkinter.Tk()
window.title('Update property | Developed by Era')
window.state('zoomed')
window.config(bg="#0a0908")

pid=tkinter.StringVar()
type=tkinter.StringVar()
sqfeet=tkinter.StringVar()
price=tkinter.IntVar()
room=tkinter.IntVar()
broom=tkinter.IntVar()
ld=tkinter.StringVar()
status=tkinter.StringVar()

#need edit
def add_client():
    window.destroy()
    os.system("D:/Python/python.exe  new_client.py")
    
def back():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\dashboard_admin.py")
    
def clear():
    pid.set("")
    type.set("")
    sqfeet.set("")
    price.set("")
    room.set("")
    broom.set("")
    ld.set("")
    status.set("")
 
def search():
        conn=sqlite3.connect("Property_info.db")
        cursor=conn.cursor()
        if pid.get()=="" :
            messagebox.showerror("Error!  ","   Please enter the property ID   ") 
        else:
            cursor.execute("SELECT * FROM Property WHERE property_id=? ",(pid.get(),))
            prop_row=cursor.fetchone()
            if prop_row==None:
                messagebox.showerror("Error!","  Property is not  booked or sold yet.   ") 
            else:
                #prop_id=prop_row[0]
                type1=prop_row[2]
                sqfeet1=prop_row[3]
                price1=prop_row[4]
                room1=prop_row[6]
                b_room1=prop_row[7]
                living1=prop_row[8]
                status1=prop_row[9]
                
                type.set(type1)
                sqfeet.set(sqfeet1)
                price.set(price1)
                room.set(room1)
                broom.set(b_room1)
                ld.set(living1)
                status.set(status1)

     
# add to database Personal_info   
def up(): #database
    conn = sqlite3.connect('Property_info.db')
    with conn:
        cursor= conn.cursor()
        
    #cursor.execute('CREATE TABLE IF NOT EXISTS Property (property_id VARCHAR(50) PRIMARY KEY , area TEXT, type TEXT, sqfeet INT, price INT ,address TEXT, room INT ,bathroom INT, living TEXT, status TEXT, floor VARCHAR(50), client_id VARCHAR(50)')
    
    if pid.get()=="" or type.get()=="" or sqfeet.get()=="" or price.get()=="" or room.get()=="" or broom.get()=="" or ld.get()=="" or status.get()=="" :
            messagebox.showerror("Error!  ","   All fields are required   ") 
    else:
        cursor.execute("SELECT * FROM Property WHERE property_id=?",(pid.get(),))
        row=cursor.fetchone()
        print(row)
        if row==None:
            messagebox.showerror("Error!","  Property ID doesn't Exists.   ") 
        else:
            cursor.execute('Update  Property set type=?,sqfeet=?,price=?,room=?,bathroom=?,living=?,status=? WHERE property_id=? ',
                           (type.get(),sqfeet.get(),price.get(),room.get(),broom.get(),ld.get(),status.get(),pid.get()))  
            conn.commit()
            messagebox.showinfo(title="Property Updated", message="You have successfully updated property information.")
            clear()

            fetch_property_info()

#view from Property_info
def fetch_property_info():
    conn = sqlite3.connect('Property_info.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute("SELECT property_id,type,sqfeet,price,room,bathroom,living,status FROM Property ")
        rows=cursor.fetchall()
        if len(rows)!=0:
            propertyTable.delete(*propertyTable.get_children())
            for row in rows:
                propertyTable.insert('',tkinter.END,values=row)
            conn.commit()
    
#main label   
Label(window,text=" Update Property Information 📜",bg='#0a0908', fg="#a9927d", font=("goudy old style", 16, 'bold'),pady=5).pack()

# Create Frame widget
left_frame = Frame(window, width=570, height=530, bd=7, relief=RIDGE,bg='#5e503f')
left_frame.place(x=50,y=50)

right_frame = Frame(window, width=580, height=530, bd=7, relief=RIDGE,bg='#5e503f')
right_frame.place(x=650,y=50)

#label and entry for left
type_label = tkinter.Label(left_frame, text="Type ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
sqfeet_label = tkinter.Label(left_frame, text="Sqfeet", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
price_label = tkinter.Label(left_frame, text="Price", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
room_label = tkinter.Label(left_frame, text="Room", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
bathroom_label =tkinter.Label(left_frame, text="Bathroom", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
living_label = tkinter.Label(left_frame, text="Living", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
status_label=tkinter.Label(left_frame, text="Status", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))

type_entry  = ttk.Combobox(left_frame,width=28, font=("Arial", 12),state='readonly', textvariable = type) 
type_entry ['values'] = ('Apartment','Flat','Duplex Flat','Bungalow','Villa','Standalone house','Duplex House')
sqfeet_entry = tkinter.Entry(left_frame,borderwidth=5,width=15,bg='#ede0d4', font=("Arial", 12),textvariable=sqfeet)
price_entry = tkinter.Entry(left_frame,borderwidth=5,width=15,bg='#ede0d4', font=("Arial", 12),textvariable=price)
room_entry=tkinter.Entry(left_frame,borderwidth=5,width=15,bg='#ede0d4', font=("Arial", 12),textvariable=room)
bathroom_entry=tkinter.Entry(left_frame,borderwidth=5,width=15,bg='#ede0d4', font=("Arial", 12),textvariable=broom)

living_combo = ttk.Combobox(left_frame,width=28, font=("Arial", 12),state='readonly', textvariable = ld) 
living_combo['values'] = (' Only living or dining','Living and dining attached','Living and dining separated')
status_combo = ttk.Combobox(left_frame, width=28, font=("Arial", 12),state='readonly', textvariable = status) 
status_combo['values'] = (' Available for sell','Under construction','pre constuction','Sold','Booked')  

type_label.place(x=30,y=30)
sqfeet_label.place(x=30,y=100)
price_label.place(x=30,y=170)
room_label.place(x=30,y=240)
bathroom_label.place(x=30,y=310)
living_label.place(x=30,y=380)
status_label.place(x=30,y=450)

type_entry.place(x=160,y=30)
sqfeet_entry.place(x=160,y=100)
price_entry.place(x=160,y=170)
room_entry.place(x=160,y=240)
bathroom_entry.place(x=160,y=310)
living_combo.place(x=160,y=380)
status_combo.place(x=160,y=450)


#label and entry for right and view box

pid_label=tkinter.Label(right_frame, text="Property ID ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
pid_entry=tkinter.Entry(right_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=pid)
pid_label.place(x=30,y=30)
pid_entry.place(x=160,y=30)
search_button = Button(right_frame,text=" Search Property 🔍 ",relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,),command= search )
search_button.place(x=200,y=80)


#show frame and database....................
view_frame = Frame(right_frame,  bd=7, relief=RIDGE,bg='#5e503f')
view_frame.place(x=15,y=190,width=540, height=320)

scrolly=Scrollbar(view_frame, orient=VERTICAL)
scrollx=Scrollbar(view_frame, orient=HORIZONTAL)

propertyTable=ttk.Treeview(view_frame, columns=("property_id","type", "sqfeet", "price","room","bathroom","living","status"),
                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,padding=2,takefocus=5)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

scrollx.config(command=propertyTable.xview)
scrolly.config(command=propertyTable.yview)

propertyTable.heading("property_id", text="Property ID")
propertyTable.heading("type", text="Type")
propertyTable.heading("sqfeet", text="Sq feet")
propertyTable.heading("price", text="Selling Price")
propertyTable.heading("room", text="Room")
propertyTable.heading("bathroom", text="Bathroom")
propertyTable.heading("living", text="Living")
propertyTable.heading("status", text="Status")

propertyTable["show"] = 'headings'

propertyTable.column("property_id", width=100,anchor="center")
propertyTable.column("type", width=100,anchor="center")
propertyTable.column("sqfeet", width=100,anchor="center")
propertyTable.column("price", width=100,anchor="center")
propertyTable.column("room", width=100,anchor="center")
propertyTable.column("bathroom", width=100,anchor="center")
propertyTable.column("living", width=150,anchor="center")
propertyTable.column("status", width=150,anchor="center")
propertyTable.pack(fill=BOTH, expand=True)
fetch_property_info()


#buttons
show_button = Button(window,text="Add New Client",relief=GROOVE, bg="#a9927d", fg="#0a0908", borderwidth=3,font=("times new roman", 14,),command= add_client)
show_button.place(x=50,y=600)

add_button = Button(window,text=" Update Property",relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,),command= up)
add_button.place(x=580,y=600)

back_button = Button(window, text="Back ↩",relief=GROOVE, bg="#5e503f", fg="#FFFFFF", borderwidth=3,font=("times new roman", 12,),command= back)
back_button.place(x=1160,y=600)


window.mainloop()