from tkinter import *
from PIL import Image , ImageTk

root = Tk()

root.geometry("235x450")

#photo = PhotoImage(file="Capture11.PNG")

#foe jpg images
image = Image.open("1.jpg")
image = image.resize((235,450))
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()
root.mainloop()