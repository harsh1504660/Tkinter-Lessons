from tkinter import *

root = Tk()

root.geometry("655x333")
f1 = Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
f1.pack(side=LEFT,fill=Y)
l = Label(f1 , text="project tkinter")
l.pack(pady=142)
F2 = Frame(root,background="grey",borderwidth=8,relief=SUNKEN)
F2.pack(side=TOP,fill=X)
l2 = Label(F2 , text="welcome to sublime text",font="Helvetica 19 bold",fg='red')
l2.pack()
root.mainloop()