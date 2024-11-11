import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3


window=Tk()
#window config
window.title('View available properties| Developed by Era ')
window.state('zoomed')
window.config(bg="#0a0908")


def home():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\dashboard_admin.py")
#need edid    
def add_client():
    window.destroy()
    os.system(" D:/Python/python.exe  new_client.py") 
  
def sold():
    window.destroy()
    os.system(" D:/Python/python.exe  new_property.py")


#shows data from database
def fetch_property_info():
    conn = sqlite3.connect('Property_info.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute("SELECT * FROM Property WHERE status=' Available for sell'AND client_id IS NULL")
        rows=cursor.fetchall()
        if len(rows)!=0:
            propertyTable.delete(*propertyTable.get_children())
            for row in rows:
                propertyTable.insert('',tkinter.END,values=row)
            conn.commit()
        
    
    
Label(window,text=" 🏠 Real Estate Management System Property List ", border=5, relief=GROOVE,bg='#0a0908', fg="#a9927d", font=("goudy old style", 15, 'bold'),pady=10).pack()

#view frame
all_Frame=Frame(window, bd=10, relief=RIDGE)
all_Frame.place(x=50, y=60, width=1180, height=520)

scrolly=Scrollbar(all_Frame, orient=VERTICAL)
scrollx=Scrollbar(all_Frame, orient=HORIZONTAL)

propertyTable=ttk.Treeview(all_Frame, columns=("property_id", "area", "type", "sqfeet", "price","address",
                                               "room","bathroom","living","status","floor","client_id"),
                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,padding=2,takefocus=5)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

scrollx.config(command=propertyTable.xview)
scrolly.config(command=propertyTable.yview)

propertyTable.heading("property_id", text="Property ID")
propertyTable.heading("area", text="Area")
propertyTable.heading("type", text="Type of property")
propertyTable.heading("sqfeet", text="Sq feet")
propertyTable.heading("price", text="Selling Price")
propertyTable.heading("address", text="Address")
propertyTable.heading("room", text="Room")
propertyTable.heading("bathroom", text="Bathroom")
propertyTable.heading("living", text="Living and Dining")
propertyTable.heading("status", text="Status")
propertyTable.heading("floor", text="Floor")
propertyTable.heading("client_id", text="Client ID")

propertyTable["show"] = 'headings'

propertyTable.column("property_id", width=100,anchor="center")
propertyTable.column("area", width=100,anchor="center")
propertyTable.column("type", width=100,anchor="center")
propertyTable.column("sqfeet", width=100,anchor="center")
propertyTable.column("price", width=100,anchor="center")
propertyTable.column("address", width=200,anchor="center")
propertyTable.column("room", width=70,anchor="center")
propertyTable.column("bathroom", width=70,anchor="center")
propertyTable.column("living", width=200,anchor="center")
propertyTable.column("status", width=150,anchor="center")
propertyTable.column("floor", width=70,anchor="center")
propertyTable.column("client_id", width=100,anchor="center")

propertyTable.pack(fill=BOTH, expand=True)
fetch_property_info()

#buttons
home_button = Button(window,text="Home 🏚",relief=GROOVE, bg="#a9927d", fg="#0a0908", borderwidth=3,font=("times new roman", 14,),command= home)
home_button.place(x=50,y=600)

add_client_button = Button(window,text="Add Client",relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,),command=add_client)
add_client_button.place(x=580,y=600)

sold_button = Button(window, text="Add New Properties ",relief=GROOVE, bg="#5e503f", fg="#FFFFFF", borderwidth=3,font=("times new roman", 12,),command= sold)
sold_button.place(x=1080,y=600)


window.mainloop()