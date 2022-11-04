text = input("Input text: ")
uniqueText = set(text)
lettersCount = []

for letters in uniqueText:
    count = 0
    for eachLetters in text:
        if letters == eachLetters:
            count+=1
    lettersCount.extend([letters + " - " + str(count)])




lettersCountString = ", ".join(lettersCount)
print("Count of letters in text: " + lettersCountString + "\n")

lettersCount.sort()
sortedByLetters = ", ".join(lettersCount)
print ("Sorted text by letters: " + sortedByLetters + "\n")

lettersCountSortedByAmount = []
for letters in uniqueText:
    count = 0
    for eachLetters in text:
        if letters == eachLetters:
            count+=1
    lettersCountSortedByAmount.extend([str(count) + " - " + letters])

lettersCountSortedByAmount.sort(reverse = True)
sortedByAmount = ", ".join(lettersCountSortedByAmount)
print ("Sorted text by amount of letters: " + sortedByAmount)