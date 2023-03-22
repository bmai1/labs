file_name = input("File name: ")
print('{:<13}'.format("Names"), '{:<15}'.format("Hours Worked"), "Weekly Pay")
print('-'*43)
with open(file_name) as file:
    for line in file:
        line = line.split()
        hourly = float(line[1])
        hours = float(line[2])
        if hours <= 40:
            pay = hourly * hours
        else:
            pay = (40 * hourly) + (hours - 40) * 1.5 * hourly
        print('{:<13}'.format(line[0]), '{:<15}'.format(hours), '$' + format(pay, '.2f'))