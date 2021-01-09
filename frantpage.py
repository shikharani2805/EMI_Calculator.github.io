#frant page
import sys
import os
from tkinter import *
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk

window=Tk()
window.title("EMI LOAN CALCULATOR")
window.configure(bg='#BDEDFF')

p1=PhotoImage(file='home.png')
window.iconphoto(False,p1)
lbl1=Label(window,text="EMI LOAN CALCULATOR",fg="#000080",bg= "#BDEDFF",font=("Helvetica",30,"bold"))
#lbl1.place(x=50,y=5)
lbl1.pack(pady=5,padx=0)

image=Image.open("emiimage.png")
image = image.resize((1000, 500), Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
lbl=Label(window,image=photo)
lbl.pack(pady=2,padx=0)

def Pg():
	global value
	value +=100
	pgBar['value']=value
	window.update_idletasks()
	if value!=600:
		window.after(600,Pg)
		window.destroy()
	os.system('python loginpage.py')
	

pgBar=Progressbar(window,length=600,orient=HORIZONTAL,value=0,mode='determinate')
pgBar.pack(pady=2)  
value=0
btn=Button(window,text="Press to continue",padx=16,bd=8,fg='black',bg='#157DEC',font=('arial',14,'bold'),command = Pg)
btn.pack(pady=5)


window.geometry("1000x650+200+100")
window.resizable(0,0)
mainloop()



