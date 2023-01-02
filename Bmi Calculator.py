from tkinter import *
root = Tk()

#The size
root.geometry("500x500")
#Title
Label(root, text= "BMI calculator \n By NFT Ape")
#Questions
Label(root, text= " How much to you wieght? (In Kg) ").pack()
Kg = Entry(root)
Kg.pack()

Label(root, text= " How tall are you? (In meters) ").pack()
Meter = Entry(root)
Meter.pack()


def last():
    lasts = Toplevel()
    #The BMI
    bmoiiiii = float(Kg.get()) / float(Meter.get()) ** 2

    Label(lasts,text= f"Your BMI is {str(bmoiiiii)}" ).pack()

    lasts.mainloop()
#The Button
Button(root,text="Here is your BMI",command= last).pack()
root.mainloop()
