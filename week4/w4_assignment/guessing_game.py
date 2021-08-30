# Guessing Number Game

import random

guessTotal = 0

print('Hello! Welcome to The Number Guessing Game! What is your name?')
myName = input()

number = random.randint(1, 9)
print('Step right up, ' + myName + ', I am thinking of a number between 1 and 9.')

while guessTotal < 9:

    print    ('What is my number? (*HINT* Enter your guess using the keyboard number keys.)') 
    guess = input()
    guess = int(guess)

    guessTotal = guessTotal + 1

    if guess < number:
        print        ('Your guess is less than my number.')

    if guess > number:
        print        ('Your guess is higher than my number.')

    if guess == number:
        break

if guess == number:
    guessTotal = str(guessTotal)
    print('Good job, ' + myName + '! Your total guesses are ' + guessTotal + '!')