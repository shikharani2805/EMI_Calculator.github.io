from tkinter import *
from tkinter import messagebox
import pymysql
pymysql.install_as_MySQLdb()
from PIL import Image,ImageTk 


def first():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientresponsibility limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        textdeduction.insert(0, row[1])
        loanemi.insert(0, row[2])
        insuranceemi.insert(0, row[3])
        houserent.insert(0, row[4])
        personalexpenditure.insert(0, row[5])
        healthexpenditure.insert(0, row[6])
        monthlyexpenses.insert(0, row[7])
    con.close()
def previous():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientresponsibility limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        textdeduction.insert(0, row[1])
        loanemi.insert(0, row[2])
        insuranceemi.insert(0, row[3])
        houserent.insert(0, row[4])
        personalexpenditure.insert(0, row[5])
        healthexpenditure.insert(0, row[6])
        monthlyexpenses.insert(0, row[7])
    con.close()

def next1():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientresponsibility order by clientid desc limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        textdeduction.insert(0, row[1])
        loanemi.insert(0, row[2])
        insuranceemi.insert(0, row[3])
        houserent.insert(0, row[4])
        personalexpenditure.insert(0, row[5])
        healthexpenditure.insert(0, row[6])
        monthlyexpenses.insert(0, row[7])
    con.close()

def last():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientresponsibility order by clientid desc limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        textdeduction.insert(0, row[1])
        loanemi.insert(0, row[2])
        insuranceemi.insert(0, row[3])
        houserent.insert(0, row[4])
        personalexpenditure.insert(0, row[5])
        healthexpenditure.insert(0, row[6])
        monthlyexpenses.insert(0, row[7])
    con.close()

def add():
	cid = clientid.get()
	txt = textdeduction.get()
	lemi = loanemi.get()
	inemi = insuranceemi.get()
	hrent = houserent.get()
	personalexp = personalexpenditure.get()
	healthexp = healthexpenditure.get()
	dep = monthlyexpenses.get()
   
	p=float(personalexpenditureVar.get())
	h=float(healthexpenditureVar.get())
	cme=(p+h)
	monthlyvar.set(format(cme,"10.2f"))

def save():
    cid = clientid.get()
    txt = textdeduction.get()
    lemi = loanemi.get()
    inemi = insuranceemi.get()
    hrent = houserent.get()
    personalexp = personalexpenditure.get()
    healthexp = healthexpenditure.get()
    dep = monthlyexpenses.get()
    if(cid ==""):
        messagebox.showinfo("Insert Status","All Fields are required")
    else:
        con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
        cursor = con.cursor()
        cursor.execute("insert into clientresponsibility values('"+ cid +"','"+ txt +"','"+ lemi +"','"+ inemi +"','"+ hrent +"','"+ personalexp +"','"+ healthexp +"','"+ dep +"')")
        cursor.execute("commit")

        clientid.delete(0, 'end')
        textdeduction.delete(0, 'end')
        loanemi.delete(0, 'end')
        insuranceemi.delete(0, 'end')
        houserent.delete(0, 'end')
        monthlyexpenses.delete(0, 'end')
        personalexpenditure.delete(0, 'end')
        healthexpenditure.delete(0, 'end')
        messagebox.showinfo("Insert Status","Insert successfully")
        con.close()

