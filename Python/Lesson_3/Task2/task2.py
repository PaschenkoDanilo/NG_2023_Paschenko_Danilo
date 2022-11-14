import sys
from task2addition import *

def main ():
    text = input("Input string: ")
    menu (text)
    return text

def sortText (text):
    printLine()
    resultMessage (" ".join(sorted(splitting(text))))
    printLine ()
    menu (text)

def countElements (text):
    wordsList = splitting(text)
    printLine ()
    resultMessage(len(wordsList))
    printLine ()
    menu (text)

def vowelsOrConsonants (text):
    printLine ()
    print ("What you want?" + "\n" + "1 - Vowels" + "\n" + "2 - Consonats")
    vowelsOrConsonatsChoice = input ("Input number: ")
    match vowelsOrConsonatsChoice:
        case "1":
            printLine ()
            resultMessage (vowelsList(text))
            printLine ()
        case "2":
            printLine ()
            resultMessage (consonantsList(text))
            printLine ()
        case _:
            printLine ()
            error ("Your number incorrect")
            vowelsOrConsonants (text)
    menu (text)
def vowelsList (text):
    text = text.lower ()
    listOfVowels = []  
    for vowels in "aeiouy":
        if vowels in text:
            listOfVowels += vowels
    return ", ".join(listOfVowels)
def consonantsList (text):
    text = text.lower ()
    listOfConsonats = []  
    for consonats in "bcdfghjklmnpqrstvwxz":
        if consonats in text:
            listOfConsonats += consonats
    return ", ".join(listOfConsonats)

def converselyText (text):
    printLine ()
    wordsList = splitting(text)
    converselyWordsText = []
    index = len(wordsList) - 1
    for conversely in range(len(wordsList)):
        converselyWordsText.extend([wordsList[index]])
        index -= 1
    resultMessage (" ".join (converselyWordsText))
    printLine ()
    menu (text)

def outputByWordNumber (text):
    printLine ()
    print (f"There are only {len(splitting(text))} words in the string")
    wordNumber = int(input("Input word number: "))
    if wordNumber > len(splitting(text)):
        printLine ()
        error ("Your number incorrect")
        outputByWordNumber (text)
    else:
        printLine ()
        resultMessage (wordsListToWordsDict (wordNumber, text))
        printLine ()
    outputWordMore = input("Do you want output word more? (y/n) ")
    match outputWordMore:
        case "y" | "Y":
            outputByWordNumber (text)
        case "n" | "N":
            printLine ()
            menu (text)
def wordsListToWordsDict (wordNumber, text):
    wordsList = splitting (text)
    wordsDict = {}
    wordsListIndex = 0
    for index in range(1,len(wordsList)+1):
        wordsDict[index] = wordsList[wordsListIndex]
        wordsListIndex += 1
    return (wordsDict.get(wordNumber))

def inputStringAgain ():
    printLine ()
    main ()

def exitProgram ():
    printLine ()
    sys.exit ("Exit the program. Thank you for using :)")

def menu (text):
    print (menuList ())
    functionNumber = input ("Choose the function number you want: ")
    match functionNumber:
        case "1":
            sortText (text)
        case "2":
            countElements (text)
        case "3":
            vowelsOrConsonants (text)
        case "4":
            converselyText (text)
        case "5":
            outputByWordNumber (text)
        case "6":
            inputStringAgain ()
        case "7":
            exitProgram ()
        case _:
            printLine ()
            error ("Your number incorrect")
            printLine ()
            menu (text)
main ()