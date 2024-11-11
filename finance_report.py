import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox
from tkinter import *
import os
import sqlite3
from datetime import date


window=tkinter.Tk()
window.title('Genarate property report|  Developed by Era')
window.state('zoomed')
window.config(bg="#0a0908")

pid=tkinter.StringVar()
day=date.today()
 
#go to new transaction page
def new_trans():
    window.destroy()
    os.system("D:/Python/python.exe  new_trans.py")
    
#go to dashboard    
def back():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\dashboard_admin.py")
    
#clear the interface data
def clear():
    pid.set("")
    paymentTable.delete(*paymentTable.get_children())


#view window for transactions
def fetch_payment_info():
    conn = sqlite3.connect('Trans_info.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute("SELECT trans_id, date, amount,account_no FROM Trans_detail where property_id=?",(pid.get(),))
        rows=cursor.fetchall()
        if len(rows)!=0:
            paymentTable.delete(*paymentTable.get_children())
            for row in rows:
                paymentTable.insert('',tkinter.END,values=row)
            conn.commit()   
 #12 coloum
def search():
        conn=sqlite3.connect("Property_info.db")
        cursor=conn.cursor()
        if pid.get()=="" :
            messagebox.showerror("Error!  ","   Please enter the property ID   ") 
        else:
            cursor.execute("SELECT * FROM Property WHERE property_id=? and status='Booked' or status='Sold'",(pid.get(),))
            prop_row=cursor.fetchone()
            
            if prop_row==None:
                messagebox.showerror("Error!","  Property is not  booked or sold yet.   ") 
            else:
                #prop_id=prop_row[0]
                area=prop_row[1]
                type=prop_row[2]
                sqfeet=prop_row[3]
                price=prop_row[4]
                add=prop_row[5]
                room=prop_row[6]
                b_room=prop_row[7]
                living=prop_row[8]
                floor=prop_row[10]
                cid=prop_row[11]
                
                conn2 = sqlite3.connect('Personal_info.db')
                with conn2:
                    cursor2= conn2.cursor()
                    cursor2.execute("SELECT * FROM Client where client_id =?",(cid,))
                    client_row=cursor2.fetchone()
                    #11 row
                    fname=client_row[1]
                    lname=client_row[2]
                    contact=client_row[5]
                    email=client_row[4]
                    
                    
                    conn3 = sqlite3.connect('Trans_info.db')
                    cursor3= conn3.cursor()
                    cursor3.execute("SELECT * FROM Payment WHERE property_id=?",(pid.get(),))
                    pay_row=cursor3.fetchone()
                    #9 row
                    bookingday=pay_row[0]
                    paid=pay_row[4]
                    due=pay_row[5]
                    rec_trans_day=pay_row[6]
                    pay_stat=pay_row[7]
                    rec_trans_id=pay_row[8]
                    
                    fetch_payment_info()
                    
                    #report
                    doc = DocxTemplate("TEMP_report_template.docx")
                    today=day
                    name = fname +" "+lname

                    phone = contact
                    emaill = email
                    client_id = cid
                    propert_id = pid.get()
                    areaa= area
                    address = add
                    typee=type
                    sq_feet=sqfeet
                    pricee=price
                    roomm=room
                    b_rooom=b_room
                    livingg=living
                    floorr=floor
                    booking_day=bookingday
                    paid_amount=paid
                    duee=due
                    pay_status=pay_stat
                    trans_id=rec_trans_id
                    trans_day=rec_trans_day
                    
                    
                    doc.render({"name":name,
                            "phone":phone, 
                            "email":emaill,
                            "client_id": client_id,
                            "property_id":propert_id,
                            "area":areaa,
                            "address": address,
                            "type":typee,
                            "sqfeet":sq_feet ,
                            "room":roomm ,
                            "bathroom":b_rooom,
                            "living":livingg ,
                            "floor":floorr ,
                            "price":pricee ,
                            "booking_date": booking_day,
                            "paid_amount":paid_amount ,
                            "due": duee,
                            "pay_status":pay_status ,
                            "trans_id": trans_id,
                            "trans_day": trans_day,
                            "date": today })
                    
                    doc_name = pid.get()+"_new_report_"  + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
                    
                    result = messagebox.askyesno("Confirmation", "Property Report Genaration Complete \n Do you want to open the document?")
                    if result:
                        doc.save(doc_name)
                        os.system(doc_name)
                    else:
                        doc.save(doc_name)   
                        #moves file
                        destination_file = os.path.join("E:\REMS\property_reports", os.path.basename(doc_name))
                        os.system(f"move {doc_name} {destination_file}")              
                    
                
                
                    
#main label   
Label(window,text=" Genarate Property Report 📜",bg='#0a0908', fg="#a9927d", font=("goudy old style", 16, 'bold'),pady=5).pack()

# Create Frame widget
s_frame = Frame(window, width=1160, height=530, bd=7, relief=RIDGE,bg='#5e503f')
s_frame.place(x=60,y=50)


#label and entry for left
pid_label = tkinter.Label(s_frame, text="Property ID", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
pid_entry = tkinter.Entry(s_frame,borderwidth=5,width=30, bg='#ede0d4',font=("Arial", 12),textvariable= pid)
pid_label.place(x=330,y=30)
pid_entry.place(x=450,y=30)
search_button = Button(s_frame,text=" Search and Genarate 🔍 ",relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,),command= search )
search_button.place(x=750,y=25)

v_frame = Frame(s_frame,  bd=7, relief=RIDGE,bg='#5e503f')
v_frame.place(x=20,y=80,width=1110, height=420,)

scrolly=Scrollbar(v_frame, orient=VERTICAL)
scrollx=Scrollbar(v_frame, orient=HORIZONTAL)

paymentTable=ttk.Treeview(v_frame, columns=('trans_id', 'date', 'amount','account_no' ),
                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,padding=2,takefocus=5)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

scrollx.config(command=paymentTable.xview)
scrolly.config(command=paymentTable.yview)
paymentTable.heading("trans_id", text="Transfer ID")
paymentTable.heading("date", text="Transfer Date")
paymentTable.heading("amount", text="Transfer Amount")
paymentTable.heading("account_no", text="Account No")

paymentTable["show"] = 'headings'

paymentTable.column("trans_id", width=150,anchor="center")
paymentTable.column("date", width=150,anchor="center")
paymentTable.column("amount", width=150,anchor="center")
paymentTable.column("account_no", width=150,anchor="center")

paymentTable.pack(fill=BOTH, expand=True)


#buttons
show_button = Button(window,text="New Transaction",relief=GROOVE, bg="#a9927d", fg="#0a0908", borderwidth=3,font=("times new roman", 14,),command= new_trans)
show_button.place(x=60,y=600)

add_button = Button(window,text="Genarate New Property Report",relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,),command= clear )
add_button.place(x=550,y=600)

back_button = Button(window, text="Home 🏚",relief=GROOVE, bg="#5e503f", fg="#FFFFFF", borderwidth=3,font=("times new roman", 12,),command= back)
back_button.place(x=1150,y=600)


window.mainloop()