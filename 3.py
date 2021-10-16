from tkinter import *
import tkinter
root=Tk()
root.title("Di chuyen tam giac")
cas = Canvas(root, width=500,height=700)
cas.pack()
cas.create_polygon(10,10,10,30,40,30)
def dichuyen(event):
    if event.keysym == 'Up':
        cas.move(1,0,-30)
    elif event.keysym == 'Down':
        cas.move(1,0,30)
    elif event.keysym == 'Left':
        cas.move(1,-30,0)
    else:
        cas.move(1,30,0)
cas.bind_all('<KeyPress-Up>',dichuyen)
cas.bind_all('<KeyPress-Down>',dichuyen)
cas.bind_all('<KeyPress-Left>',dichuyen)
cas.bind_all('<KeyPress-Right>',dichuyen)
root.mainloop()