from tkinter import *
root=Tk()

name=Label(root,text="name")
password=Label(root,text="password")

entry1=Entry(root)
entry2=Entry(root)

name.grid(row=0,sticky=E)
#ستيكي بتخلي الكلمة تلزق بال تكست بوكس
entry1.grid(row=0,column=1)

password.grid(row=1,column=0)
entry2.grid(row=1,column=1)

c=Checkbutton(root,text="keep me logged in")
c.grid(columnspan=2)


root.mainloop()

