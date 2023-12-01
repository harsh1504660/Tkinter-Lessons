from tkinter import *

root = Tk()
root.geometry("655x333")

# for connecting scrollbar to widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command = widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(fill=Y,side=RIGHT)
lbx = Listbox(root , yscrollcommand= scrollbar.set)
for i in range(344):
   lbx.insert(END , f"item : {i}")
text = Text(root , yscrollcommand= scrollbar.set)
text.pack(fill=BOTH)
scrollbar.config(command = text.yview)
scrollbar.config(command = lbx.yview)
lbx.pack(fill=BOTH)
root.mainloop()