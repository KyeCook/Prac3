try:
    numerator= int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator/denominator
except ValueError:
    print("Numerator and denominator must be valid numbers")
except ZeroDivisionError:
    print("Cannot devide by zero!")
print("Finished")

# ---- QUESTIONS -----
# 1) This error will occur when the input is not of the same datatype as integer.
# 2) This error will occur when the user attempts to add a zero in the denominator
# 3) To eliminate the possibility of this error, the users input could be error
#    checked to ensure no 0's are entered