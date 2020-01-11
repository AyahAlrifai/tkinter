from tkinter import *
root=Tk()

frame=Frame(root)
bottomframe=Frame(root)

button1=Button(frame,text='button1')
button2=Button(frame,text='button2')
button3=Button(frame,text='button3')

button4=Button(bottomframe,text='button4')
button5=Button(bottomframe,text='button5')
button6=Button(bottomframe,text='button6')

button1.pack(side=BOTTOM)#بحدد المكان حسب الاوبجكت يلي الهن نفس الفريم
button2.pack(side=BOTTOM)
button3.pack(side=BOTTOM)

button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)

frame.pack(side=LEFT)#بحدد المكان حسب الويندوز
bottomframe.pack(side=BOTTOM)
root.mainloop()