userName = input("Enter your name: ")
userAge = int(input("Enter your age: "))

yearsLeft = 100 - userAge
year100 = yearsLeft + 2021

print("Hello " + userName + "!" + " You are " + str(userAge) + " years old, and will turn 100 years old in " + str(year100) + "!") 