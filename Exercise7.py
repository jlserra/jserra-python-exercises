
inputText = raw_input("Enter String:")

letters = []

for char in inputText:
    if char.lower() not in letters:
        letters.append(char.lower())
        print "Letter occurence:", char.upper(), "-", inputText.count(char)

