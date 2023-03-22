from random import randint
while True:
    try:
        n = randint(1, 5)
        if (int(input("Guess: ")) == n):
            print("Correct")
        else:
            print("Incorrect, the answer is: ", n)
    except ValueError:
        continue
