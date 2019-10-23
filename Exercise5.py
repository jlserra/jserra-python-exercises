option = 0


def isLetter(letter):
    booleanIsLetters = True

    for val in "1234567890":
        if val == letter:
            booleanIsLetters = False
        else:
            continue

    return booleanIsLetters


def exercise1():
    print "Exercise 1:"
    i = 0
    while i < 6:
        i += 1
        if i == 3 or i == 6:
            continue
        print(i)


def exercise2():
    print "Exercise 2:"
    i = 0
    while i < 4:
        letter = raw_input("Enter letter to know if it is a vowel or consonant: ")
        i += 1
        try:
            if len(letter) == 1 and isLetter(letter):
                if letter.lower() == "a" or letter.lower() == "e" or letter.lower() == "i" or letter.lower() == "o" or letter.lower() == "u":
                    print letter, "is a vowel"
                else:
                    print letter, "is a consonant"
            else:
                print "invalid letter entered"
        except ValueError:
            print "invalid letter entered"


def invalidValue():
    print "Invalid value selected"


def menuSwitch(program):
    switcher = {
        "1": exercise1,
        "2": exercise2,
        "3": exit
    }

    switcher.get(program, invalidValue)()


while option != 3:
    try:
        option = raw_input(
            "Enter program you want to run! \n 1.) Exercise #1 \n 2.) Exercise #2 \n 3.) Exit \n Enter Option: ")
        menuSwitch(option)
    except ValueError:
        print "Invalid value selected"
