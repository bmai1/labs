start = int(input("Start value: "))
end = int(input("End value: "))


# create consecutive numbers file
file_n = open("consecutive_numbers.txt", 'w')
while (start <= end):
    file_n.write(str(start) + '\n')
    start += 1
file_n.close()


# reading from file, creating result file
total = 0 
lines = 0
with open("consecutive_numbers.txt") as file:
    for line in file:
        total += int(line)
        lines += 1
file_r = open("results.txt", 'w')
file_r.write("The sum is: " + str(total) + '\n')
file_r.write("The average is: " + str(total / lines))


print("The sum is: " + str(total))
print("The average is: " + str(total / lines))
