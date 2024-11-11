import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import sqlite3
from datetime import date


window=tkinter.Tk()
window.title('Add New transaction | Developed by Era')
window.state('zoomed')
window.config(bg="#0a0908")

trans_id=tkinter.StringVar()
pid=tkinter.StringVar()
nid=tkinter.StringVar() #nid=client_id
fname=tkinter.StringVar()   
lname=tkinter.StringVar()
acc=tkinter.StringVar()
amount=tkinter.StringVar()


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
    trans_id.set("")
    acc.set("")
    amount.set("")
    nid.set("")
    pid.set("")
    print("clear")

  
def add(): #database
    conn = sqlite3.connect('Trans_info.db')
    with conn:
        cursor= conn.cursor()
    #cursor.execute('CREATE TABLE IF NOT EXISTS Trans_detail (date TEXT, trans_id VARCHAR(50), property_id VARCHAR(50),client_id VARCHAR(50) , first_name TEXT, last_name TEXT,amount TEXT,  account_no TEXT ,CONSTRAINT trans_pk PRIMARY KEY (trans_id,client_id,property_id))')
    if fname.get()=="" or lname.get()=="" or trans_id.get()=="" or nid.get()=="" or acc.get()=="" or  pid.get()=="" or amount.get()=="" :
            messagebox.showerror("Error!","   All fields are required   ") 
    else:
        cursor.execute("SELECT * FROM Trans_detail WHERE trans_id=?",(trans_id.get(),))
        row=cursor.fetchone()
        if row!=None:
            messagebox.showerror("Error!","Transaction error ") 
        else:
            day=date.today()
            cursor.execute('INSERT INTO Trans_detail (date , trans_id , property_id ,client_id , first_name , last_name ,amount ,  account_no  ) VALUES(?,?,?, ?,?,?, ?,?)',
                           ( day ,trans_id.get(), pid.get(), nid.get() , fname.get() , lname.get() ,amount.get() , acc.get()))  
            conn.commit()
            messagebox.showinfo(title="Transaction Added", message="You have successfully added the transaction.")
            
            
            #get total_paid amount
            cursor.execute('SELECT SUM(amount) AS "Total" FROM Trans_detail where property_id=? ',(pid.get(),))
            total=cursor.fetchone()
            total_amount= tkinter.IntVar
            total_amount=total[0]
            
            #updating total
            cursor.execute("SELECT * FROM Payment WHERE property_id=?",(pid.get(),))
            row=cursor.fetchone()
            if row!=None: 
                cursor.execute('UPDATE Payment SET total_paid=?, recent_transfer_date=?,recent_transfer_id=? WHERE property_id=? ',(total_amount,day,trans_id.get(),pid.get()))
                conn.commit()
            else:
                stat="Installment ongoing"
                cursor.execute('INSERT INTO Payment(booking_date,property_id,client_id,total_paid,recent_transfer_date, payment_status,recent_transfer_id) VALUES(?,?,?,?, ?,?,?)',(day, pid.get(),nid.get(),total_amount,day,stat,trans_id.get()))  
                conn.commit()
            
            #getting price from property database
            conn2 = sqlite3.connect('Property_info.db')
            with conn2:
                cursor2= conn2.cursor()
                cursor2.execute("SELECT price FROM Property WHERE property_id=?",(pid.get(),))
                price=cursor2.fetchone()
                prop_price=price[0]
                due=prop_price-total_amount
                
                cursor.execute('UPDATE Payment SET price=?, due=? WHERE property_id=? ',(prop_price, due ,pid.get()))
                conn.commit()    
                
                if due==0:
                    status="All installment clear"
                    cursor.execute('UPDATE Payment SET payment_status=? WHERE property_id=? ',(status,pid.get()))
                    conn.commit()
                    stat="Sold"
                    cursor2.execute('UPDATE Property SET status=? WHERE property_id=? ',(stat,pid.get()))
            fetch_payment_info()
            clear()

