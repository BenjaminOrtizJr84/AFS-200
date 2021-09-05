from functools import reduce

numberList = [3,6,9,12,15]

total = reduce (lambda x, y: x*y, numberList)

print(total)