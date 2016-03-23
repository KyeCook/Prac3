"""
Using files with programming
writing and reading textfiles
"""

# -------------- Task 1 -- Writing ------------------------

# user_name = input("Enter name:")
# file = open('name.txt', 'w')
# file.write(user_name + '\n')
# file.close()

# --------------- Task 2 -- Reading/printing  -------------

# file = open('name.txt', 'r')
# names = file.read()
# print("Your name is", names)
# file.close()

# --------------- Task 3 -- Reading/adding ----------------

file = open("numbers.txt", 'r')
lines = file.readlines()
number_1 = lines[0]
number_2 = lines[1]

total = int(number_1) + int(number_2)
print(total)
file.close()




