finished = False
result = 0
while not finished:
    try:
        result = input("Enter a number")
        result = int(result)
    except ValueError:
        print("Please  enter  a  valid  integer.")
print("valid  result  is", result)
