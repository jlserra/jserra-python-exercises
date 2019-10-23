
user_input = raw_input('Enter a number to know whether it is odd or even: ')

try:
    if (int(user_input) % 2) == 0:
        print "The number you have entered is even."
    else:
        print "The number you have entered is odd."
except ValueError:
    print "Invalid value entered. Whole Numbers only."