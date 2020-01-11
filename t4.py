from tkinter import *
root=Tk()
one=Label(root,text='One ',bg='red')
two=Label(root,text='Two',bg='yellow')
three=Label(root,text='Three',bg='blue')

one.pack(fill=X)
two.pack()
three.pack(fill=Y,side=LEFT)

root.mainloop()

