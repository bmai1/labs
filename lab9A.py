print("Enter list values, Enter \"-000\" to stop")
list = []
while True:
    num = int(input())
    if num == -000:
        break
    list.append(num)
print(list)
print("Enter a) total sum, b) sum of even values, c) sum of odd values, q) quit.")

a = 0
b = 0
c = 0
for n in list:
    a += n
    if n % 2 == 0:
        b += n
    else:
        c += n

while True:
    cmd = input()
    if cmd == 'q':
        break
    if cmd == 'a':
        print("Total sum:", a)
    elif cmd == 'b':
        print("Even sum:", b)
    elif cmd == 'c':
        print("Odd sum:", c)


