finished = False
result = 0
while not finished:
    try:
        result = input(int("Enter a number"))
        finished = True
    except ValueError:
        print("Please  enter  a  valid  integer.")
print("valid  result  is", result)
