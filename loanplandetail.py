
from tkinter import *
from tkinter import messagebox
import pymysql
pymysql.install_as_MySQLdb()  
from tkinter.ttk import Combobox
from PIL import Image,ImageTk

def first():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from planmaster limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        planname.insert(0, row[1])
        interestrate.insert(0, row[2])
        description.insert(0, row[3])
    con.close()
def previous():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from planmaster limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        planname.insert(0, row[1])
        interestrate.insert(0, row[2])
        description.insert(0, row[3])
    con.close()

def next1():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from planmaster limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        planname.insert(0, row[1])
        interestrate.insert(0, row[2])
        description.insert(0, row[3])
    con.close()

def last():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from planmaster order by clientid desc limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        planname.insert(0, row[1])
        interestrate.insert(0, row[2])
        description.insert(0, row[3])
    con.close()


def save():
	pid = clientid.get()
	pname = planname.get()
	intr = interestrate.get()
	dec = description.get()
	if(pid =="" and pname ==""):
		messagebox.showinfo("Insert Status","All * Fields are required")
	else:
		con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
		cursor = con.cursor()
		cursor.execute("insert into planmaster values('"+ pid +"','"+ pname +"','"+ intr +"','"+ dec +"')")
		cursor.execute("commit")

		clientid.delete(0, 'end')
		planname.delete(0, 'end')
		interestrate.delete(0, 'end')
		description.delete(0, 'end')
		messagebox.showinfo("Insert Status","Insert successfully")
		con.close()

def update():
	pid = clientid.get()
	pname = planname.get()
	intr = interestrate.get()
	dec = description.get()
	if(pid =="" and pname ==""):
		messagebox.showinfo("update Status","All * Fields are required")
	else:
		con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
		cursor = con.cursor()
		cursor.execute("update planmaster set  planname ='"+ pname +"', interestrate ='"+ intr +"',description ='"+ dec +"' where clientid='"+ pid +"'")
		#cursor.execute ("update planmaster set username= '%s', password= '%s', securityquestion= '%s', securityanswer= '%s' where userid = '%s'" %(userid,username,password,securityquestion,securityanswer))
		cursor.execute("commit")
		
		clientid.delete(0, 'end')
		planname.delete(0, 'end')
		interestrate.delete(0, 'end')
		description.delete(0, 'end')
		messagebox.showinfo("Update Status","Update successfully")
		con.close()

window=Tk()
window.title('Loan Plan Detail')
window.configure(bg='#0B446D')
p1=PhotoImage(file='logos.png')
window.iconphoto(False,p1)
      
lbl=Label(window,text="Loan plan Detail",fg="white" ,bg='#292F68',font=("arial",30,'bold'),bd=6,relief=GROOVE)
lbl1=Label(window,text="Loan Id",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl2=Label(window,text="Loan Name",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl3=Label(window,text="Loan Rate",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl4=Label(window,text="Discription",fg="white",bg='#0B446D',font=('arial',14,'bold'))
 

clientid=Entry(window,bd=4,width=10,bg='#F0F8FF',font=('arial',14))
planname=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
interestrate=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
description=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
#description = Text(window, height=7, width=30,bd=4)

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
   

       
lbl.place(x=1,y=1,relwidth=1)
        
lbl1.place(x=80,y=170)
clientid.place(x=220,y=170)
        
lbl2.place(x=80,y=240)
planname.place(x=220,y=240)
        
lbl3.place(x=80,y=310)
interestrate.place(x=220,y=310)
        
lbl4.place(x=80,y=380)
description.place(x=220,y=380)
              
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
lbl.place(x=530,y=100)        
       
window.geometry("800x650+200+100")
window.mainloop()         
               
        