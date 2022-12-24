def cardNumberValidity(cardNumberList):
    cardNumberList.reverse()
    multiplyByTwoList = []
    for position in range(len(cardNumberList)):
        if position % 2 == 0:
            multiplyByTwoList.extend(cardNumberList[position])
            continue
        else:
            multiplyByTwoList.extend(str(int(cardNumberList[position]) * 2))

    numberForCheckValidity = 0
    for position in range(len(multiplyByTwoList)):
        numberForCheckValidity += int(multiplyByTwoList[position])

    cardNumberList.reverse()
    if numberForCheckValidity % 10 == 0:
        return True
    else:
        return False

def main():
    cardNumberLength = input("Entire credit card number: ")
    cardNumberList = list(cardNumberLength)
    if cardNumberValidity(cardNumberList) == True:
        if (len(cardNumberLength) == 13 or len(cardNumberLength) == 16) and cardNumberList[0] == "4":
            print ("VISA")
        elif len(cardNumberList) == 16 and cardNumberList[0] == "5":
            print ("MASTERCARD")
        elif len(cardNumberLength) == 15 and cardNumberList[0] == "3" and (cardNumberList[1] == "4" or cardNumberList[1] == "7"):
            print ("AMEX")
        else:
            print ("INVALID")
    else:
        print ("INVALID")

main()