"""
Pass Word validator
"""
SPECIALS = "!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|"
LOWEST_LENGTH = 5
HIGHEST_LENGTH = 15

lower_case = 0
upper_case = 0
special_characters = 0
numbers = 0

user_password = input("Please enter a valid input\n Your Password must be between 5 and 15 characters, and contain: \n\
\t 1 or more uppercase characters\n\t 1 or more lowercase characters\n\t one or more numbers\n\
\t and 1 or more special characters:  !@#$%^&*()_-­‐=+`~,./o'[]\<>?O|\n")


for character in user_password:
        if character.islower():
            lower_case += 1
        elif character.isupper():
            upper_case += 1
        elif character in SPECIALS:
            special_characters += 1
        elif character.isnumeric():
            numbers += 1


if LOWEST_LENGTH <= len(user_password) <= HIGHEST_LENGTH and lower_case >= 1 and upper_case >= 1 and special_characters \
        >= 1 and numbers >= 1:
    print("Your {} character password is valid: {}".format(len(user_password), user_password))
else:
    print("Invalid password")
