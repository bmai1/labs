from random import randint
list = []
# list = [35, 6, 25, 11, 36, 17]

ls = int(input("List size: "))
for i in range(ls):
    list.append(randint(1, 50))

print(list)

for index, n in enumerate(list):
    if index >= len(list) / 2:
        break
    print("Sum of pair", index + 1, "is", list[index] + list[len(list) - 1 - index])