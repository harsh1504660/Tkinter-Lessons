from tkinter import *

root = Tk()
root.geometry("655x333")
#heading
Label(root , text="welcome to travels",font="comicsansms 13 bold",pady=15).grid(column=3)

#text for forms
name = Label(root,text='name')
phone = Label(root,text='phone number')
gender = Label(root,text='phone gender')
em_contact = Label(root,text='emergency contact')
payment_mode = Label(root,text='payment mode')

# packing the text
name.grid(row= 1, column=2)
phone.grid(row=2 , column=2)
gender.grid(row= 3, column=2)
em_contact.grid(row= 4, column=2)
payment_mode.grid(row=5 , column=2)

#tkinter variable for storing the entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
em_contactvalue = StringVar()
payment_modevalue = StringVar()

foodservice_value = IntVar()             ## checkbox

#Entries for form
nameentry = Entry(root , textvariable=namevalue)
phoneentry = Entry(root , textvariable=phonevalue)
genderentry = Entry(root , textvariable=gendervalue)
em_contactentry = Entry(root , textvariable=em_contactvalue)
payment_modeentry = Entry(root , textvariable=payment_modevalue)

#packing the entry
nameentry.grid(row = 1,column=3)
phoneentry.grid(row = 2,column=3)
genderentry.grid(row = 3,column=3)
em_contactentry.grid(row =4 ,column=3)
payment_modeentry.grid(row =5 ,column=3)

#checkbox & packing
foodservice = Checkbutton(text='want to take your meal',variable=foodservice_value)
foodservice.grid(row=6,column=3)

#button making
def getvals():
    print("works") 
Button(text='submit to travels',command=getvals).grid(row=7,column=3)
root.mainloop()