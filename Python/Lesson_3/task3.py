text = input("Entire your string: ").lower()
lettersDict = {}

def equatingToOne(position):
    if len(text) > position:
        lettersDict[text[position]] = 0
        return equatingToOne(position + 1)
    else:
        return lettersDict

def lettersCount(position, lettersDict):
    if position == 0:
        equatingToOne(0)
    if len(text) > position:
        lettersDict[text[position]] += 1
        return lettersCount(position + 1, lettersDict)
    else:
        print(lettersDict)

lettersCount(0, lettersDict)