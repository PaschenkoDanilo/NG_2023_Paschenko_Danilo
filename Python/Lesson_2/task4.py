factorial = int(input("Input factorial: "))

for iterationNumber in range(1,factorial):
    factorial = factorial * iterationNumber
print ("Result: " + str(factorial))