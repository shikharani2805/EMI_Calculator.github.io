#frame page
import sys
import os
from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk
from tkinter import Toplevel, Button, Tk, Menu  
from tkinter import messagebox

def profileaccount():
	os.system('python profileaccountdetail.py')

def profilepersonal():
	os.system('python profilepersonaldetail.py')

def useraccount():
	os.system('python useraccountdetail.py')

def userpersonal():
	os.system('python userpersonaldetail.py')

def clientpersonal():
	os.system('python clientpersonaldetail.py')

def clientprofesional():
	os.system('python clientprofesionaldetail.py')

def clienresponsibility():
	os.system('python clientresponsibilitydetail.py')

def loanplan():
	os.system('python loanplandetail.py')

def loanfile():
	os.system('python loanfiledetail.py')

def loanissue():
	os.system('python loanissuedetail.py')



def profilereport():
	os.system('python profilereport.py')

def useraccountreport():
	os.system('python usermasterreport.py')

def userpersonalreport():
	os.system('python userpersonalreport.py')

def clientpersonalreport():
	os.system('python clientpersonalreport.py')

def clientprofessionalreport():
	os.system('python clientprofessionalreport.py')

def clientresponsibilityreport():
	os.system('python clientresponsibilityreport.py')

def planreport():
	os.system('python planreport.py')

def filereport():
	os.system('python filereport.py')

def issuereport():
	os.system('python issuereport.py')



def exit():  
	MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')  
	if MsgBox == 'yes':  
		window.destroy() 

window=Tk()
window.title("Welcome to EMI Loan Calculator")
p1=PhotoImage(file='login.png')
window.iconphoto(False,p1)

chooser = Menu()
item1 = Menu(tearoff=0)
item1.add_command(label='Profile Account Detail',command = profileaccount)
item1.add_command(label='Profile Personal Detail',command = profilepersonal)
#item1.add_separator()
#item1.add_command(label='Help')
        
item2 = Menu(tearoff=0)
item2.add_command(label='User Account Detail',command = useraccount)
item2.add_command(label='User Personal Detail',command = userpersonal)

item3 = Menu(tearoff=0)
item3.add_command(label='Client Personal Detail',command = clientpersonal)
item3.add_command(label='Client Professional Detail',command = clientprofesional)
item3.add_command(label='Client Responsibility Detail',command = clienresponsibility)

item4 = Menu(tearoff=0)
item4.add_command(label='Loan Plan Detail',command = loanplan)
item4.add_command(label='Loan file detail',command = loanfile)
item4.add_command(label='Loan Issue Detail',command = loanissue)

item5 = Menu(tearoff=0)
item5.add_command(label='Profile Personal Report',command = profilereport)
item5.add_command(label='User Account Report',command = useraccountreport)
item5.add_command(label='User Personal Report',command = userpersonalreport)
item5.add_command(label='Client Personal Report',command = clientpersonalreport)
item5.add_command(label='Client Professional Report',command = clientprofessionalreport)
item5.add_command(label='Client Responsibility Report',command = clientresponsibilityreport)
item5.add_command(label='Loan Plan Report',command = planreport)
item5.add_command(label='Loan file Report',command = filereport)
item5.add_command(label='Loan Issue Report',command = issuereport)
        
chooser.add_cascade(label='User Profile',menu=item1)
chooser.add_cascade(label='User Manager',menu=item2)
chooser.add_cascade(label='Client Manager',menu=item3)
chooser.add_cascade(label='Loan Manager',menu=item4)
chooser.add_cascade(label='Report',menu=item5)
chooser.add_cascade(label='Exit',command=exit)
window.config(menu=chooser)


image=Image.open("frame.png")
image = image.resize((1400, 700), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lbl=Label(window,image=photo)
lbl.pack(pady=2,padx=0)



window.geometry("1400x700+100+50")
window.resizable(0, 0)
mainloop()



