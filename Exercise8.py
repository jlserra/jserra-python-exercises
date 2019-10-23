
file_path = ""

try:
    with open(file_path, 'w') as f:
        f.write("test")
except IOError as e:
    print ("Error catched : IOError", e)

arrays = [1, 2, 3, 4, 5]

try:
    print(arrays[5])
except IndexError as e:
    print ("Error catched : IndexError", e)


ages = {'One': 1, 'Two': 2, 'Three': 3}

try:
    print(ages['Four'])
except KeyError as e:
    print ("Error catched : KeyError", e)

try:
    print name
except NameError as e:
    print ("Error catched : NameError", e)

count = 69

try:
    print(len(count))
except TypeError as e:
    print ("Error catched : TypeError", e)

value = "text"

try:
    print(int(value))
except ValueError as e:
    print ("Error catched : ValueError", e)

try:
    print(1/0)
except ZeroDivisionError as e:
    print ("Error catched : ZeroDivisionError", e)

