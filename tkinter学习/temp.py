from tkinter import *

root=Tk()
root.title("登录")
root.geometry('512x324+234+88')
f1=Frame(root)
f1.pack()
f2=Frame(root)
f2.pack()
f3=Frame(root)
f3.pack()
Label(f1,text="用户名").pack(side=LEFT)
Entry(f1).pack(side=LEFT)
Label(f2,text="密   码").pack(side=LEFT)
Entry(f2,show="*").pack(side=LEFT)
Button(f3,text='登录').pack(side=RIGHT)
Button(f3,text='取消').pack(side=RIGHT)
v=StringVar()
v.set("YES")
w=Checkbutton(root,text='音乐',variable=v,onvalue="yes",offvalue="no").pack()

root.mainloop()
