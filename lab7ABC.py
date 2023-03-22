# Lab 7A
def oddTo(n):
  sum = 0
  # n + 1 so it checks last number 
  for i in range(n + 1):
    if i % 2 != 0:
      sum += i
  return sum

# Lab 7B
def sumSq(n):
  sum = 0
  for i in range(n):
    sum += (i + 1) ** 2
    if (i + 1) < n:
      print((i + 1) ** 2, '+ ', end='')
    # last num
    else:
      print((i + 1) ** 2, '= ', end='')
  return sum 

# Lab 7C
def rsum_three():
  start = int(input("Start: "))
  end = int(input("End: "))
  
  sum = 0
  # inclusive
  while (start <= end):
    sum += start
    if start + 3 < end: 
      print(start, '+ ', end='')
    else:
      print(' +', start, end='')
    start += 3
  
  print(" =", sum)
