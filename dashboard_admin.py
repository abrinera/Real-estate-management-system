import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from datetime import date

window = Tk()
window.state("zoomed")
window.title("Real Estate Management System | Developed by Era and Murad")
window.config(bg='#ede0d4')


title = Label(window, text="Real Estate Management System 🌃 ",  font=("times new roman", 25, "bold"),relief=RIDGE,border=8,bg="#49111c", fg="white").pack(fill="x",pady=15)


heading = Label(window, text="Properties for sale in Dhaka \t\t\t\t\tWelcome to Hossain Real Estate Limited\t\t\t\t\t © Reserved by BUBT",font=("times new roman", 13), bg="#a9927d", fg="black",relief=RIDGE,border=5)
heading.place(x=0, y=70, relwidth=1, height=30)

def reg_broker():
    window.destroy()
    os.system(" D:/Python/python.exe reg_broker.py")   

def reg_fm():
    window.destroy()
    os.system(" D:/Python/python.exe reg_fm.py") 
    
def logout():
    result = messagebox.askquestion("  Logout  ", "  Do you want to logout?   ")
    if result == "yes":
        window.destroy()

#client dropdown
def add_client():
    window.destroy()
    os.system(" D:/Python/python.exe new_client.py")

def view_client():
    window.destroy()
    os.system(" D:/Python/python.exe  view_client.py")

def update_client(): #need edit
        messagebox.showinfo(title="Information added", message="You have successfully added new property information.")
    
    
#property dropdown
def add_prop():
    window.destroy()
    os.system(" D:/Python/python.exe new_property.py")

def view_all_prop():
    window.destroy()
    os.system(" D:/Python/python.exe all_property.py")

#update property
def update_prop():
    window.destroy()
    os.system(" D:/Python/python.exe update_property.py")

def avail_prop():
    window.destroy()
    os.system(" D:/Python/python.exe  view_avail_property.py")
 
#finance dropdown
def trans():
    window.destroy()
    os.system(" D:/Python/python.exe  new_trans.py")    
def report():
    window.destroy()
    os.system(" D:/Python/python.exe  finance_report.py") 
    

menu_logo = Image.open("Images/building.png")
menu_logo = menu_logo.resize((200, 200), Image.BILINEAR)
menu_logo = ImageTk.PhotoImage(menu_logo)

left_menu = Frame(window, bd=2, relief=RIDGE,border=8, bg="white")
left_menu.place(x=0, y=102, width=350, height=550)

lbl_menu_logo = Label(left_menu, image=menu_logo)
lbl_menu_logo.pack(side=TOP, fill=X)

btn_logout = Button(left_menu, text="  Logout  ", font=("times new roman", 15, "bold"), bg="#49111c", fg='#ffffff',
                    cursor="hand2",relief=RIDGE,border=5, command=logout)
btn_logout.pack(side="bottom")

icon_side = PhotoImage(file="Images/arrow.png")
Label(left_menu, text="Home", font=("times new roman", 20), bg="#5e503f", fg='#ffffff').pack(side=TOP, fill=X,pady=5)
Label(left_menu, text="Register Employee", font=("times new roman", 20), bg="#5e503f", fg='#ffffff').pack(side=TOP, fill=X,pady=5)

Button(left_menu, text="Broker", image=icon_side, compound=LEFT, padx=5, anchor="w",
       font=("times new roman", 18, "bold"), bg="#49111c", fg='#ffffff', bd=3, cursor="hand2",command=reg_broker).pack(side=TOP, fill=X)
Button(left_menu, text="Financial Manager", image=icon_side, compound=LEFT, padx=5, anchor="w",
       font=("times new roman", 18, "bold"), bg="#49111c", fg='#ffffff', bd=3, cursor="hand2",command=reg_fm).pack(side=TOP, fill=X)

#dropdown button font
my_font1=('times new roman',20,'bold')

# Menu buttons for the main dashboard
client_menu_button = Menubutton(window, text="Client", font=("times new roman", 20),cursor="hand2", bg="#49111c", fg='#ffffff', bd=3,relief=RIDGE,border=8)
client_menu = Menu(client_menu_button,bg="#49111c", fg='#ffffff',font=my_font1)
client_menu.add_command(label="Add Client",command=add_client)
#client_menu.add_command(label="Update Client",command=update_client)
client_menu.add_command(label="View All Client",command=view_client)
client_menu_button["menu"] = client_menu
client_menu_button.place(x=450, y=180, height=150, width=350)


property_details_menu_button = Menubutton(window, text="Property Details", font=("times new roman", 20),cursor="hand2", bg="#5e503f",fg='#ffffff', bd=3,relief=RIDGE,border=8)
property_details_menu = Menu(property_details_menu_button,bg="#5e503f", fg='#ffffff',font=my_font1)
property_details_menu.add_command(label="Add New Property",command=add_prop)
property_details_menu.add_command(label="View All Properties", command=view_all_prop)
property_details_menu_button["menu"] = property_details_menu
property_details_menu_button.place(x=850, y=180, height=150, width=350)


property_updates_menu_button = Menubutton(window, text="Update Property", font=("times new roman", 20),cursor="hand2", bg="#5e503f",fg='#ffffff',bd=3,relief=RIDGE,border=8)
property_updates_menu = Menu(property_updates_menu_button,bg="#5e503f", fg='#ffffff',font=my_font1)
property_updates_menu.add_command(label="Update Property",command=update_prop)
property_updates_menu.add_command(label="View Available Property",command=avail_prop)
property_updates_menu_button["menu"] = property_updates_menu
property_updates_menu_button.place(x=450, y=360, height=150, width=350)


transaction_menu_button = Menubutton(window, text="Transaction", font=("times new roman", 20),cursor="hand2", bg="#49111c", fg='#ffffff',bd=3,relief=RIDGE,border=8)
transaction_menu = Menu(transaction_menu_button,bg="#49111c", fg='#ffffff',font=my_font1)
transaction_menu.add_command(label="Financial Transaction",command=trans)
transaction_menu.add_command(label="Financial Report",command=report)
transaction_menu_button["menu"] = transaction_menu
transaction_menu_button.place(x=850, y=360, height=150, width=350)

#date and time
today=date.today()
day=today.strftime("%A, %B %d, %Y  ")
date_label = Label(window, text="📅 "+day, font=("times new roman", 13), bg="#ede0d4", fg="black",relief=RIDGE,border=3)
date_label.place(x=1030,y=625)

window.mainloop()
