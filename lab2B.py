from math import sqrt
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# quadratic formula function, returns array of x-values
def qf(a, b, c):
    return [((-1 * b) + sqrt((b**2) - (4 * a * c)))/ (2 * a), ((-1 * b) - sqrt((b**2) - (4 * a * c)))/ (2 * a)]

if (b**2 - (4 * a * c) < 0):
    print("The discriminant is negative")
    exit()

ans = qf(a, b, c)
print("x: ", ans[0])
print("x: ", ans[1])
