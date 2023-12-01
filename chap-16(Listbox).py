from tkinter import *
i=0
def add():
    global i
    lbx.insert(ACTIVE , f"{i}")
    i=i+1
root = Tk()
root.geometry("655x333")
lbx = Listbox(root)
lbx.pack()
lbx.insert(END,'first item of a listbox')

Button(root,text='add item',command=add).pack()
root.mainloop() 