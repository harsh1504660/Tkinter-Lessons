from tkinter import *

root = Tk()

# width X heigth
root.geometry('644x434')        ### decides the size of gui screen

# width , heigth
root.minsize(200,100)         ### decides the minimum size

root.maxsize(1200,988)

harsh = Label(text='this is the first demo hello world')
harsh.pack()

root.mainloop()