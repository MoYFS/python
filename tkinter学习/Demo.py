from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("个人信息调查")

def funcOK():
    strSex='男' if(vSex.get()=='M')else '女'
    strMusic = checkbokMusic['text'] if(vHobbyMusic.get()==1) else ''
    strSports=checkbokSports["text"] if(vHobbySports.get()==1) else ''
    strTravel = checkbokTravel["text"] if(vHobbyTravel.get()==1) else ''
    strMovie = checkbokMovie["text"] if(vHobbyMovie.get()==1) else ''
    str1=entryName.get()+'您好：\n'
    str1+="您的性别是："+strSex+"\n"
    str1+="您的爱好是：\n"+strMusic+''+strSports+''+strTravel+''+strMovie
    messagebox.showinfo("个人信息调查",str1)

lbTitle=Label(root,text='个人信息调查')
lbName=Label(root,text="姓名")
lbSex=Label(root,text="性别")
lbHobby=Label(root,text='爱好')
lbTitle.grid(row=0,column=0,columnspan=4)
lbName.grid(row=1,column=0)
lbSex.grid(row=2,column=0)
lbHobby.grid(row=3,column=0)

entryName=Entry(root)
entryName.grid(row=1,column=1,columnspan=3)
vSex=StringVar()
vSex.set("M")
radioSexM=Radiobutton(root,text="男",value="M",variable=vSex)
radioSexF=Radiobutton(root,text="女",value="F",variable=vSex)
radioSexM.grid(row=2,column=1)
radioSexF.grid(row=2,column=2)
vHobbyMusic=IntVar()
vHobbySports=IntVar()
vHobbyTravel=IntVar()
vHobbyMovie=IntVar()
checkbokMusic=Checkbutton(root,text="音乐",variable=vHobbyMusic)
checkbokSports=Checkbutton(root,text="运动",variable=vHobbySports)
checkbokTravel=Checkbutton(root,text="旅游",variable=vHobbyTravel)
checkbokMovie=Checkbutton(root,text="影视",variable=vHobbyMovie)
checkbokMusic.grid(row=3,column=1)
checkbokSports.grid(row=3,column=2)
checkbokTravel.grid(row=3,column=3)
checkbokMovie.grid(row=3,column=4)
btnOk=Button(root,text="提交",command=funcOK)
btnOk.grid(row=4,column=1,sticky=E)
btnCancel=Button(root,text="取消",command=root.destroy)
btnCancel.grid(row=4,column=3,sticky=W)

root.mainloop()


