from tkinter import *

root = Tk()
root.geometry("733x566")

#use this to create non dropdown menu
def func():
    print("i am a function")
"""my_menue = Menu(root)
my_menue.add_command(label='file',command=func)
my_menue.add_command(label='exit',command=quit)
root.config(menu=my_menue)"""

mainmenu = Menu(root)
m1 = Menu(mainmenu , tearoff=0)
m1.add_command(label='save',command=func)
m1.add_command(label='new project',command=func)
m1.add_separator()                                     ### creates the line between the options
m1.add_command(label='print',command=func)

mainmenu.add_cascade(label='file', menu=m1)
root.config(menu=mainmenu)

m2 = Menu(mainmenu , tearoff=0)
m2.add_command(label='save',command=func)
m2.add_command(label='new project',command=func)
m2.add_separator()                                     ### creates the line between the options
m2.add_command(label='print',command=func)

mainmenu.add_cascade(label='jay hind', menu=m2)
root.config(menu=mainmenu)
root.mainloop() 