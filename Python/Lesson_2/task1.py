text = input("Input text: ")
uniqueText = set(text)
lettersCount = {}

for unique in uniqueText:
    lettersCount[unique] = text.count(unique)
print ("Count of letters: " + str(lettersCount) + "\n")

print ("Sorted by letters: " + str(sorted(lettersCount.items())))
print ("Sorted by amount: " + str(sorted(lettersCount.items(), key = lambda x: x[1], reverse = True)))
