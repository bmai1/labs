# print("The largest is: ", max(int(input("a: ")), int(input("b: ")), int(input("c: "))))

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)


def max_b(a, b, c):
  if (a >= b and a >= c):
    return a
  if (b >= a and b >= c):
    return b
  if (c >= a and c >= b):
    return c

print("The largest is ", max_b(a, b, c))