def fetch_client_info():
    conn = sqlite3.connect('Personal_info.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute("SELECT  property_id,client_id , first_name , last_name, email  ,contact   FROM Client")
        rows=cursor.fetchall()
        if len(rows)!=0:
            clientTable2.delete(*clientTable2.get_children())
            for row in rows:
                clientTable2.insert('',tkinter.END,values=row)
            conn.commit()

def fetch_payment_info():
    conn = sqlite3.connect('Trans_info.db')
    with conn:
        cursor= conn.cursor()
        cursor.execute("SELECT booking_date, property_id, client_id, price, total_paid, due, recent_transfer_date, payment_status, recent_transfer_id FROM Payment")
        rows=cursor.fetchall()
        if len(rows)!=0:
            paymentTable.delete(*paymentTable.get_children())
            for row in rows:
                paymentTable.insert('',tkinter.END,values=row)
            conn.commit()
    
#main label   
Label(window,text=" Enter New Financial Transaction 📜",bg='#0a0908', fg="#a9927d", font=("goudy old style", 16, 'bold'),pady=5).pack()

# Create Frame widget
left_frame = Frame(window, width=570, height=530, bd=7, relief=RIDGE,bg='#5e503f')
left_frame.place(x=50,y=50)

right_frame = Frame(window,  bd=7, relief=RIDGE,bg='#5e503f')
right_frame.place(x=650,y=50,width=580, height=530,)

#label and entry for left
trans_id_label = tkinter.Label(left_frame, text="Transaction no ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
pid_label = tkinter.Label(left_frame, text="Property ID ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
nid_label = tkinter.Label(left_frame, text="Client NID", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
fname_label = tkinter.Label(left_frame, text="First Name", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
lname_label =tkinter.Label(left_frame, text="Last Name", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
acc_label = tkinter.Label(left_frame, text="Account no ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))
amount_label=tkinter.Label(left_frame, text="Amount paid ", bg='#5e503f', fg="#a9927d", font=("times new roman", 13, 'bold'))

trans_id_entry= tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=trans_id) 
pid_entry=tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=pid)
nid_entry=tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=nid)
fname_entry = tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable= fname)
lname_entry = tkinter.Entry(left_frame, borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=lname)
acc_entry = tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=acc)
amount_entry = tkinter.Entry(left_frame,borderwidth=5,width=30,bg='#ede0d4', font=("Arial", 12),textvariable=amount)

trans_id_label.place(x=30,y=30)
pid_label.place(x=30,y=100)
nid_label.place(x=30,y=170)
fname_label.place(x=30,y=240)
lname_label.place(x=30,y=310)
acc_label.place(x=30,y=380)
amount_label.place(x=30,y=450)

trans_id_entry.place(x=160,y=30)
pid_entry.place(x=160,y=100)
nid_entry.place(x=160,y=170)
fname_entry.place(x=160,y=240)
lname_entry.place(x=160,y=310)
acc_entry.place(x=160,y=380)
amount_entry.place(x=160,y=450)


#label and entry for right and view box

#show frame 1 and database client....................
view_frame = Frame(right_frame, bd=7, relief=RIDGE,bg='#5e503f')
view_frame.place(x=15,y=5,width=540,height=255)

scrolly=Scrollbar(view_frame, orient=VERTICAL)
scrollx=Scrollbar(view_frame, orient=HORIZONTAL)

clientTable2=ttk.Treeview(view_frame, columns=('property_id','client_id' , 'first_name' , 'last_name','email'  ,'contact'   ),
                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,padding=2,takefocus=5)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

scrollx.config(command=clientTable2.xview)
scrolly.config(command=clientTable2.yview)

clientTable2.heading("property_id", text="Property ID")
clientTable2.heading("client_id", text="Client ID")
clientTable2.heading("first_name", text="First Name")
clientTable2.heading("last_name", text="Last Name")
clientTable2.heading("email", text="Email")
clientTable2.heading("contact", text="Contact")

clientTable2["show"] = 'headings'

clientTable2.column("property_id", width=100,anchor="center")
clientTable2.column("client_id", width=100,anchor="center")
clientTable2.column("first_name", width=150,anchor="center")
clientTable2.column("last_name", width=150,anchor="center")
clientTable2.column("email", width=150,anchor="center")
clientTable2.column("contact", width=100,anchor="center")

clientTable2.pack(fill=BOTH, expand=True)
fetch_client_info()

#payment table view//////////////
view_frame2 = Frame(right_frame, bd=7, relief=RIDGE,bg='#5e503f')
view_frame2.place(x=15,y=260,width=540,height=255)

scrolly=Scrollbar(view_frame2, orient=VERTICAL)
scrollx=Scrollbar(view_frame2, orient=HORIZONTAL)

paymentTable=ttk.Treeview(view_frame2, columns=('booking_date', 'property_id', 'client_id', 'price', 'total_paid',
                                                'due', 'recent_transfer_date', 'payment_status', 'recent_transfer_id' ),
                      xscrollcommand=scrollx.set, yscrollcommand=scrolly.set,padding=2,takefocus=5)

scrollx.pack(side=BOTTOM, fill=X)
scrolly.pack(side=RIGHT, fill=Y)

scrollx.config(command=paymentTable.xview)
scrolly.config(command=paymentTable.yview)

paymentTable.heading("booking_date", text="Booking Date")
paymentTable.heading("property_id", text="Property ID")
paymentTable.heading("client_id", text="Client ID")
paymentTable.heading("price", text="Selling Price")
paymentTable.heading("total_paid", text="Total Paid")
paymentTable.heading("due", text="Due amount")
paymentTable.heading("recent_transfer_date", text="Last Payment")
paymentTable.heading("payment_status", text="Payment Status")
paymentTable.heading("recent_transfer_id", text="Transfer ID")


paymentTable["show"] = 'headings'

paymentTable.column("booking_date", width=100,anchor="center")
paymentTable.column("property_id", width=100,anchor="center")
paymentTable.column("client_id", width=100,anchor="center")
paymentTable.column("price", width=100,anchor="center")
paymentTable.column("total_paid", width=100,anchor="center")
paymentTable.column("due", width=100,anchor="center")
paymentTable.column("recent_transfer_date", width=100,anchor="center")
paymentTable.column("payment_status", width=150,anchor="center")
paymentTable.column("recent_transfer_id", width=100,anchor="center")

paymentTable.pack(fill=BOTH, expand=True)
fetch_payment_info()

#buttons
show_button = Button(window,text="View Clients",relief=GROOVE, bg="#a9927d", fg="#0a0908", borderwidth=3,font=("times new roman", 14,),command= show_client)
show_button.place(x=50,y=600)

add_button = Button(window,text=" Add Transaction Info ",relief=GROOVE, bg="#49111c", fg="#FFFFFF", borderwidth=3,font=("times new roman", 14,),command= add)
add_button.place(x=550,y=600)

back_button = Button(window, text="Back ↩",relief=GROOVE, bg="#5e503f", fg="#FFFFFF", borderwidth=3,font=("times new roman", 12,),command= back)
back_button.place(x=1160,y=600)


window.mainloop()