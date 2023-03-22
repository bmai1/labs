import math
c7Test = [78, 65, 91, 62, 84, 72, 100, 59, 91, 57, 81]
lo = 100
hi = 0
total = 0
c7Test.sort()
print(c7Test)
# brute force
for n in c7Test:
    total += n 
    if n < lo:
        lo = n
    if n > hi:
        hi = n

print("Low:", lo)
print("High:", hi)
print("Average: " + str(round(total / len(c7Test), 1)))

if len(c7Test) % 2 == 0:
    print(len(c7Test) / 2)
    print((len(c7Test) / 2) - 1)
    median = (c7Test[int(len(c7Test) / 2)] + c7Test[int(len(c7Test) / 2) - 1]) / 2
else:
    median = c7Test[math.floor(len(c7Test) / 2)]

print("Median:", median)

target = int(input("Enter score to count: "))
count = 0
for n in c7Test:
    if n == target:
        count += 1
print("There are", count, "tests with a score of", target)