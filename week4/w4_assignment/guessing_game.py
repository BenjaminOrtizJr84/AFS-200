import random

n = random.randint(1, 9)
guess = int(input("Enter an integer from 1 to 9: "))
while n != "guess":
    print
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 9: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 9: "))
    else:
        print("you guessed it!")
        break
    print