
# Login page
import sys
import os
import pymysql
pymysql.install_as_MySQLdb()
#import MySQLdb
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox 

def login():
    uname = txtuname.get()
    passwd = txtpasswd.get()
    if(uname =="" and passwd==""):
        messagebox.showinfo("Insert Status","All Fields are required")
    else:
        con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
        cursor = con.cursor()
        cursor.execute("select * from profilemaster WHERE username = '" + uname + "' AND password = '" + passwd + "'")
        #cursor.execute("commit")
        rowcount = cursor.rowcount == 1

        print(rowcount)  
        if cursor.rowcount == 1: 
            messagebox.showinfo("login Status","login successfully")
            os.system('python framepage.py')
            txtuname.delete(0, 'end')
            txtpasswd.delete(0, 'end') 
        else :
            txtuname.delete(0, 'end')
            txtpasswd.delete(0, 'end')
            messagebox.showinfo('Information', "Login failed,Invalid Username or Password.Try again!!!")
            
    con.close()

def forget_password():
    os.system('python profileaccountdetail.py')
    

window=Tk()
window.title('LOGIN PAGE')
window.configure(bg='#BDEDFF')
p1=PhotoImage(file='loginlogo3.png')
window.iconphoto(False,p1)
usericon=PhotoImage(file='user_female_blue.png')
passwordicon=PhotoImage(file='blue_key.png')

userlbl=Label(window,text="User Name",image=usericon,compound=LEFT,fg="#151B54",bg='#BDEDFF',font=("arial",16,'bold'))
userlbl.place(x=60,y=120)
passlbl=Label(window,text="Password",image=passwordicon,compound=LEFT,fg="#151B54",bg='#BDEDFF',font=("arial",16,'bold'))
passlbl.place(x=60,y=200)
txtuname=Entry(window,bd=7,width=18,bg = "light gray", fg = "black",font=("arial",16,'bold'))
txtuname.place(x=250,y=120)
txtpasswd=Entry(window,bd=7,width=18,bg = "light gray",show="*",fg = "black",font=("arial",16,'bold')) 
txtpasswd.place(x=250,y=200)

submiticon=PhotoImage(file='user_tick.png')
fpassicon=PhotoImage(file='help.png')
#PhotoImage = submiticon.subsample(3,3)

subbtn=Button(window,compound=LEFT,width=100,image=submiticon,text="SUBMIT",padx=12,bd=8,bg='#157DEC',font=('arial',12,'bold'),command=login)
subbtn.place(x=70,y=300)

forbtn=Button(window,compound=LEFT,width=170,image=fpassicon,text="Forget Password!",padx=12,bd=8,bg='#3BB9FF',font=('arial',12,'bold'),command = forget_password)    
forbtn.place(x=280,y=300)

image=Image.open("login2.png")
image = image.resize((550, 70), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lbl=Label(window,image=photo)
lbl.pack(pady=2,padx=0)

window.geometry("550x400+300+200")
window.mainloop()











