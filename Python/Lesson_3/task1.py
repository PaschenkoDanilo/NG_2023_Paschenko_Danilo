from math import sqrt

def main ():
    print ("Hello! It is calculator.")
    print ("Math operators available: +, -, *, /, ^, square root(input: sqrt).")
    mathOperator = input("Input math operator which you want: ")
    if mathOperator == "^":
        exponentation ()
    elif mathOperator == "sqrt":
        quadraticRoot ()
    else: defaultMathOperation (mathOperator)


def exponentation ():
    numberForExponentiation = int(input("Input number: "))
    powerOfNumber = int(input("Input power of number: "))
    print ("Result: " + str(numberForExponentiation ** powerOfNumber))

def quadraticRoot ():
    numberForSqrt = int(input("Input number: "))
    print ("Result:" + str(sqrt(numberForSqrt)))

def defaultMathOperation (mathOperator):
    numberOne = int(input("Input number one: "))
    numberTwo = int(input("Input number two: "))
    print ("Result:" , end = " ")
    if mathOperator == "+":
        print (numberOne + numberTwo)
    elif mathOperator == "-":
        print (numberOne - numberTwo)
    elif mathOperator == "*":
        print (numberOne * numberTwo)
    else:
        print (numberOne / numberTwo)



main ()