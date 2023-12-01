from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("733x566")

#use this to create non dropdown menu
def func():
    print("i am a function")

def help():
    print("i will help you")
    tmsg.showinfo("help","i will help you")
def exits():
    a=tmsg.askquestion('help','do you want to exit')
    if a=='yes':
        quit()
    else:
        pass
mainmenu = Menu(root)
m1 = Menu(mainmenu , tearoff=0)
m1.add_command(label='save',command=func)
m1.add_command(label='new project',command=func)
m1.add_separator()                                     ### creates the line between the options
m1.add_command(label='exit',command=exits)
mainmenu.add_cascade(label='file', menu=m1)
root.config(menu=mainmenu)

m2 = Menu(mainmenu , tearoff=0)
m2.add_command(label='copy',command=func)
m2.add_command(label='cut',command=func)
m2.add_separator()                                     ### creates the line between the options
m2.add_command(label='find',command=func)
mainmenu.add_cascade(label='jay hind', menu=m2)
root.config(menu=mainmenu)

m3 = Menu(mainmenu,tearoff=0)
m3.add_command(label='help',command=help)
mainmenu.add_cascade(label='Edit',menu=m3)
root.config(menu=mainmenu)
root.mainloop() 