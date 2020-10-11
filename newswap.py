#program to swap first and last element of a list:
def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList

newList = [20, 30, 40, 50, 60]
print(swapList(newList))






