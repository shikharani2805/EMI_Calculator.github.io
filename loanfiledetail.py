from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
pymysql.install_as_MySQLdb()  
from tkinter.ttk import Combobox
from PIL import Image,ImageTk



def first():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from loanfilemaster limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        planname.insert(0, row[1])
        clientname.insert(0, row[2])
        loanamount.insert(0, row[3])
        remark.insert(0, row[4])
        status.insert(0, row[5])
        loanamount2.insert(0, row[6])
        interestrate.insert(0, row[7])
        clientmonthlyincome.insert(0, row[8])
        clientmonthlyexpences.insert(0, row[9])
        numberofyear.insert(0, row[10])
    con.close()

def previous():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from loanfilemaster limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        planname.insert(0, row[1])
        clientname.insert(0, row[2])
        loanamount.insert(0, row[3])
        remark.insert(0, row[4])
        status.insert(0, row[5])
        loanamount2.insert(0, row[6])
        interestrate.insert(0, row[7])
        clientmonthlyincome.insert(0, row[8])
        clientmonthlyexpences.insert(0, row[9])
        numberofyear.insert(0, row[10])
    con.close()

def next1():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from loanfilemaster limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        planname.insert(0, row[1])
        clientname.insert(0, row[2])
        loanamount.insert(0, row[3])
        remark.insert(0, row[4])
        status.insert(0, row[5])
        loanamount2.insert(0, row[6])
        interestrate.insert(0, row[7])
        clientmonthlyincome.insert(0, row[8])
        clientmonthlyexpences.insert(0, row[9])
        numberofyear.insert(0, row[10])
    con.close()

def last():
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from loanfilemaster order by clientid desc limit 1")
    rows = cursor.fetchall()
    for row in rows:
        clientid.insert(0, row[0])
        planname.insert(0, row[1])
        clientname.insert(0, row[2])
        loanamount.insert(0, row[3])
        remark.insert(0, row[4])
        status.insert(0, row[5])
        loanamount2.insert(0, row[6])
        interestrate.insert(0, row[7])
        clientmonthlyincome.insert(0, row[8])
        clientmonthlyexpences.insert(0, row[9])
        numberofyear.insert(0, row[10])
    con.close()

def add():
  fid = clientid.get()

  if(fid ==""):
      messagebox.showinfo("Insert Status","All Fields are required")
  else:
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
    cursor = con.cursor()
    cursor.execute("select * from loanfilemaster where clientid='"+ fid +"'")
    rows = cursor.fetchall()
    for row in rows:
      #planname.insert(0, row[1])
      #clientname.insert(0, row[2])
      loanamount.insert(0, row[3])
      remark.insert(0, row[4])
      status.insert(0, row[5])
      loanamount2.insert(0, row[3])
      #interestrate.insert(0, row[7])
      #clientmonthlyincome.insert(0, row[8])
      #clientmonthlyexpences.insert(0, row[9])
      numberofyear.insert(0, row[10]) 

    cursor.execute("select * from planmaster where clientid='"+ fid +"'")
    rows = cursor.fetchall()
    for row in rows:
      planname.insert(0, row[1])
      interestrate.insert(0, row[2])

    cursor.execute("select * from clientpersonal where clientid='"+ fid +"'")
    rows = cursor.fetchall()
    for row in rows:
      clientname.insert(0, row[1])
    
    cursor.execute("select * from clientresponsibility where clientid='"+ fid +"'")
    rows = cursor.fetchall()
    for row in rows:
      clientmonthlyexpences.insert(0, row[7])
    
    cursor.execute("select * from clientprofessional where clientid='"+ fid +"'")
    rows = cursor.fetchall()
    for row in rows:
      clientmonthlyincome.insert(0, row[5])
    con.close()

