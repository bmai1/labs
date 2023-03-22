my_list = [4, 9.7, 11.5, 8, 14, 17.3, 48]
while True:
    target = float(input("Enter target, -000 to quit: "))
    if target == -000:
        break
    found = False
    for index, n in enumerate(my_list):
        if n == target:
            print(index)
            found = True

    if found == False:
        print(str(target), "not found in list.")


