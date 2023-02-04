from tkinter import *

root = Tk()
root.geometry("400x200")
root.title('Fraction Calculator')

mode = "addition"

# recursion for gcd
def g(b, d):
  if (d == 0):
    return abs(b)
  else:
    return g(d, b % d)

def solve_fraction(a, b, c, d):
  global mode
  # if denominator(s) equal zero
  if b == 0 or d == 0:
    return 'Not possible'
  else:
    if mode == "addition" or mode == "subtraction":
      if a == 0 : 
        return ''.join((str(c), '/', str(d)))
      elif c == 0:
        return ''.join((str(a), '/', str(b)))
      
      # negative second numerator when subtraction
      if mode == "subtraction":
        c = 0 - c
      numerator = a * d + b * c
      denominator = b * d

    if mode == "multiplication":
      if a == 0 or c == 0:
        return '0'
      numerator = a * c
      denominator = b * d

    if mode == "division":
      if a == 0:
        return '0'
      if c == 0:
        return 'Not possible'
      numerator = a * d
      denominator = b * c

    gcd = g(numerator, denominator)
    # reduce fraction using gcd even
    while (numerator % gcd == 0 and denominator % gcd == 0):
      if gcd == 1:
        break;
      numerator /= gcd
      denominator /= gcd
    
    # if divide by 1
    if denominator == 1:
      return int(numerator)
    # base case for one
    if numerator == denominator:
      return 1; 
    # simplify improper fractions
    if numerator > denominator:
      return ''.join((str(int(numerator / denominator)), ' ', str(int(numerator % denominator)), '/', str(int(denominator))))

    return ''.join((str(int(numerator)), '/', str(int(denominator)))) 


def callback(selection):
  global mode
  if selection == '+':
    mode = "addition"
  elif selection == '—':
    mode = "subtraction"
  elif selection == 'x':
    mode = "multiplication"
  elif selection == chr(247):
    mode = "division"

options = [
  '+',
  '—',
  'x',
  chr(247)
]
clicked = StringVar()
clicked.set('+')

drop = OptionMenu(root, clicked, *options, command = callback)
drop.place(x = 148,  y = 65)

# sign = Label(root, text = '+')
# sign.place(x = 143, y = 65)

sign = Label(root, text = '=')
sign.place(x = 260, y = 65)


line = Label(root, text = "——")
line.place(x = 101, y = 65)

line = Label(root, text = "——")
line.place(x = 221, y = 65)

# fraction input
a = Entry(root, width = 3)
a.place(x = 100, y = 50)

b = Entry(root, width = 3)
b.place(x = 100, y = 80)

c = Entry(root, width = 3)
c.place(x = 220, y = 50)

d = Entry(root, width = 3)
d.place(x = 220, y = 80)

def solve():
  cover = Label(root, text = '', width = 100, height = 100)
  cover.place(x = 280, y = 0)
  sum = solve_fraction(int(a.get()), int(b.get()), int(c.get()), int(d.get()))
  bob = Label(root, text = sum, font='Helvetica 18 bold', fg = 'red')
  bob.place(x = 280, y = 55)
  
ans = Button(root, width = 6, text = "Calculate", command = solve)
ans.place(x = 136, y = 120)

root.mainloop()
