text = input("Entire your string: ").lower()
lettersDict = {}

def lettersCount(position, lettersDict):
    if len(text) > position:
        try:
            lettersDict[text[position]] += 1
        except:
            lettersDict[text[position]] = 1
        return lettersCount(position + 1, lettersDict)
    else:
        print(lettersDict)

lettersCount(0, lettersDict)