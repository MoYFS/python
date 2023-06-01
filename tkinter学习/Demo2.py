from tkinter import *
from tkinter.messagebox import *

root=Tk()
root.geometry('400x350')
menu=Menu(root)
def callback():
    print("this is menu")
for item in ['文件','编辑','视图','格式']:
    menu.add_command(label=item,
    command=callback)
root['menu']=menu

# def change(label):
#     label['text']='hello world'
#
# lb=Label(root,text='事件处理示例')
# lb.pack()
# bt=Button(root,text='更改',command=lambda :change(lb))
# bt.pack()

# def headler(event):
#     showinfo('点到了','你好')
# button=Button(root,text='点我啊！')
# button.bind('<Double-Button-1>',headler)
# button.pack()
root.mainloop()

