"""
Initial Program
"""
# lower = 10
# upper = 100
#
# int(input("Enter a number ( {} - {}): ".format(lower,upper)))
# for i in range(10,  120,  11):    #  make  sure  we  have  integers  of  different  'length'
#     print("{}  {}".format(i,  chr(i)))
# ---- Program With Functions ----


def main():
    lower = 10
    upper = 100

    inputted_number = get_number(10, 100)
    print(inputted_number)

    # for i in range(10,  120,  11):    #  make  sure  we  have  integers  of  different  'length'
    #     print("{}  {}".format(i,  chr(i)))


def get_number(lower, upper):


    user_number = input("Enter a number ( {} - {}): ".format(lower, upper))
    while user_number.isnumeric() != True or int(user_number) < lower or int(user_number) > upper:
        print("Please Enter a Valid Number!")
        user_number = input("Enter a number ( {} - {}): ".format(lower, upper))
    return int(user_number)


def print_ascii():
    for i in range(10,  120,  11):    #  make  sure  we  have  integers  of  different  'length'
        print("{}  {}".format(i,  chr(i)))

main()