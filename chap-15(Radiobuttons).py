from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("655x333")

def order():
    tmsg.showinfo('ORDER RESCIVIED',f"your order is : {var.get()}")

var = StringVar()
#var.set(1)
Label(root , text='what would you like to have?',justify=LEFT,padx=14,font="lucida 19 bold").pack()

radio = Radiobutton(root,text='dosa',padx=14,variable=var,value='dosa').pack(anchor='nw')
radio = Radiobutton(root,text='idli',padx=14,variable=var,value='idli').pack(anchor='nw')
radio = Radiobutton(root,text='paratha',padx=14,variable=var,value='paratha').pack(anchor='nw')
radio = Radiobutton(root,text='pizza',padx=14,variable=var,value='pizza').pack(anchor='nw')

Button(text='order now',command=order).pack()
root.mainloop()