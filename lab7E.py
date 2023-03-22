height = float(input("Height: "))
bounciness = float(input("Bounciness: "))
num = int(input("Number of bounces: "))
distance = 0
while (num > 0):
    distance += height + height * bounciness
    height *= bounciness
    num -= 1
print("Total distance traveled is:" "", round(distance, 4), "units.")