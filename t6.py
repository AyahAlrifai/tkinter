from tkinter import *
root=Tk()

def call_me():
    print("i'm called")
    
button=Button(root,text="click me",command=call_me)
#كوماند من خلالها بحدد اذا كبست على هاد البوتون ايش رح يصير؟
button.pack()

root.mainloop()

