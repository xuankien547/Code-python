from tkinter import *
from PIL import Image,ImageTk
#tao tk window
root=Tk()
root.title('Google Translate')
#root.iconbitmap('image_MCL_icon.ico')
root.minsize(height=500, width=500)


load=Image.open('images.jpg')
render=ImageTk.PhotoImage(load)
img=Label(root,Image=render)
img.place(x=0,y=0)

name=Label(root,text=XuanKien,fg="#FFFFFF",bd=0)

root.mainloop()      