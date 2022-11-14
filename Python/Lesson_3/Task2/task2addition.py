def menuList ():
    return ('''[1] - Sort the string
[2] - Count the number of elements
[3] - Display only vowels or consonats
[4] - Output the string from the end
[5] - Output the word by word number
[6] - Input the string again
[7] - Exit the program
''')

def splitting (text):
    return text.split(" ")

def printLine ():
    print ("======================================")

def resultMessage (result):
    print ("RESULT: " + str(result))

def error (errorMessage):
    print ("ERROR: " + errorMessage)