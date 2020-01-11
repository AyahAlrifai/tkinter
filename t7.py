import tkinter
root=tkinter.Tk()

def call_me(event):
    print("i'm called")
    
button=tkinter.Button(root,text="click me",bg='red')

button.bind("<Button-1>",call_me)
button.pack()

root.mainloop()

