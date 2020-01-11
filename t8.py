import tkinter
root=tkinter.Tk()

def rightclick(event):
    print("right click")

def leftclick(event):
    print("left click")
    
def middleclick(event):
    print("middle click")
    
frame=tkinter.Frame(root,width=300,height=300,bg="green")

frame.bind("<Button-1>",leftclick)
frame.bind("<Button-3>",rightclick)
frame.bind("<Button-2>",middleclick)


frame.pack()
root.mainloop()

