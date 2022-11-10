numberList = input("Input number list: ")
numberList = list(map(lambda x: int(x), numberList.split(", ")))

print ("Max value: " + str(max(numberList)) + "\n" + "Min value: " + str(min(numberList)))
numberList.remove (max(numberList))
numberList.remove (min(numberList))
sum = 0
for number in numberList:
    sum += int(number)
print ("Sum of numbers without max and min: " + str(sum))