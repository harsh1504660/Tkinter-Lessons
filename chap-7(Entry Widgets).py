from tkinter import *
def getvals():
    print('The value of username is : ',uservalue.get())
    print('the password is : ',passvalue.get())
root = Tk()
root.geometry("655x333")

user = Label(root , text = 'usernmae')
password = Label(root , text='password')
user.grid()
password.grid()

# variables in tkinter
# booleanvar , IntVar , StringVar , DoubleVar

uservalue = StringVar()                                    ### string variable
passvalue = StringVar() 

user_entry = Entry(root , textvariable=uservalue)           ### entry widgets 
pass_entry = Entry(root , textvariable=passvalue)

user_entry.grid(row=0,column=1)
pass_entry.grid(row=1,column=1)

Button(text='submit', command=getvals).grid()             ### one line packing 
root.mainloop()