def save():
  fid = clientid.get()
  pl = planname.get()
  cl = clientname.get()
  lamount = loanamount.get()
  rem = remark.get()
  sta = status.get()
  lamount2 = loanamount2.get()
  roi = interestrate.get()
  cmi = clientmonthlyincome.get()
  cme = clientmonthlyexpences.get()
  noy = numberofyear.get()
  if(fid ==""):
    messagebox.showinfo("Insert Status","All Fields are required")
  else:
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
    cursor = con.cursor()
    cursor.execute("insert into loanfilemaster values('"+ fid +"','"+ pl +"','"+ cl +"','"+ lamount +"','"+ rem +"','"+ sta +"','"+ lamount2 +"','"+ roi +"','"+ cmi +"','"+ cme +"','"+ noy +"')")
    cursor.execute("commit")
    clientid.delete(0, 'end')
    planname.delete(0, 'end')
    clientname.delete(0, 'end')
    loanamount.delete(0, 'end')
    remark.delete(0, 'end')
    status.delete(0, 'end')
    loanamount2.delete(0, 'end')
    interestrate.delete(0, 'end')
    clientmonthlyincome.delete(0, 'end')
    numberofyear.delete(0, 'end')
    messagebox.showinfo("Insert Status","Insert successfully")
    con.close()

def update():
  fid = clientid.get()
  pl = planname.get()
  cl = clientname.get()
  lamount = loanamount.get()
  rem = remark.get()
  sta = status.get()
  lamount2 = loanamount2.get()
  roi = interestrate.get()
  cmi = clientmonthlyincome.get()
  cme = clientmonthlyexpences.get()
  noy = numberofyear.get()
  if(fid ==""):
    messagebox.showinfo("update Status","All Fields are required")
  else:
    con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator") 
    cursor = con.cursor()
    cursor.execute("update loanfilemaster set  loanamount ='"+ lamount +"',remark ='"+ rem +"',status ='"+ sta +"',numberofyear ='"+ noy +"' where clientid ='"+ fid +"'")
    #cursor.execute ("update loanfilemaster set username= '%s', password= '%s', securityquestion= '%s', securityanswer= '%s' where userid = '%s'" %(userid,username,password,securityquestion,securityanswer))
    cursor.execute("commit")


    clientid.delete(0, 'end')
    planname.delete(0, 'end')
    clientname.delete(0, 'end')
    loanamount.delete(0, 'end')
    remark.delete(0, 'end')
    status.delete(0, 'end')
    loanamount2.delete(0, 'end')
    interestrate.delete(0, 'end')
    clientmonthlyincome.delete(0, 'end')
    numberofyear.delete(0, 'end')
    messagebox.showinfo("Update Status","Update successfully")
    con.close()

def evaluate():
  noy = numberofyear.get()
  sta = status.get()

  r=float(interestVar.get())/1200
  n=int(yearVar.get())
  p=float(amountVar.get())
  for i in range(1,n+1):
    n=i
    monthly=float(p*r*(1+r)**(i*12))/(((1+r)**(i*12))-1)
    tb1.insert('','end',value=i)
    tb2.insert('','end',value=monthly)
    #tb2.set(format(monthly,"10.2f"))
    tb3.insert('','end',value=sta)

def cancel():
  clientid.delete(0, 'end')
  planname.delete(0, 'end')
  clientname.delete(0, 'end')
  loanamount.delete(0, 'end')
  remark.delete(0, 'end')
  status.delete(0, 'end')
  loanamount2.delete(0, 'end')
  interestrate.delete(0, 'end')
  clientmonthlyincome.delete(0, 'end')
  clientmonthlyexpences.delete(0, 'end')
  numberofyear.delete(0, 'end')


window=Tk()
window.title('Loan File Detail & Evaluation')
window.configure(bg='#0B446D')
p1=PhotoImage(file='logos.png')
window.iconphoto(False,p1)


