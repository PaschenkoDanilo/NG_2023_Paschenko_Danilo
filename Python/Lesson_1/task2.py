from math import sqrt

print ("Hello! It is calculator")
print ("Math operators available: +, -, *, /, ^, square root(input: sqrt)")
mathOperator = input("Input math operator which you want: ")
if mathOperator == "^":
    numberForExponentiation = int(input("Input number: "))
    powerOfNumber = int(input("Input power of number: "))
    print ("Result: " + str(numberForExponentiation** powerOfNumber))
elif mathOperator == "sqrt":
    numberForSqrt = int(input("Input number: "))
    print ("Result:" + str(sqrt(numberForSqrt)))
else:
    numberOne = int(input("Input number one: "))
    numberTwo = int(input("Input number two: "))
    print ("Result:" , end = " ")
    if mathOperator == "+":
        print (numberOne + numberTwo)
    if mathOperator == "-":
        print (numberOne - numberTwo)
    if mathOperator == "*":
        print (numberOne * numberTwo)
    if mathOperator == "/":
        print (numberOne / numberTwo)
    

    
