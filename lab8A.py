read = input("Read from: ")
write = input("Write to: ")
file1 = open(read, 'r')
file2 = open(write, 'w')
for line in file1:
    file2.write(line)
file1.close()
file2.close()
