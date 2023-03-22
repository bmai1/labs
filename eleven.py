num = int(input("Number: "))
width = len(str(num)) + 2
while (num > 100):
  print('{num:<{width}}{tmp} - {last}'.format(num=num, width=width, tmp=num//10, last=num%10))
  num = (num // 10) - (num % 10)
ans = "YES" if num % 11 == 0 else "NO"
print('{num:<{width}}{ans}'.format(num=num, width=width, ans=ans))