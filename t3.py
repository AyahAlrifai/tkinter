from tkinter import *
root1=Tk()
root2=Tk()
#كل رووت بتعمل ويندوز واما الفريمز بنفس الويندوز
frame1=Frame(root1,width=300,height=300)
frame2=Frame(root2,width=300,height=300)

frame1.pack()
frame2.pack()

root1.mainloop()
root2.mainloop()