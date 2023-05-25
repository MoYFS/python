from tkinter import *

# root =Tk()
# root.title("hello world")
# root.geometry('1024x648+234+88')
# bg=PhotoImage(file='Demo.png')
# label1=Label(root,image=bg).pack()
# root.mainloop()
root=t=Tk()
root.title("设置字体大小")
root['width']=400
root['height']=50

def changefont(value):
    fontNew=('Helvetica',scaleFont.get(),'bold')
    lblTitle.config(font=fontNew)

scaleFont=Scale(root,from_=10,to=60,length=400,orient=HORIZONTAL,command=changefont)
scaleFont.set(20)
scaleFont.pack()
lblTitle=Label(root,text="Hello",font=('Helvetica',20,'bold'))
lblTitle.pack()
root.mainloop()