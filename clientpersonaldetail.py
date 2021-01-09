
from tkinter import *
from tkinter import messagebox
import pymysql
pymysql.install_as_MySQLdb()
from PIL import Image,ImageTk 

def first():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientpersonal limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        username.insert(0, row[1])
        dateofbirth.insert(0, row[2])
        address.insert(0, row[3])
        phone.insert(0, row[4])
        email.insert(0, row[5])
    con.close()
def previous():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientpersonal limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        username.insert(0, row[1])
        dateofbirth.insert(0, row[2])
        address.insert(0, row[3])
        phone.insert(0, row[4])
        email.insert(0, row[5])
    con.close()

def next1():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientpersonal limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        username.insert(0, row[1])
        dateofbirth.insert(0, row[2])
        address.insert(0, row[3])
        phone.insert(0, row[4])
        email.insert(0, row[5])
    con.close()

def last():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientpersonal order by clientid desc limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        username.insert(0, row[1])
        dateofbirth.insert(0, row[2])
        address.insert(0, row[3])
        phone.insert(0, row[4])
        email.insert(0, row[5])
    con.close()

def save():
    cid = clientid.get()
    uname = username.get()
    dob = dateofbirth.get()
    adrs = address.get()
    phon = phone.get()
    em = email.get()
    if(cid =="" and uname =="" and adrs==""):
        messagebox.showinfo("Insert Status","All Fields are required")
    else:
        con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
        cursor = con.cursor()
        cursor.execute("insert into clientpersonal values('"+ cid +"','"+ uname +"','"+ dob +"','"+ adrs +"','"+ phon +"','"+ em +"')")
        cursor.execute("commit")

        clientid.delete(0, 'end')
        username.delete(0, 'end')
        dateofbirth.delete(0, 'end')
        address.delete(0, 'end')
        phone.delete(0, 'end')
        email.delete(0, 'end')
        messagebox.showinfo("Insert Status","Insert successfully")
        con.close()

def update():
    cid = clientid.get()
    uname = username.get()
    dob = dateofbirth.get()
    adrs = address.get()
    phon = phone.get()
    em = email.get()
    if(cid =="" and uname =="" and adrs== ""):
        messagebox.showinfo("update Status","All Fields are required")
    else:
        con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
        cursor = con.cursor()
        cursor.execute("update clientpersonal set  username ='"+ uname +"',dateofbirth ='"+ dob +"', address ='"+ adrs +"', email='"+ em +"' where clientid='"+ cid +"'")
        #cursor.execute ("update clientpersonal set username= '%s', dateofbirth= '%s', address= '%s',phone= '%s', mobile= '%s', email= '%s' where userid = '%s'" %(uid,uname,dob,adrs,phon,mob,em))
        cursor.execute("commit")

        clientid.delete(0, 'end')
        username.delete(0, 'end')
        dateofbirth.delete(0, 'end')
        address.delete(0, 'end')
        phone.delete(0, 'end')
        email.delete(0, 'end')
        messagebox.showinfo("Update Status","Update successfully")
        con.close()




window=Tk()
window.title('Client Personal Detail')
window.configure(bg='#0B446D')
p1=PhotoImage(file='logos.png')
window.iconphoto(False,p1)

lbl=Label(window,text="Client Personal Detail",fg="white" ,bg='#292F68',font=("arial",30,'bold'),bd=6,relief=GROOVE)
lbl1=Label(window,text="Client Id",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl2=Label(window,text="Client Name*",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl3=Label(window,text="Address*",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl4=Label(window,text="Phone",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl5=Label(window,text="Mobile*",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl6=Label(window,text="Pan*",fg="white",bg='#0B446D',font=('arial',14,'bold'))
        
clientid=Entry(window,bd=4,width=10,bg='#F0F8FF',font=('arial',14))
username=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
dateofbirth=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
address=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
phone=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
email=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))

firsticon=PhotoImage(file='button_first.png')
previousicon=PhotoImage(file='buttons_17.png')
next1icon=PhotoImage(file='buttons_12.png')
lasticon=PhotoImage(file='button_last.png')
addicon=PhotoImage(file='buttons_11.png')
updateicon=PhotoImage(file='arrow_clockwise.png')
saveicon=PhotoImage(file='tick.png')
cancelicon=PhotoImage(file='delete.png')        

first=Button(window,compound=LEFT,width=100,image=firsticon,text="First",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=first)
previous=Button(window,compound=LEFT,width=100,image=previousicon,text="Previous",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=previous)
next1=Button(window,compound=LEFT,width=100,image=next1icon,text="Next",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=next1)
last=Button(window,compound=LEFT,width=100,image=lasticon,text="Last",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=last)
add=Button(window,compound=LEFT,width=100,image=addicon,text="Add",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=save)
update=Button(window,compound=LEFT,width=100,image=updateicon,text="Update",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=update)
save=Button(window,compound=LEFT,width=100,image=saveicon,text="Save",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=save)
cancel=Button(window,compound=LEFT,width=100,image=cancelicon,text="Cancel",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=window.quit)

#address = Text(window, height=2, width=30,bd=4)

lbl.place(x=1,y=1,relwidth=1)

lbl1.place(x=80,y=100)
clientid.place(x=250,y=100)
        
lbl2.place(x=80,y=160)
username.place(x=250,y=160)
          
lbl3.place(x=80,y=220)
dateofbirth.place(x=250,y=220)
        
lbl4.place(x=80,y=280)
address.place(x=250,y=280)

lbl5.place(x=80,y=340)
phone.place(x=250,y=340)

lbl6.place(x=80,y=400)
email.place(x=250,y=400)
        
first.place(x=100,y=500)
previous.place(x=250,y=500)
next1.place(x=400,y=500)
last.place(x=550,y=500)
add.place(x=100,y=560)
update.place(x=250,y=560)
save.place(x=400,y=560)
cancel.place(x=550,y=560)

image=Image.open("client1.png")
image = image.resize((200, 250), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lbl=Label(window,image=photo,bg='#0B446D')
lbl.place(x=550,y=160)

window.geometry("800x650+200+100")
window.mainloop()