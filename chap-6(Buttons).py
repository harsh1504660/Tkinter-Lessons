from tkinter import *
def hello():
    print("hello tkinter world")
root = Tk()
root.geometry("655x333")

frame = Frame(root , borderwidth=6,bg='grey',relief=SUNKEN)
frame.pack(side=LEFT,anchor='nw')

b1 = Button(frame , fg='red' , text='print now',command=hello)
b1.pack()

root.mainloop()