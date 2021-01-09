from tkinter import *
from tkinter import messagebox
import pymysql
pymysql.install_as_MySQLdb()  
from tkinter.ttk import Combobox
from PIL import Image,ImageTk


def save():
	uid = userid.get()
	uname = username.get()
	passwd = password.get()
	securityq = securityquestion.get()
	securitya = securityanswer.get()
	if(uid =="" and uname =="" and passwd==""):
		messagebox.showinfo("Insert Status","All Fields are required")
	else:
		con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
		cursor = con.cursor()
		cursor.execute("insert into profilemaster values('"+ uid +"','"+ uname +"','"+ passwd +"','"+ securityq +"','"+ securitya +"')")
		cursor.execute("commit")

		userid.delete(0, 'end')
		username.delete(0, 'end')
		password.delete(0, 'end')
		securityquestion.delete(0, 'end')
		securityanswer.delete(0, 'end')
		messagebox.showinfo("Insert Status","Insert successfully")
		con.close()

def update():
	uid = userid.get()
	uname = username.get()
	passwd = password.get()
	securityq = securityquestion.get()
	securitya = securityanswer.get()
	if(uid =="" and uname =="" and passwd== ""):
		messagebox.showinfo("update Status","All Fields are required")
	else:
		con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
		cursor = con.cursor()
		cursor.execute("update profilemaster set  username ='"+ uname +"', password ='"+ passwd +"',securityquestion ='"+ securityq +"', securityanswer ='"+ securitya +"' where userid='"+ uid +"'")
		#cursor.execute ("update profilemaster set username= '%s', password= '%s', securityquestion= '%s', securityanswer= '%s' where userid = '%s'" %(userid,username,password,securityquestion,securityanswer))
		cursor.execute("commit")

		userid.delete(0, 'end')
		username.delete(0, 'end')
		password.delete(0, 'end')
		securityquestion.delete(0, 'end')
		securityanswer.delete(0, 'end')
		messagebox.showinfo("Update Status","Update successfully")
		con.close()


window=Tk()
window.title('Profile Account Detail')
window.configure(bg='#0B446D')
p1=PhotoImage(file='logos.png')
window.iconphoto(False,p1)
lbl=Label(window,text="Profile Account Detail",fg="white" ,bg='#292F68',font=("arial",30,'bold'),bd=6,relief=GROOVE)

lbl1=Label(window,text="User Id",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl2=Label(window,text="User Name*",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl3=Label(window,text="Password*",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl4=Label(window,text="Security Question",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl5=Label(window,text="Security Answer*",fg="white",bg='#0B446D',font=('arial',14,'bold'))
options = ["What is your school name?",  
                          "What is your nick name?", 
                          " What is your fathers name", 
                          "What is your mothers name", 
                          "What is your brothers name"
          ]
 

var=StringVar()
var.set("Select...")

securityquestion=Combobox(window,values=options,textvariable=var,width=19,font=('arial',14))

updateicon=PhotoImage(file='arrow_clockwise.png')
saveicon=PhotoImage(file='tick.png')
Cancelicon=PhotoImage(file='delete.png')


userid=Entry(window,bd=4,width=10,bg='#F0F8FF',font=('arial',14))
username=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
password=Entry(window,show="*",bd=4,bg='#F0F8FF',width=20,font=('arial',14))
securityanswer=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))

update=Button(window,compound=LEFT,width=100,image=updateicon,text="Update",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command =update)
save=Button(window,compound=LEFT,width=100,image=saveicon,text="Save",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),state = DISABLED)
Cancel=Button(window,compound=LEFT,width=100,image=Cancelicon,text="Cancel",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command =window.quit)
        
lbl.place(x=1,y=1,relwidth=1)

lbl1.place(x=80,y=150)
userid.place(x=280,y=150)
        
lbl2.place(x=80,y=220)
username.place(x=280,y=220)
        
lbl3.place(x=80,y=290)
password.place(x=280,y=290)
        
lbl4.place(x=80,y=360)
securityquestion.place(x=280,y=360)
      
lbl5.place(x=80,y=430)
securityanswer.place(x=280,y=430)

update.place(x=150,y=550)
save.place(x=300,y=550)
Cancel.place(x=450,y=550)

image=Image.open("login.png")
image = image.resize((200, 280), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lbl=Label(window,image=photo,bg='#0B446D')
lbl.place(x=560,y=150)

window.geometry("800x650+200+100")
window.mainloop()

