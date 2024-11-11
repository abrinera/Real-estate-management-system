import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3


window=tkinter.Tk()
window.title('Update new property')
window.state('zoomed')
window.config(bg="#0a0908")

pid=tkinter.StringVar()
area=tkinter.StringVar()
type=tkinter.StringVar()
sqfeet=tkinter.StringVar()
price=tkinter.StringVar()
address=tkinter.StringVar()
room=tkinter.StringVar()
broom=tkinter.StringVar()
ld=tkinter.StringVar()
status=tkinter.StringVar()
floor=tkinter.StringVar()

#need edit
def show_property():
    window.destroy()
    os.system("D:/Python/python.exe  all_property.py")
#need edit    
def back():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\dashboard_admin.py")
    
    
def clear():
    pid.set("")
    area.set("")
    type.set("")
    sqfeet.set("")
    price.set("")
    address.set("")
    room.set("")
    broom.set("")
    ld.set("")
    status.set("")
    floor.set("")
    print("clear")
    
    
def add(): #database
    conn = sqlite3.connect('Property_info.db')
    with conn:
        cursor= conn.cursor()
        
    #cursor.execute('CREATE TABLE IF NOT EXISTS Property (property_id VARCHAR(50) PRIMARY KEY , area TEXT, type TEXT, sqfeet INT, price INT ,address TEXT, room INT ,bathroom INT, living TEXT, status TEXT, floor VARCHAR(50), client_id VARCHAR(50)')
    
    if pid.get()=="" or area.get()=="" or type.get()=="" or sqfeet.get()=="" or price.get()=="" or address.get()=="" or room.get()=="" or broom.get()=="" or ld.get()=="" or status.get()=="" or floor.get()=="" :
            messagebox.showerror("Error!  ","   All fields are required   ") 
    else:
        cursor.execute("SELECT * FROM Property WHERE property_id=?",(pid.get(),))
        row=cursor.fetchone()
        print(row)
        if row!=None:
            messagebox.showerror("Error!","  Property ID already Exists.   ") 
        else:
            cursor.execute('INSERT INTO Property (property_id,area,type,sqfeet,price,address,room,bathroom,living,status,floor) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
                           (pid.get(),area.get(),type.get(),sqfeet.get(),price.get(),address.get(),room.get(),broom.get(),ld.get(),status.get(),floor.get()))  
            conn.commit()
            messagebox.showinfo(title="Property added", message="You have successfully added new property information.")
            clear()

    
#main label   
Label(window,text=" Enter New Property Information 📜",bg='#0a0908', fg="#a9927d", font=("goudy old style", 16, 'bold'),pady=5).pack()

# Create Frame widget
left_frame = Frame(window, width=550, height=530, bd=7, relief=RIDGE,bg='#5e503f')
left_frame.place(x=60,y=50)

right_frame = Frame(window, width=550, height=530, bd=7, relief=RIDGE,bg='#5e503f')
right_frame.place(x=670,y=50)

#label and entry for left
pid_label = tkinter.Label(left_frame, text="Property ID", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
area_label = tkinter.Label(left_frame, text="Area ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
type_label = tkinter.Label(left_frame, text="Type ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
sqfeet_label = tkinter.Label(left_frame, text="Square feet", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
price_label =tkinter.Label(left_frame, text="Price ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
address_label = tkinter.Label(left_frame, text="Address ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))

pid_entry = tkinter.Entry(left_frame,borderwidth=5,width=30, bg='#ede0d4',font=("Arial", 12),textvariable= pid)
area_entry = tkinter.Entry(left_frame, borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=area)
type_entry  = ttk.Combobox(left_frame,width=28, font=("Arial", 12),state='readonly', textvariable = type) 
type_entry ['values'] = ('Apartment','Flat','Duplex Flat','Bungalow','Villa','Standalone house','Duplex House')
sqfeet_entry = tkinter.Entry(left_frame,borderwidth=5,width=15,bg='#ede0d4', font=("Arial", 12),textvariable=sqfeet)
price_entry = tkinter.Entry(left_frame,borderwidth=5,width=15,bg='#ede0d4', font=("Arial", 12),textvariable=price)
address_entry= tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=address) 


pid_label.place(x=30,y=30)
area_label.place(x=30,y=110)
type_label.place(x=30,y=190)
sqfeet_label.place(x=30,y=270)
price_label.place(x=30,y=350)
address_label.place(x=30,y=430)

pid_entry.place(x=160,y=30)
area_entry.place(x=160,y=110)
type_entry.place(x=160,y=190)
sqfeet_entry.place(x=160,y=270)
price_entry.place(x=160,y=350)
address_entry.place(x=160,y=430)

#label and entry for right
room_label=tkinter.Label(right_frame, text="Room ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
bathroom_label=tkinter.Label(right_frame, text="Bathroom ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
living_label=tkinter.Label(right_frame, text="Living & Dining", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
status_label=tkinter.Label(right_frame, text="Status ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
floor_label=tkinter.Label(right_frame, text="Floor plan", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))


room_entry=tkinter.Entry(right_frame,borderwidth=5,width=15,bg='#ede0d4', font=("Arial", 12),textvariable=room)
bathroom_entry=tkinter.Entry(right_frame,borderwidth=5,width=15,bg='#ede0d4', font=("Arial", 12),textvariable=broom)
floor_entry=tkinter.Entry(right_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=floor)
#combobox
living_combo = ttk.Combobox(right_frame,width=28, font=("Arial", 12),state='readonly', textvariable = ld) 
living_combo['values'] = (' Only living or dining','Living and dining attached','Living and dining separated')
status_combo = ttk.Combobox(right_frame, width=28, font=("Arial", 12),state='readonly', textvariable = status) 
status_combo['values'] = (' Available for sell','Under construction','pre constuction')  
 
room_label.place(x=30,y=30)
bathroom_label.place(x=30,y=110)
living_label.place(x=30,y=190)
status_label.place(x=30,y=270)
floor_label.place(x=30,y=350)

room_entry.place(x=170,y=30)
bathroom_entry.place(x=170,y=110)
living_combo.place(x=170,y=190)
status_combo.place(x=170,y=270)
floor_entry.place(x=170,y=350)


#buttons
show_button = Button(window,text="Show Property",relief=GROOVE, bg="#a9927d", fg="#0a0908", borderwidth=3,font=("times new roman", 14,),command= show_property)
show_button.place(x=60,y=600)

add_button = Button(window,text="Add Property",relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,),command= add)
add_button.place(x=580,y=600)

back_button = Button(window, text="Back ↩",relief=GROOVE, bg="#5e503f", fg="#FFFFFF", borderwidth=3,font=("times new roman", 12,),command= back)
back_button.place(x=1160,y=600)


window.mainloop()