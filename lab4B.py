from tkinter import *

# checking balance = cb, savings balance  = sb
cb = 500.00
sb = 2000.00

# window size, title, background color
root = Tk()
root.geometry("400x300")
root['background'] = '#f0ffff'
root.title('Bank Account')

myLabel = Label(root, text="Enter amount to deposit, withdraw, or transfer", bg = '#defffc')
myLabel.pack()

# user input box
dollar = Label(root, text = "$", bg = '#f0ffff')
dollar.place(x = 105, y = 20)
e = Entry(root)
e.pack()

# ValueError exception not handled, when user enters an empty string or non-numerical value to deposit, transfer, withdraw

# button functions: print_balance, deposit, withdraw, transfer
def print_balance():
  # empty string widget to cover overlap
  cover = Label(root, text = "                                                                                                    ", bg = '#f0ffff')
  cover.place(x = 15, y = 200)
  # print balances
  s = "Checking balance: $" + format(cb, '.2f') + ", Savings balance: $" + format(sb, '.2f')
  caption = Label(root, text = s, bg = '#defffc')
  caption.place(x = 15, y = 200)

def deposit():
  cover = Label(root, text = "                                                                                                    ", bg = '#f0ffff')
  cover.place(x = 15, y = 200)
  global cb
  cb += float(e.get())
  caption = Label(root, text = "Deposit successful", bg = '#defffc')
  caption.place(x = 15, y = 200)

def withdraw():
  cover = Label(root, text = "                                                                                                    ", bg = '#f0ffff')
  cover.place(x = 15, y = 200)
  global cb
  if float(e.get()) <= cb:
    cb -= float(e.get())
    caption = Label(root, text = "Withdraw successful", bg = '#defffc')
    caption.place(x = 15, y = 200)
  else: 
    caption = Label(root, text = "Insufficient funds", bg = '#defffc')
    caption.place(x = 15, y = 200)

def transfer():
  cover = Label(root, text = "                                                                                                    ", bg = '#f0ffff')
  cover.place(x = 15, y = 200)
  global cb
  global sb
  if float(e.get()) <= sb:
    sb -= float(e.get())
    cb += float(e.get())
    caption = Label(root, text = "Transfer successful", bg = '#defffc')
    caption.place(x = 15, y = 200)
  else: 
    caption = Label(root, text = "Insufficient funds", bg = '#defffc')
    caption.place(x = 15, y = 200)

# space under input box, because I am too lazy to manually position widgets

# button widgets
sp = Label(root, text = "", bg = '#f0ffff')
sp.pack()
    
p = Button(root, text = "Balance", width = 8, command = print_balance)
p.pack()

d = Button(root, text = "Deposit", width = 8, command = deposit)
d.pack()

w = Button(root, text = "Withdraw", width = 8, command = withdraw)
w.pack()

t = Button(root, text = "Transfer", width = 8, command = transfer)
t.pack()

root.mainloop()