def update():
    cid = clientid.get()
    txt = textdeduction.get()
    lemi = loanemi.get()
    inemi = insuranceemi.get()
    hrent = houserent.get()
    personalexp = personalexpenditure.get()
    healthexp = healthexpenditure.get()
    dep = monthlyexpenses.get()
    if(cid ==""):
        messagebox.showinfo("update Status","All Fields are required")
    else:
        con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
        cursor = con.cursor()
        cursor.execute("update clientresponsibility set  textdeduction= '"+ txt +"',loanemi= '"+ lemi +"',insuranceemi= '"+ inemi +"', houserent= '"+ hrent +"', personalexpenditure= '"+ personalexp +"', healthexpenditure= '"+ healthexp +"',monthlyexpenses= '"+ dep +"' where clientid='"+ cid +"'")
        #cursor.execute ("update clientresponsibility set profession= '%s', designation= '%s', officephone= '%s',annualincome= '%s', otherincome= '%s' where userid = '%s'" %(uid,uname,dob,adrs,phon,mob,em))
        cursor.execute("commit")

        clientid.delete(0, 'end')
        textdeduction.delete(0, 'end')
        loanemi.delete(0, 'end')
        insuranceemi.delete(0, 'end')
        houserent.delete(0, 'end')
        monthlyexpenses.delete(0, 'end')
        personalexpenditure.delete(0, 'end')
        healthexpenditure.delete(0, 'end')
        messagebox.showinfo("Update Status","Update successfully")
        con.close()


window=Tk()
window.title('Client Responsibility Detail')
window.configure(bg='#0B446D')
p1=PhotoImage(file='logos.png')
window.iconphoto(False,p1)
lbl=Label(window,text="Client Responsibility Detail",fg="white" ,bg='#292F68',font=("arial",30,'bold'),bd=6,relief=GROOVE)

lbl1=Label(window,text="Client Id",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl2=Label(window,text="Tax Deduction",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl3=Label(window,text="Loan EMI",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl4=Label(window,text="Insurance EMI",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl5=Label(window,text="House Rent",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl6=Label(window,text="Personal Expenditure",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl7=Label(window,text="Health Expenditure",fg="white",bg='#0B446D',font=('arial',14,'bold'))      
lbl8=Label(window,text="Monthly Expenses",fg="white",bg='#0B446D',font=('arial',14,'bold'))
       
clientid=Entry(window,bd=4,width=10,bg='#F0F8FF',font=('arial',14))
textdeduction=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
loanemi=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
insuranceemi=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
houserent=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
personalexpenditureVar=StringVar()
personalexpenditure=Entry(window,textvariable=personalexpenditureVar,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
healthexpenditureVar=StringVar()
healthexpenditure=Entry(window,textvariable=healthexpenditureVar,bd=4,width=20,bg='#F0F8FF',font=('arial',14))       
monthlyvar=StringVar()
monthlyexpenses=Entry(window,textvariable=monthlyvar,width=20,bg='#0B446D',font=('arial',14))

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
add=Button(window,compound=LEFT,width=100,image=addicon,text="Add",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=add)
update=Button(window,compound=LEFT,width=100,image=updateicon,text="Update",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=update)
save=Button(window,compound=LEFT,width=100,image=saveicon,text="Save",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=save)
cancel=Button(window,compound=LEFT,width=100,image=cancelicon,text="Cancel",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=window.quit)
     
lbl.place(x=1,y=1,relwidth=1)
        
lbl1.place(x=70,y=100)
clientid.place(x=300,y=100)
        
lbl2.place(x=70,y=150)
textdeduction.place(x=300,y=150)

lbl3.place(x=70,y=200)
loanemi.place(x=300,y=200)
        
lbl4.place(x=70,y=250)
insuranceemi.place(x=300,y=250)
        
lbl5.place(x=70,y=300)
houserent.place(x=300,y=300)
        
lbl6.place(x=70,y=350)
personalexpenditure.place(x=300,y=350)

lbl7.place(x=70,y=400)
healthexpenditure.place(x=300,y=400)

lbl8.place(x=70,y=450)
monthlyexpenses.place(x=300,y=450)

first.place(x=100,y=520)
previous.place(x=250,y=520)
next1.place(x=400,y=520)
last.place(x=550,y=520)
add.place(x=100,y=580)
update.place(x=250,y=580)
save.place(x=400,y=580)
cancel.place(x=550,y=580)
         
image=Image.open("client1.png")
image = image.resize((200, 230), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lbl=Label(window,image=photo,bg='#0B446D')
lbl.place(x=600,y=170) 

window.geometry("800x650+200+100")
window.mainloop()




