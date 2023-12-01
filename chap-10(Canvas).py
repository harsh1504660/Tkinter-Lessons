from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400
root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root , width=canvas_width , height=canvas_height)
can_widget.pack()

#the line goes from x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill='red')
can_widget.create_line(800,0,0,400,fill='green')

# specify parameters in this order - cor oftop left and cors of botton right
can_widget.create_rectangle(3,5,700,300 ,fill='blue')

can_widget.create_text(200,200,text='python')

can_widget.create_oval(344,233,100,123)

can_widget.create_window(100,750)

root.mainloop()