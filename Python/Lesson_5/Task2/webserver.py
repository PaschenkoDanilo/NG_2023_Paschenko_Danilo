from flask import Flask, render_template, request, redirect
from math import sqrt

app = Flask("Calculator", template_folder='template')

numberPrint1 = ""
numberPrint2 = ""
numberOne = 0
numberTwo = 0
mathOperator = ""
logical = False

def main ():
    if mathOperator == "^":
        exponentation ()
    elif mathOperator == "sqrt":
        quadraticRoot ()
    elif mathOperator == "*" or mathOperator == "/" or mathOperator == "+" or mathOperator == "-": 
        defaultMathOperation ()

def exponentation ():
    global numberPrint1
    deleteAllSymbols()
    numberPrint1 = str(numberOne ** numberTwo)

def quadraticRoot ():
    global numberPrint1
    deleteAllSymbols()
    numberPrint1 = sqrt(numberOne)

def defaultMathOperation ():
    global numberPrint1
    deleteAllSymbols()
    if mathOperator == "*":
        numberPrint1 = numberOne * numberTwo
    elif mathOperator == "/":
        numberPrint1 = numberOne / numberTwo
    elif mathOperator == "+":
        numberPrint1 = numberOne + numberTwo
    elif mathOperator == "-":
        numberPrint1 = numberOne - numberTwo

@app.route('/')
def index():
    textareaPrint = "<textarea readonly id=\"outputTextarea\">" + str(numberPrint1) + str(numberPrint2) + "</textarea>"
    return render_template("index.html", contents = textareaPrint)

@app.route('/number1')
def number1():
    global numberPrint1
    global numberPrint2
    if logical == False:
        numberPrint1 += request.args.get('number1')
    elif logical == True:
        numberPrint2 += request.args.get('number1')
    return redirect('/')

@app.route('/number2')
def number2():
    global numberPrint1
    global numberPrint2
    if logical == False:
        numberPrint1 += request.args.get('number2')
    elif logical == True:
        numberPrint2 += request.args.get('number2')
    return redirect('/')

@app.route('/number3')
def number3():
    global numberPrint1
    global numberPrint2
    if logical == False:
        numberPrint1 += request.args.get('number3')
    elif logical == True:
        numberPrint2 += request.args.get('number3')
    return redirect('/')

@app.route('/deleteAllSymbols')
def deleteAllSymbols():
    global numberPrint1
    global numberPrint2
    global logical
    logical = False
    numberPrint1 = ""
    numberPrint2 = ""
    return redirect('/')

@app.route('/mathOperators')
def mathOperators():
    global numberPrint1
    global numberOne
    global mathOperator
    global logical
    mathOperator = request.args.get('mathOperator')
    numberOne = int(numberPrint1)
    logical = True
    if mathOperator == "sqrt":   
        numberPrint1 = "sqrt(" + str(numberOne) + ")"
    else:
        numberPrint1 +=  mathOperator
    return redirect('/')

@app.route('/result')
def result():
    global numberPrint2
    global numberTwo
    if mathOperator != "sqrt":
        numberTwo = int(numberPrint2)
    main()
    return redirect('/')

app.run(host="0.0.0.0", port=8081)