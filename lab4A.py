from tkinter import *

root = Tk()

myLabel = Label(root, text="Enter a number")
myLabel.pack()

# user input
e = Entry(root)
e.pack()

def click():
  ans = Label(root, text = int(e.get()) * 2)
  ans.pack()
  
# button to double
button = Button(root, text="Click to double up!", command = click)
button.pack()

root.mainloop()