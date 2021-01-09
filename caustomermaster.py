from tkinter import*
from PIL import ImageTk,Image
class mainwindow:
    def __init__(self,root):


        self.mymenu=Menu(root)

     """self.new_icon=PhotoImage(file='icons2/new.png')
        self.open_icon=PhotoImage(file='icons2/open.png')
        self.save_icon=PhotoImage(file='icons2/save.png')
        self.save_as_icon=PhotoImage(file='icons2/save_as.png')
        self.exit_icon=PhotoImage(file='icons2/exit.png')             """

        self.m1=Menu(self.mymenu,tearoff=0 )
        self.m1.add_command(label='file',image=self.new_icon, compound=LEFT)
        self.m1.add_separator()
        self.m1.add_command(label='exit')
        root.config(menu=self.mymenu)
        self.mymenu.add_cascade(label="User Master",menu=self.m1)

        self.m2 = Menu(self.mymenu, tearoff=0)
        self.m2.add_command(label='file')
        self.m2.add_separator()
        self.m2.add_command(label='exit')
        root.config(menu=self.mymenu)
        self.mymenu.add_cascade(label="Admin Master", menu=self.m2)

        self.m3 = Menu(self.mymenu, tearoff=0)
        self.m3.add_command(label='Add ',command=self.add)
        self.m3.add_separator()
        self.m3.add_command(label='Delete',command=self.delete)
        root.config(menu=self.mymenu)
        self.mymenu.add_cascade(label="Customer Master", menu=self.m3)

        self.m3= Menu(self.mymenu, tearoff=0)
        self.m3.add_command(label='file')
        self.m3.add_separator()
        self.m3.add_command(label='exit')
        root.config(menu=self.mymenu)
        self.mymenu.add_cascade(label="Product Master", menu=self.m3)

        self.m4= Menu(self.mymenu, tearoff=0)
        self.m4.add_command(label='file')
        self.m4.add_separator()
        self.m4.add_command(label='exit')
        root.config(menu=self.mymenu)
        self.mymenu.add_cascade(label="Order Master", menu=self.m4)

        self.m5= Menu(self.mymenu, tearoff=0)
        self.m5.add_command(label='file')
        self.m5.add_separator()
        self.m5.add_command(label='exit')
        root.config(menu=self.mymenu)
        self.mymenu.add_cascade(label="Report",  menu=self.m5)

        self.m6 = Menu(self.mymenu, tearoff=0)
        self.m6.add_command(label='file')
        self.m6.add_separator()
        self.m6.add_command(label='exit')
        root.config(menu=self.mymenu)
        self.mymenu.add_cascade(label="Exit", menu=self.m6)


        #addfunction
    def add(self):
       root1=Tk()
       root1.title("alptacalculater")
       root1.geometry('1000x570')

       f1 = Frame(root1, borderwidth=6)
       f1.pack(fill=BOTH, expand=TRUE)

       f2 = Frame(f1,bg="white", highlightbackground="green",highlightthickness=1)
       f2.pack(padx=20,pady=20,fill=BOTH, expand=TRUE)


       f3 = Frame(f2,bg="white")
       l1=Label(f3,text="Profile Account Detail",font=(NONE, 14),bd=1,relief="solid",padx=12,pady=6)
       l1.pack(pady=5)
       f4=Frame(f3,borderwidth=6)
       l2=Label(f4,text="Enter profile personal details here....!")
       l2.pack(side=TOP,anchor='sw')
       f5=Frame(f4,borderwidth=4,relief=GROOVE)

       l31 = Label(f5, text="user Id")
       l31.grid(row=0, column=0,padx=40,pady=20)
       e1 = Entry(f5,width = 20, font = (NONE, 15))
       e1.grid(row=0, column=1,padx=30)

       l32 = Label(f5, text="Name")
       l32.grid(row=1, column=0,padx=40,pady=20)
       e2 = Entry(f5,width = 20, font = (NONE, 15))
       e2.grid(row=1, column=1,padx=30)

       l33 = Label(f5, text="Address")
       l33.grid(row=2, column=0 ,padx=40,pady=20)
       e3 = Text(f5,height=4,width = 20, font = (NONE, 15))
       e3.grid(row=2, column=1,padx=30)

       l31 = Label(f5, text="Phone No")
       l31.grid(row=3, column=0,padx=40,pady=20)
       e4 = Entry(f5,width = 20, font = (NONE, 15))
       e4.grid(row=3, column=1,padx=30)

       l31 = Label(f5, text="Email")
       l31.grid(row=4, column=0,padx=40,pady=20)
       e1 = Entry(f5,width = 20, font = (NONE, 15))
       e1.grid(row=4, column=1,padx=30)

       f5.pack()
       f4.pack(padx=20,pady=10)
       f6=Frame(f3,borderwidth=4,highlightbackground="skyblue",highlightthickness=2)
       B1=Button(f6,text="Save")
       B1.pack(side=RIGHT,padx=30,pady=4)
       B2 = Button(f6,text="Update")
       B2.pack(side=RIGHT,padx=10,pady=4)
       f6.pack(fill=X,padx=20,pady=10)
       f3.pack(side =LEFT,fill=Y)
       f7=Frame(f2,relief="solid" ,bg="red")
       f7.pack(side=TOP, fill=BOTH,expand=TRUE)
       c1=Canvas(f7,bg="black",height=250,width=200)
       c1.pack()
       img= Image.open("3.jpg")
       c1.image=ImageTk.PhotoImage(img)
       c1.create_image(0,0,image=g5.image)





       root1.mainloop()

    def delete(self):
        root = Tk()
        root.title("alptacalculater")
        root.geometry('500x600')
        root.mainloop()


root=Tk()
main_win=mainwindow(root)
root.title("alptacalculater")
root.state('zoomed')
root.mainloop()
