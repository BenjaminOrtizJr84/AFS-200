import random

n = random.randint(1, 9)
guess = int(input('Enter a number from 1 to 9: '))
while n != "guess":
    print
    if guess < n:
        print("Guess is low")
        guess = int(input('Enter an number from 1 to 9: '))
    elif guess > n:
        print("Guess is high")
        guess = int(input('Enter an number from 1 to 9: '))
    else:
        print('You guessed it! Game Over.')
        break
    