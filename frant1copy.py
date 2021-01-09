from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Progressbar
from PIL import Image,ImageTk


win=Tk()
p1=PhotoImage(file='emi.png')
win.iconphoto(False,p1)
lbl1=Label(win,text="EMI LOAN CALCULATOR",font=("Helvetica",30,"bold"))
#lbl1.place(x=50,y=5)
lbl1.pack(pady=5,padx=0)

image=Image.open("emiimage.png")
photo=ImageTk.PhotoImage(image)
lbl=Label(win,image=photo)
lbl.pack(pady=2,padx=0)
def Pg():
    global value
    value +=10
    pgBar['value']=value
    win.update_idletasks()
    if value!=600:
        win.after(600,Pg)

 	

pgBar=Progressbar(win,length=600,orient=HORIZONTAL,value=0,mode='determinate')
pgBar.pack(pady=2)  
value=0
btn=Button(win,text="Press to continue",command=Pg)
btn.pack(pady=5)

win.title("EMI LOAN CALCULATOR")
win.geometry("800x650+300+200")
win.resizable(0,0)
mainloop()