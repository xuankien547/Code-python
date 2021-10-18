from tkinter import *
from PIL import Image,ImageTk
root=Tk()

#title
root.title('Tính toán dung lượng tuyến quang')
root.minsize(height=250, width=600)
root.resizable(height=True,width=True)

#icon 
root.iconbitmap('abc.ico')

#Hình nền
load=Image.open('hinh-nen-mau-xanh-4.jpg')
render=ImageTk.PhotoImage(load)
img=Label(root, image=render)
img.place(x=0, y=0)


StringHSA=StringVar
StringHSB=StringVar
StringHSC=StringVar
StringHSD=StringVar
StringHSE=StringVar
StringHSF=StringVar
StringHSG=StringVar




def  action():
    pass
#Label Chính 
Label(root, text="CHƯƠNG TRÌNH TÍNH TOÁN DUNG LƯỢNG OLT DỰA VÀO DỊCH VỤ"
,font=('arial',11,'bold'),relief=FLAT,fg='red',bd=0,bg='#002F67',justify=LEFT).grid(row=0,columnspan=7)

Label(root, text="===================================",relief=FLAT,fg='#FFFFFF',bd=0,bg='#002F67').grid(row=1,columnspan=7)

Label(root,text='Thông số đầu vào:\n',relief=FLAT,fg='black',bd=0,bg='#002F67',justify=LEFT,font=('arial',12,'bold')).grid(row=2,column=0)
Label(root,text='SỐ CARD\n',relief=FLAT,fg='#FFFFFF',bd=0,bg='#01356F',justify=LEFT).grid(row=4,column=0)
Entry(root,width=15,textvariable=StringHSA).grid(row=4,column=1)

Label(root,text='SỐ PORT/CARD\n',relief=FLAT,fg='#FFFFFF',bd=0,bg='#01356F',justify=LEFT).grid(row=6,column=0)
Entry(root,width=15,textvariable=StringHSB).grid(row=6,column=1)

Label(root,text='TỐC ĐỘ HƯỚNG XUỐNG\n',relief=FLAT,fg='#FFFFFF',bd=0,bg='#01356F',justify=LEFT).grid(row=8,column=0)
Entry(root,width=15,textvariable=StringHSC).grid(row=8,column=1)

Label(root,text='TỈ LỆ CHIA 1: \n',relief=FLAT,fg='#FFFFFF',bd=0,bg='#01356F',justify=LEFT).grid(row=10,column=0)
Entry(root,width=15,textvariable=StringHSD).grid(row=10,column=1)

Label(root,text='Thông số đầu ra:\n',relief=FLAT,fg='black',bd=0,bg='#002F67',justify=LEFT,font=('arial',12,'bold')).grid(row=2,column=3)

Label(root,text='SỐ THUÊ BAO TỐI ĐA\n',relief=FLAT,fg='#FFFFFF',bd=0,bg='#01356F',justify=LEFT).grid(row=4,column=3)
Entry(root,width=15,textvariable=StringHSE).grid(row=4,column=4)

Label(root,text='SỐ SPLITTER CẦN THIẾT\n',relief=FLAT,fg='#FFFFFF',bd=0,bg='#01356F',justify=LEFT).grid(row=5,column=3)
Entry(root,width=15,textvariable=StringHSF).grid(row=5,column=4)

Label(root,text='TỐC ĐỘ MỖI THUÊ BAO\n',relief=FLAT,fg='#FFFFFF',bd=0,bg='#01356F',justify=LEFT).grid(row=6,column=3)
Entry(root,width=15,textvariable=StringHSG).grid(row=6,column=4)
Button(text='KẾT QUẢ:').grid(row=20,column=0)
Button(text='TIẾ TỤC',command=action).grid(row=20,column=2)
Button(text='THOÁT',command=root.quit).grid(row=20,column=4)

#name.pack(pady=10)
#name2.pack(pady=10)
#Label(root,text="xuankien").pack()
#Button(root,text='click me',command=root.quit).pack()
#e=StringVar()
#e.set('xuankien')
#Entry(root,textvariable=e,width=30).pack()


root.mainloop()