lb1=Label(window,text="",height=27,width=70,bg='#0B446D')
lb2=Label(window,text="",height=5,width=70,bg='#0B446D')
lb9=Label(window,text="Loan File Detail",fg="white" ,bg='#292F68',font=("arial",30,'bold'),bd=6,relief=GROOVE)
lbl0=Label(window,text="Loan Evaluation",fg="white" ,bg='#292F68',font=("arial",30,'bold'),bd=6,relief=GROOVE)
lbl1=Label(window,text="File Id",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl2=Label(window,text="plan Name",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl3=Label(window,text="Client",fg="white",bg='#0B446D',font=('arial',12,'bold'))

lbl4=Label(window,text="Loan Amount",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl5=Label(window,text="ID Proof",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl6=Label(window,text="Income Proof",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl7=Label(window,text="Residence Proof",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl8=Label(window,text="Bank Statement",fg="white",bg='#0B446D',font=('arial',12,'bold'))

lbl9=Label(window,text="Remarks",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl10=Label(window,text="Status",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl11=Label(window,text="Loan Amount",fg="white",bg='#0B446D',font=('arial',12,'bold'))

lbl12=Label(window,text="Rate of Interest",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl13=Label(window,text="Client M. Income",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl14=Label(window,text="Client M. Expences",fg="white",bg='#0B446D',font=('arial',12,'bold'))
lbl15=Label(window,text="Number of Years",fg="white",bg='#0B446D',font=('arial',12,'bold'))

#lbl20=Label(text="Monthly Payable Amount(EMI):",bg="black",fg="white")
#lbl21=Label(text="total Amount:",bg="black",fg="white")


var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()

idproof = Checkbutton(window,variable=var1,text="    ",bg='#0B446D')
incomeproof = Checkbutton(window,variable=var2,text="    ",bg='#0B446D')
residenceproof = Checkbutton(window,variable=var3,text="    ",bg='#0B446D')
bankstatement = Checkbutton(window,variable=var4,text="    ",bg='#0B446D')



clientid=Entry(window,bd=4,width=10,bg='#F0F8FF',font=('arial',14)) 
planname=Entry(window,width=25,bg='#0B446D',font=('arial',14)) 
clientname=Entry(window,width=25,bg='#0B446D',font=('arial',14)) 
loanamount=Entry(window,bd=4,width=25,bg='#F0F8FF',font=('arial',14))
remark =Entry(window,width=25,bd=4,bg='#F0F8FF',font=('arial',14))
status=Entry(window,bd=4,width=25,bg='#F0F8FF',font=('arial',14))
amountVar=StringVar()
loanamount2=Entry(window,textvariable=amountVar,width=10,bg='#0B446D',font=('arial',14))
interestVar=StringVar()
interestrate=Entry(window,textvariable=interestVar,width=12,bg='#0B446D',font=('arial',14))
clientmonthlyincome=Entry(window,width=10,bg='#0B446D',font=('arial',14))
clientmonthlyexpencesVar=StringVar()
clientmonthlyexpences=Entry(window,textvariable=clientmonthlyexpencesVar,width=12,bg='#0B446D',font=('arial',14))
yearVar=StringVar()
numberofyear=Entry(window,textvariable=yearVar,bd=4,width=10,bg='#F0F8FF',font=('arial',14))



firsticon=PhotoImage(file='button_first.png')
previousicon=PhotoImage(file='buttons_17.png')
next1icon=PhotoImage(file='buttons_12.png')
lasticon=PhotoImage(file='button_last.png')
addicon=PhotoImage(file='buttons_11.png')
updateicon=PhotoImage(file='arrow_clockwise.png')
saveicon=PhotoImage(file='tick.png')
cancelicon=PhotoImage(file='delete.png') 
Evaluateicon=PhotoImage(file='calc.png')
save2icon=PhotoImage(file='folder.png')
        
first=Button(window,compound=LEFT,width=100,image=firsticon,text="First",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=first)
previous=Button(window,compound=LEFT,width=100,image=previousicon,text="Previous",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=previous)
next1=Button(window,compound=LEFT,width=100,image=next1icon,text="Next",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=next1)
last=Button(window,compound=LEFT,width=100,image=lasticon,text="Last",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=last)
add=Button(window,compound=LEFT,width=100,image=addicon,text="Display",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=add)
update=Button(window,compound=LEFT,width=100,image=updateicon,text="Update",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=update)
save1=Button(window,compound=LEFT,width=100,image=saveicon,text="Save",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=save)
cancel=Button(window,compound=LEFT,width=100,image=cancelicon,text="Clear",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=cancel)

Evaluate=Button(window,compound=LEFT,width=100,image=Evaluateicon,text="Evaluate",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),command=evaluate)
save2=Button(window,compound=LEFT,width=100,image=save2icon,text="ISSUE",padx=12,fg="white",bg='#736FAF',font=('arial',10,'bold'),state = DISABLED)


lb1.place(x=1,y=1,relwidth=2) 
lb2.place(x=1,y=1,relwidth=1)
lb9.place(x=150,y=10)
lbl0.place(x=800,y=10)


lbl1.place(x=70,y=100)
clientid.place(x=250,y=100)
      
lbl2.place(x=70,y=140)
planname.place(x=250,y=140)
        
lbl3.place(x=70,y=180)
clientname.place(x=250,y=180)
        
lbl4.place(x=70,y=220)
loanamount.place(x=250,y=220)
        
lbl5.place(x=70,y=260)
idproof.place(x=250,y=260)

lbl6.place(x=70,y=300)
incomeproof.place(x=250,y=300)

lbl7.place(x=70,y=340)
residenceproof.place(x=250,y=340)

lbl8.place(x=70,y=380)
bankstatement.place(x=250,y=380)

lbl9.place(x=70,y=420)
remark.place(x=250,y=420)

lbl10.place(x=70,y=460)
status.place(x=250,y=460)

lbl11.place(x=610,y=100)
loanamount2.place(x=770,y=100)

lbl12.place(x=940,y=100)
interestrate.place(x=1110,y=100)

lbl13.place(x=610,y=150)
clientmonthlyincome.place(x=770,y=150)

lbl14.place(x=945,y=150)
clientmonthlyexpences.place(x=1112,y=150)

lbl15.place(x=610,y=200)
numberofyear.place(x=770,y=200)


#lbl20.place(x=945,y=300)
#monthly.place(x=1112,y=300)

#lbl21.place(x=610,y=400)
#monthly.place(x=770,y=400)


first.place(x=50,y=510)
previous.place(x=200,y=510)
next1.place(x=350,y=510)
last.place(x=500,y=510)
add.place(x=50,y=570)
update.place(x=200,y=570)
save1.place(x=350,y=570)
cancel.place(x=500,y=570)
Evaluate.place(x=950,y=200)
save2.place(x=1115,y=200)

frm1 = Frame(window)
frm1.place(x=660,y=270)
tb1=ttk.Treeview(frm1, column=(1), show="headings",height=6)
tb1.pack()
tb1.heading(1, text="Number Of Years")

frm2 = Frame(window)
frm2.place(x=860,y=270)
tb2=ttk.Treeview(frm2, column=(1), show="headings",height=6)
tb2.pack()
tb2.heading(1, text="Monthly Installment")

frm3 = Frame(window)
frm3.place(x=1060,y=270)
tb3=ttk.Treeview(frm3, column=(1), show="headings",height=6)
tb3.pack()
tb3.heading(1, text="Issue Status?")




"""tb.heading(2, text="Monthly Installment")
tb.heading(3, text="Issue Status?")
for i in range(3):
    tb.insert('','end',value=i)"""

image=Image.open("logos.png")
image = image.resize((150, 80), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lbl=Label(window,image=photo,bg='#0B446D')
lbl.place(x=490,y=5)

window.geometry("1300x630+200+100")
window.mainloop()