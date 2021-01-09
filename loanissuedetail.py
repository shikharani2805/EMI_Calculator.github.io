from tkinter import *
from tkinter import messagebox
import pymysql
pymysql.install_as_MySQLdb()  
from tkinter.ttk import Combobox
from PIL import Image,ImageTk

def first():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from loanissuemaster limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        issuedate.insert(0, row[1])
        loanduration.insert(0, row[2])
        emi.insert(0, row[3])
        chequenumber.insert(0, row[4])
        issuingbank.insert(0, row[5])
    con.close()

def previous():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from loanissuemaster limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        issuedate.insert(0, row[1])
        loanduration.insert(0, row[2])
        emi.insert(0, row[3])
        chequenumber.insert(0, row[4])
        issuingbank.insert(0, row[5])
    con.close()

def next1():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from loanissuemaster limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        issuedate.insert(0, row[1])
        loanduration.insert(0, row[2])
        emi.insert(0, row[3])
        chequenumber.insert(0, row[4])
        issuingbank.insert(0, row[5])
    con.close()

def last():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from loanissuemaster order by clientid desc limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        issuedate.insert(0, row[1])
        loanduration.insert(0, row[2])
        emi.insert(0, row[3])
        chequenumber.insert(0, row[4])
        issuingbank.insert(0, row[5])
    con.close()


def save():
    lid = clientid.get()
    idate = issuedate.get()
    loandur = loanduration.get()
    e = emi.get()
    chqn = chequenumber.get()
    ibank = issuingbank.get()
    if(lid =="" and e ==""):
        messagebox.showinfo("Insert Status","All * Fields are required")
    else:
        con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
        cursor = con.cursor()
        cursor.execute("insert into loanissuemaster values('"+ lid +"','"+ idate +"','"+ loandur +"','"+ e +"','"+ chqn +"','"+ ibank +"')")
        cursor.execute("commit")

        clientid.delete(0, 'end')
        issuedate.delete(0, 'end')
        loanduration.delete(0, 'end')
        emi.delete(0, 'end')
        chequenumber.delete(0, 'end')
        issuingbank.delete(0, 'end')
        messagebox.showinfo("Insert Status","Insert successfully")
        con.close()

def update():
    lid = clientid.get()
    idate = issuedate.get()
    loandur = loanduration.get()
    e = emi.get()
    chqn = chequenumber.get()
    ibank = issuingbank.get()
    if(lid =="" and e ==""):
        messagebox.showinfo("update Status","All * Fields are required")
    else:
        con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
        cursor = con.cursor()
        cursor.execute("update loanissuemaster set  issuedate ='"+ idate +"',loanduration ='"+ loandur +"',emi ='"+ e +"', chequenumber ='"+ chqn +"',issuingbank ='"+ ibank +"' where clientid='"+ lid +"'")
        #cursor.execute ("update loanissuemaster set username= '%s', password= '%s', securityquestion= '%s', securityanswer= '%s' where userid = '%s'" %(userid,username,password,securityquestion,securityanswer))
        cursor.execute("commit")
        
        clientid.delete(0, 'end')
        issuedate.delete(0, 'end')
        loanduration.delete(0, 'end')
        emi.delete(0, 'end')
        chequenumber.delete(0, 'end')
        issuingbank.delete(0, 'end')
        messagebox.showinfo("Update Status","Update successfully")
        con.close()


window= Tk()
window.title("Loan Issue Detail")
window.configure(bg='#0B446D')
p1=PhotoImage(file='logos.png')
window.iconphoto(False,p1)

p1=PhotoImage(file='logos.png')
window.iconphoto(False,p1)

lbl7=Label(window,text="Loan Issue Detail",fg="white" ,bg='#292F68',font=("arial",30,'bold'),bd=6,relief=GROOVE)

lbl1=Label(window,text="Loan Id",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl2=Label(window,text="Issue Date",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl3=Label(window,text="Loan Duration(Year)",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl4=Label(window,text="EMI",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl5=Label(window,text="Cheque Number",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl6=Label(window,text="Issuing Bank",fg="white",bg='#0B446D',font=('arial',14,'bold'))

clientid=Entry(window,bd=4,width=10,bg='#F0F8FF',font=('arial',14))
issuedate=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
loanduration=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
emi=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
chequenumber=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
issuingbank=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))

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
   


lbl7.place(x=1,y=1,relwidth=1)
        
lbl1.place(x=80,y=120)
clientid.place(x=280,y=120)
        
lbl2.place(x=80,y=180)
issuedate.place(x=280,y=180)
          
lbl3.place(x=80,y=240)
loanduration.place(x=280,y=240)
        
lbl4.place(x=80,y=300)
emi.place(x=280,y=300)

lbl5.place(x=80,y=360)
chequenumber.place(x=280,y=360)

lbl6.place(x=80,y=420)
issuingbank.place(x=280,y=420)
        
first.place(x=100,y=500)
previous.place(x=250,y=500)
next1.place(x=400,y=500)
last.place(x=550,y=500)
add.place(x=100,y=570)
update.place(x=250,y=570)
save.place(x=400,y=570)
cancel.place(x=550,y=570)

image=Image.open("logos.png")
image = image.resize((200, 350), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lbl=Label(window,image=photo,bg='#0B446D')
lbl.place(x=550,y=100)        
       

window.geometry("800x650+200+100")
window.mainloop()