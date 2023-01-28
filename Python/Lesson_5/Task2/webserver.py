from flask import Flask, render_template, request, redirect
from math import sqrt

app = Flask("Calculator", template_folder='template')

expression = ""

def expressionResult(result):
    global expression
    expression = str(result)

def allInfoAboutExpression(number, mathOperator):
    global expression
    expression += number + mathOperator

def fromStrToInt(expression):
    expressionList = expression.split(" ")
    numberOne = int(expressionList[0])
    mathOperator = expressionList[1]
    if mathOperator == "sqrt":
        quadraticRoot(numberOne)
    else:
        numberTwo = int(expressionList[2])
        calculatorMain(numberOne, numberTwo, mathOperator)

def calculatorMain(numberOne, numberTwo, mathOperator):
    if mathOperator == "^":
        exponentation (numberOne, numberTwo)
    else:
        defaultMathOperation (numberOne, numberTwo, mathOperator)

def quadraticRoot (numberForSqrt):
    expression = sqrt(numberForSqrt)
    return expressionResult(expression)

def exponentation (numberForExponentiation, powerOfNumber):
    expression = numberForExponentiation ** powerOfNumber
    return expressionResult(expression)

def defaultMathOperation (numberOne, numberTwo, mathOperator):
    if mathOperator == "*":
        expression = numberOne * numberTwo
    elif mathOperator == "/":
        expression = numberOne / numberTwo
    elif mathOperator == "+":
        expression = numberOne + numberTwo
    elif mathOperator == "-":
        expression = numberOne - numberTwo
    return expressionResult(expression)
    

@app.route('/')
def index():
    textarea = "<textarea id=\"outputTextarea\" readonly>" + expression + "</textarea>"
    return render_template("index.html", contents = textarea)

@app.route('/number')
def numbers():
    number = request.args.get("number")
    allInfoAboutExpression(number, "")
    return redirect('/')

@app.route('/mathOperator')
def mathOperators():
    mathOperator = " " + request.args.get("mathOperator") + " "
    allInfoAboutExpression("", mathOperator)
    return redirect('/')

@app.route('/result')
def result():
    fromStrToInt(expression)
    return redirect('/')

@app.route('/deleteAllSymbols')
def deleteAllSymbols():
    expressionResult("")
    return redirect('/')

app.run(host="0.0.0.0", port=8081)