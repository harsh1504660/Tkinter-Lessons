from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("655x333")
def getdollar():
    print(f"{myslider2.get()}dollars credited")
    tmsg.showinfo('massage',f"{myslider2.get()}dollars credited")
"""myslider = Scale(root , from_=0,to=100)
myslider.pack()"""
Label(root,text='how many dollars you want').pack()
myslider2 = Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(34)                                                ### default value
myslider2.pack()
Button(root,text='get dollars',command=getdollar).pack()
root.mainloop()


