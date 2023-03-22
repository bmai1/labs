from random import randint


total = 0
trials = int(input("Trials: "))
trial = 1
print()
while trial <= trials:
    print("Trial", trial)
    rolls = 0
    while True:
        roll = randint(1, 6)
        rolls += 1
        total += 1
        print("Roll", rolls, ":", roll)
        if roll == 6:
            break
    print("It took", rolls, "rolls to get '6'")
    trial += 1; 
print("Total rolls:", total)
print("Average:", total / trials)