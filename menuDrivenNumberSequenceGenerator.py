# ||||||Menu Number Sequence Generator |||||

menu_selection = input("\nMENU NUMBER SEQUENCE GENERATOR\n||E = Even Numbers| |O = Odd Numbers| |S = Square Numbers|\
|Q = Quit|\n").upper()

while menu_selection != "Q":

    if menu_selection == "E":
        print("Even numbers between 1st input and 2nd input\n")
        x = int(input("Please enter first number:"))
        y = int(input("Please enter second number:"))

        if x % 2 == 1:
            x += 1

        for i in range(x, y + 1, 2):
            print(i, end=' ')
        print()
        menu_selection = input("\nMENU NUMBER SEQUENCE GENERATOR\n||E = Even Numbers| |O = Odd Numbers| |S = Square Numbers|\
|Q = Quit|\n").upper()

    elif menu_selection == "O":
        print("\nOdd numbers between 1st input and 2nd input\n")
        x = int(input("Please enter first number:"))
        y = int(input("Please enter second number:"))

        if x % 2 == 0:
            x += 1

        for i in range(x, y + 1, 2):
            print(i, end=' ',)
        print()
        menu_selection = input("\nMENU NUMBER SEQUENCE GENERATOR\n||E = Even Numbers| |O = Odd Numbers| |S = Square Numbers|\
|Q = Quit|\n").upper()

    elif menu_selection == "S":
        print("\nSquare numbers between 1st input and 2nd input\n")
        x = int(input("Please enter first number:"))
        y = int(input("Please enter second number:"))

        square = x
        for i in range(x - 1, y):
            square = (x + i) ** 2
            print(square, end=' ')
        print()
        menu_selection = input("\nMENU NUMBER SEQUENCE GENERATOR\n||E = Even Numbers| |O = Odd Numbers| |S = Square Numbers|\
|Q = Quit|\n").upper()
    else:
        print("Wrong menu selection, please choose again")
        menu_selection = input("\nMENU NUMBER SEQUENCE GENERATOR\n||E = Even Numbers| |O = Odd Numbers| |S = Square Numbers|\
|Q = Quit|\n").upper()


# # Show even numbers between x and y
#
# print("Even numbers between 1st input and 2nd input\n")
# x = int(input("Please enter first number:"))
# y = int(input("Please enter second number:"))
#
# if x % 2 == 1:
#     x += 1
#
# for i in range(x, y + 1, 2):
#     print(i, end=' ')
# print()
#
# # Show odd numbers between x and y
#
# print("\nOdd numbers between 1st input and 2nd input\n")
# x = int(input("Please enter first number:"))
# y = int(input("Please enter second number:"))
#
# if x % 2 == 0:
#     x += 1
#
# for i in range(x, y + 1, 2):
#     print(i, end=' ')
# print()
#
# # Show squares from x to y
#
# print("\nSquare numbers between 1st input and 2nd input\n")
# x = int(input("Please enter first number:"))
# y = int(input("Please enter second number:"))
#
# square = x
# for i in range(x - 1, y):
#     square = (x + i) ** 2
#     print(square, end=' ')
# print()