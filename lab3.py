def print_grid():
  for i in range(3):
    print("+ - - - - + - - - - +")
    if i == 2: 
      break
    for j in range(4):
      print("|         |         |")

def triangle_area(base, height):
  print("The area is ", 0.5 * base * height, " units squared.")

triangle_area(4,2)

def cube(num):
  # This function is useless
  return num ** 3

print(cube(2))