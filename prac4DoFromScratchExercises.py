"""
Task - Add function for following :
                    a) Calculating the area of a rectangle
                    b) Converting Celsius to Fahrenheit
                    c) Calculating Body Mass Index
"""

# -- Task a) ---


# def main():
#     length, height = get_values()
#     print("Area = {}cm x {}cm".format(length, height))
#     area = calculations(length, height)
#     print("Therefore area = {}cm^2".format(area))
#
#
# def get_values():
#     length = float(input("Enter Length:"))
#     height = float(input("Enter Height:"))
#
#     return length,height
#
#
# def calculations(length,height):
#     area_of_rectangle = length * height
#     return int(area_of_rectangle)
#
# main()

# -- Task b) ---


# def main():
#     celsius = get_values()
#     fahrenheit = calculations(celsius)
#     print("Celsius Value = {0}c\nTherefore fahrenheit = {0}c x 9 / 5 + 32\n Thus\
#  converted Fahrenheit = {1}F".format(celsius, fahrenheit))
#
#
# def get_values():
#     celsius_value = float(input("Enter Celsius Value:"))

#     return celsius_value
#
#
# def calculations(celsius):
#     fahrenheit = celsius * 9 / 5 + 32

#     return fahrenheit
#
# main()

# -- Task C) ---


def main():
    weight, height = get_values()
    bmi = calculations(weight,height)
    print("BMI = Weight / Height^2\nTherefore BMI = {}kg / {}m^2\nBMI = {}".format(weight, height, bmi))


def get_values():
    weight = float(input("Enter Weight (kg):"))
    height = float(input("Enter Height  (m):"))

    return weight, height


def calculations(weight,height):
    bmi = weight/(height ** 2)

    return bmi

main()
