numberList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

for item in numberList:
    if item < 5:
        newList.append(item)

print(newList)