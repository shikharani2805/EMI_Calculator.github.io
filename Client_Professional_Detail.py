#!/usr/bin/env python
# coding: utf-8

# In[ ]:


win=Tk()


win.title('Client Professional Detail')

      
lbl=Label(win,text="Client Professional Detail",bg="lightgrey" ,font=("arial",25))
lbl1=Label(win,text="Client Id")
lbl2=Label(win,text="Profession")
lbl3=Label(win,text="Designation")
lbl4=Label(win,text="Office Phone")
lbl5=Label(win,text="Office Address")
lbl6=Label(win,text="Annual Income")
lbl7=Label(win,text="Other Income")
        

        
t1=Entry(win,bd=4,width=15)
t2=Entry(win,bd=4,width=40)
t3=Entry(win,bd=4,width=40)
t4=Entry(win,bd=4,width=40)
t5=Entry(win,bd=4,width=40)
t6=Entry(win,bd=4,width=40)
t7=Entry(win,bd=4,width=40)
        
        
btn1=Button(win,text="First",width=10,bg='Lightblue',font=('arial',10,'bold'))
btn2=Button(win,text="Previous",width=10,bg='Lightblue',font=('arial',10,'bold'))
btn3=Button(win,text="Next",width=10,bg='Lightblue',font=('arial',10,'bold'))
        
btn4=Button(win,text="Last",width=10,bg='Lightblue',font=('arial',10,'bold'))
btn5=Button(win,text="Add",width=10,bg='Lightblue',font=('arial',10,'bold'))
btn6=Button(win,text="Update",width=10,bg='Lightblue',font=('arial',10,'bold'))
btn7=Button(win,text="Save",width=10,bg='Lightblue',font=('arial',10,'bold'))
btn8=Button(win,text="Cancel",width=10,bg='Lightblue',font=('arial',10,'bold'))

        
lbl.place(x=200,y=30)
        
lbl1.place(x=100,y=100)
t1.place(x=200,y=100)
        
lbl2.place(x=100,y=150)
t2.place(x=200,y=150)
              

lbl3.place(x=100,y=200)
t3.place(x=200,y=200)
        
lbl4.place(x=100,y=250)
t4.place(x=200,y=250)
        
lbl5.place(x=100,y=300)
t5.place(x=200,y=300)
        
lbl6.place(x=100,y=350)
t6.place(x=200,y=350)

lbl7.place(x=100,y=400)
t7.place(x=200,y=400)


btn1.place(x=150,y=480)
btn2.place(x=250,y=480)
btn3.place(x=350,y=480)
btn4.place(x=450,y=480)
btn5.place(x=150,y=520)
btn6.place(x=250,y=520)
btn7.place(x=350,y=520)
btn8.place(x=450,y=520)
        
        
       
win.geometry("750x600+300+100")
win.mainloop()


# In[ ]:




