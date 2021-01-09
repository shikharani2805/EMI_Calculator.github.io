
from tkinter import *
from tkinter import messagebox
import pymysql
pymysql.install_as_MySQLdb()
#import MySQLdb
from PIL import Image,ImageTk 


def first():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientprofessional limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        profession.insert(0, row[1])
        designation.insert(0, row[2])
        officephone.insert(0, row[3])
        officeaddress.insert(0, row[4])
        clientmonthlyincome.insert(0, row[5])
        otherincome.insert(0, row[6])
    con.close()
def previous():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientprofessional limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        profession.insert(0, row[1])
        designation.insert(0, row[2])
        officephone.insert(0, row[3])
        officeaddress.insert(0, row[4])
        clientmonthlyincome.insert(0, row[5])
        otherincome.insert(0, row[6])

def next1():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientprofessional order by clientid desc limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        profession.insert(0, row[1])
        designation.insert(0, row[2])
        officephone.insert(0, row[3])
        officeaddress.insert(0, row[4])
        clientmonthlyincome.insert(0, row[5])
        otherincome.insert(0, row[6])

def last():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from clientprofessional order by clientid desc limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        profession.insert(0, row[1])
        designation.insert(0, row[2])
        officephone.insert(0, row[3])
        officeaddress.insert(0, row[4])
        clientmonthlyincome.insert(0, row[5])
        otherincome.insert(0, row[6])

def save():
    cid = clientid.get()
    prof = profession.get()
    design = designation.get()
    office = officephone.get()
    officead = officeaddress.get()
    annual = clientmonthlyincome.get()
    other = otherincome.get()
    if(cid ==""):
        messagebox.showinfo("Insert Status","All Fields are required")
    else:
        con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
        cursor = con.cursor()
        cursor.execute("insert into clientprofessional values('"+ cid +"','"+ prof +"','"+ design +"','"+ office +"','"+ officead +"','"+ annual +"','"+ other +"')")
        cursor.execute("commit")

        clientid.delete(0, 'end')
        profession.delete(0, 'end')
        designation.delete(0, 'end')
        officephone.delete(0, 'end')
        officeaddress.delete(0, 'end')
        clientmonthlyincome.delete(0, 'end')
        otherincome.delete(0, 'end')
        messagebox.showinfo("Insert Status","Insert successfully")
        con.close()

def update():
    cid = clientid.get()
    prof = profession.get()
    design = designation.get()
    office = officephone.get()
    officead = officeaddress.get()
    annual = clientmonthlyincome.get()
    other = otherincome.get()
    if(cid ==""):
        messagebox.showinfo("update Status","All Fields are required")
    else:
        con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
        cursor = con.cursor()
        cursor.execute("update clientprofessional set  profession= '"+ prof +"',designation= '"+ design +"', officephone= '"+ office +"',officeaddress= '"+ officead +"', clientmonthlyincome= '"+ annual +"', otherincome= '"+ other +"' where clientid='"+ cid +"'")
        #cursor.execute ("update clientprofessional set profession= '%s', designation= '%s', officephone= '%s',clientmonthlyincome= '%s', otherincome= '%s' where userid = '%s'" %(uid,uname,dob,adrs,phon,mob,em))
        cursor.execute("commit")

        clientid.delete(0, 'end')
        profession.delete(0, 'end')
        designation.delete(0, 'end')
        officephone.delete(0, 'end')
        officeaddress.delete(0, 'end')
        clientmonthlyincome.delete(0, 'end')
        otherincome.delete(0, 'end')
        messagebox.showinfo("Update Status","Update successfully")
        con.close()




window= Tk()
window.title('Client Professional Detail')
window.configure(bg='#0B446D')
p1=PhotoImage(file='logos.png')
window.iconphoto(False,p1)
      
lbl=Label(window,text="Client Professional Detail",fg="white" ,bg='#292F68',font=("arial",30,'bold'),bd=6,relief=GROOVE)
lbl1=Label(window,text="Client Id",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl2=Label(window,text="Profession",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl3=Label(window,text="Designation",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl4=Label(window,text="Office Phone",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl5=Label(window,text="Office Address",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl6=Label(window,text="Monthly Income",fg="white",bg='#0B446D',font=('arial',14,'bold'))
lbl7=Label(window,text="Other Income",fg="white",bg='#0B446D',font=('arial',14,'bold'))
        
clientid=Entry(window,bd=4,width=10,bg='#F0F8FF',font=('arial',14))
profession=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
designation=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
officephone=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
officeaddress=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
clientmonthlyincome=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
otherincome=Entry(window,bd=4,width=20,bg='#F0F8FF',font=('arial',14))
               
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
        
lbl1.place(x=80,y=120)
clientid.place(x=250,y=120)
        
lbl2.place(x=80,y=170)
profession.place(x=250,y=170)
          
lbl3.place(x=80,y=220)
designation.place(x=250,y=220)
        
lbl4.place(x=80,y=270)
officephone.place(x=250,y=270)

lbl5.place(x=80,y=320)
officeaddress.place(x=250,y=320)

lbl6.place(x=80,y=370)
clientmonthlyincome.place(x=250,y=370)

lbl7.place(x=80,y=420)
otherincome.place(x=250,y=420)


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


