"""
Pass Word validator
"""
SPECIALS = "!@#$%^&*()_-­‐=+`~,./o'[]\<>?O{}|"
LOWEST_LENGTH = 5
HIGHEST_LENGTH = 15

lower_case = 0
upper_case = 0
special_characters = 0

user_password = input("Please enter a valid input\n Your Password must be between 5 and 15 characters, and contain: \n\
\t 1 or more uppercase characters\n\t 1 or more lowercase characters\n\t one or more numbers\n\
\t and 1 or more special characters:  !@#$%^&*()_-­‐=+`~,./o'[]\<>?O|\n")

# for c in user_password:
#     if LOWEST_LENGTH < len(user_password) < HIGHEST_LENGTH:
#         if c.islower():
#             lower_case += 1
#         elif lower_case < 1:
#             print("Invalid Password")
#         elif c.isupper():
#             upper_case += 1
#         elif upper_case < 1:
#             print("Invalid Password")
#         elif SPECIALS in user_password:
#             special_characters += 1
#         elif special_characters < 1:
#             print("Invalid Password")
#     print("Invalid Password")
# print("Your", len(user_password), "character password is valid:", user_password)
#
#
# # while LOWEST_LENGTH < len(user_password) < HIGHEST_LENGTH:
# #
# # print("Your" + len(user_password) + "character password is valid:", user_password )

for c in user_password:
        if c.islower():
            lower_case += 1
        elif c.isupper():
            upper_case += 1
        elif SPECIALS in user_password:
            special_characters += 1

if LOWEST_LENGTH < len(user_password) < HIGHEST_LENGTH and lower_case >= 1 and upper_case >= 1:
    print("Your", len(user_password), "character password is valid:", user_password)
else:
    print("Invalid password")
