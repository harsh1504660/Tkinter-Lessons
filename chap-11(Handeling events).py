from tkinter import *

def harsh(event):
    print(f"you clicked the button at {event.x} and {event.y}")
root = Tk()
root.geometry("644x355")

widget = Button(root , text='click me please')
widget.pack()

widget.bind('<Button-1>',harsh)
widget.bind('<Double-1>',quit)
root.mainloop()