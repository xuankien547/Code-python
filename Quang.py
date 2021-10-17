from tkinter import *
from PIL import Image,ImageTk
root=Tk()

#title
root.title('Tính toán dung lượng tuyến quang')
root.minsize(height=600, width=600)

#icon 
root.iconbitmap('abc.ico')

#Hình nền
load=Image.open('hinh-nen-mau-xanh-4.jpg')
render=ImageTk.PhotoImage(load)
img=Label(root, image=render)
img.place(x=0, y=0)

#Label Chính 
Label(root, text="CHƯƠNG TRÌNH TÍNH TOÁN DUNG LƯỢNG OLT DỰA VÀO DỊCH VỤ CUNG CẤP"
,justify=CENTER,relief=SUNKEN,fg='#FFFFFF',bd=0,bg='#002F67').grid(row=0,column=1)
Label(root, text="==================================="
,justify=CENTER,relief=SUNKEN,fg='#FFFFFF',bd=0,bg='#002F67').grid(row=1,column=1)
#name.config(font=('GlamourAbsolute_Regular.otf',13))
#name2.config(font=('GlamourAbsolute_Regular.otf',13))
#name.pack(pady=10)
#name2.pack(pady=10)
Label(root,text="xuankien").pack()
Button(root,text='click me',command=root.quit).pack()
e=StringVar()
e.set('xuankien')
Entry(root,textvariable=e,width=30).pack()


root.mainloop()