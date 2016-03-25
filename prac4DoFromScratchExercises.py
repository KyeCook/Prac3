"""
Task - Add function for following :
                    a) Calculating the area of a rectangle
                    b) Converting Celsius to Fahrenheit
                    c) Calculating Body Mass Index
"""


def main():
    length, height = get_values()
    print("Area = {}cm x {}cm".format(length, height))
    area = calculations(length, height)
    print("Therefore area = {}cm^2".format(area))


def get_values():
    length = float(input("Enter Length:"))
    height = float(input("Enter Height:"))

    return length,height


def calculations(length,height):
    area_of_rectangle = length * height
    return int(area_of_rectangle)

main()