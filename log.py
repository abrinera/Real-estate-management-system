import tkinter
from tkinter import *
import os

window=tkinter.Tk()
window.title("Login form | Era")
window.geometry('550x540')
window.state('zoomed')
window.config(bg="#0a0908")#background

def ad():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\login_admin.py ")
 
def br():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\login_broker.py ")

def fm():
    window.destroy()
    os.system(" D:/Python/python.exe E:\REMS\login_finance.py ")        
    
#main login window
Label(window,text="Login as",bg="#0a0908", fg="#a9927d", width="300", height="3", font=("times new roman",25,"bold"),pady=10).pack()

Button(window,text="Admin",bg="#333333" ,fg="white",height="4", width="40",borderwidth=3, font=("times new roman",15,"bold"),command=ad).pack()
Label(text="",bg="#0a0908").pack()
Button(window,text="Broker",bg="#333333",fg="white", height="4", width="40", borderwidth=3,font=("times new roman",15,"bold"),command=br).pack()
Label(text="",bg="#0a0908").pack()
Button(window,text="Finance Manager",bg="#333333",fg="white", height="4", width="40",borderwidth=3, font=("times new roman",15,"bold"),command=fm).pack()

window.mainloop()

