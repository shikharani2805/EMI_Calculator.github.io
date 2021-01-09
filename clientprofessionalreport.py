from tkinter import *
from tkinter import messagebox
import pymysql
pymysql.install_as_MySQLdb() 

window=Tk()
window.title('Client Professional Report')
window.configure(bg='#0B446D')
p1=PhotoImage(file='logos.png')
window.iconphoto(False,p1)
#lbl=Label(window,text="Profile Report",fg="white" ,bg='#292F68',font=("arial",30,'bold'),bd=6,relief=GROOVE)

con = pymysql.connect(host ="localhost", user = "root", password = "root", db ="emiloancalculator")
cursor = con.cursor()
cursor.execute("select * from clientprofessional limit 0,20")
rows = cursor.fetchall()
i=0 
for clientprofessional in rows: 
    for j in range(len(clientprofessional)):
        e = Entry(window,width=10,fg="white",bg='#0B446D',font=('arial',14))
        e.grid(row=i, column=j) 
        e.insert(END, clientprofessional[j])
    i=i+1
con.close()

#lbl.place(x=1,y=1,relwidth=1)
window.geometry("800x650+200+100")
window.mainloop()