# password = input("Enter your password: ")
# lower_case = password.islower()
# upper_case = password.isupper()
# numeric = password.isdigit()

# if lower_case and upper_case and numeric:

# password = input("Enter your password: ")

# is_upper = False
# is_lower = False
# is_digit = False

# for letter in password:
#     if is_upper == is_lower == is_digit == True:
#         break
#      if(letter.isupper()):
#          is_upper = True
#      if(letter.islower()):
#          is_lower = True
#      if(letter.isdigit()):
#          is_digit = True
# if is_upper and is_lower and is_digit :
#     print("Strong password")
# else:
#     print("Weak password")


l = False
u = False
d = False

password = input("Enter your password: ")

for letter in password:
    if letter.islower():
        l = True
    elif letter.isupper():
        u = True
    elif letter.isdigit():
        d = True

if l and u and d:
    print("Strong password")
else:
    print("Weak password")