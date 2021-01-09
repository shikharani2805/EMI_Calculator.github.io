from tkinter import *


class  LoanCalculator:
    def __init__(self,master):
        frame=Frame(master)
        
        Label(text="Enter the interest rate(%):",bg="black",fg="white").grid(row=0,column=0,sticky=W)
        self.interestVar=StringVar()
        Entry(textvariable=self.interestVar,bg="sky blue").grid(row=0,column=4)

        Label(text="Year of Loan:",bg="black",fg="white").grid(row=1,column=0,sticky=W)
        self.yearVar=StringVar()
        Entry(textvariable=self.yearVar,bg="sky blue").grid(row=1,column=4)

        Label(text="Enter the loan amount:",bg="black",fg="white").grid(row=2,column=0,sticky=W)
        self.amountVar=StringVar()
        Entry(textvariable=self.amountVar,bg="sky blue").grid(row=2,column=4)

        Label(text="Monthly Payable Amount(EMI):",bg="black",fg="white").grid(row=3,column=0,sticky=W)
        self.monthlyVar=StringVar()
        Entry(textvariable=self.monthlyVar,bg="sky blue").grid(row=3,column=4)

        Label(text="total Amount:",bg="black",fg="white").grid(row=4,column=0,sticky=W)
        self.totalVar=StringVar()
        Entry(textvariable=self.totalVar,bg="sky blue").grid(row=4,column=4)

        Button(text="Calculate",bg="red",command=self.calculation).grid(row=5,column=2)

    def  calculation(self):
        
       try:
            r=float(self.interestVar.get())/1200
            n=float(self.yearVar.get())
            p=float(self.amountVar.get())

            monthly=(p*r*(1+r)**(n*12))/(((1+r)**(n*12))-1)
            total=monthly*12*n
        
            self.monthlyVar.set(format(monthly,"10.2f"))
            self.totalVar.set(format(total,"10.2f"))
       except:
           pass


root=Tk()
app=LoanCalculator(root)
root.mainloop()