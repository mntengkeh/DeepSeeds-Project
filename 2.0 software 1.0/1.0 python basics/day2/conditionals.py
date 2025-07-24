# if - else pair

# eligiblility for voting application

# age = int(input("Please enter your age: "))"".join(ciphertext)
# if age > 18:
#     print("Yes you can vote")
# else:
#     print("Please wait for next year")


# excercise: take a person's age, check if they are more than 16, if yes, they can play in the basket ball team

# e_age = int(input("Please enter your age: "))
# if age > 16:
#     print("You are eligible for the basketball team")
# else:
#     print("You ain't eligible")


# if - elif - else chain
# school grading system

# score = float(input("Enter your score: "))

# if score > 80 : 
#     print("You got an A")
# elif score >= 70:
#     print("You got a B+")
# elif score >= 60:
#     print("You got a B")
# elif score >= 50:
#     print("You got a C")
# elif score >= 40:
#     print("You got a D")
# else:
#     print("Banished from this land")





#cl
# expression = input("Enter expression: ")
# tns = list(expression)
# print(tns)
# operation = tns[1]

# match operation:
#     case '+':
#         print(f"result: {float(tns[0]) + float(tns[2])}")
#     case '-':
#         print(f"result: {float(tns[0]) - float(tns[2])}")
    
# simple calculaor
# first_number = float(input("Enter first number: "))
# second_number = float(input("Enter second number: "))
# operator = input("Enter operator: ")

# if operator == "+":
#     print(f"Result = {first_number + second_number}")
# elif operator == "-":
#     print(f"Result = {first_number - second_number}")
# elif operator == "/":
#     if second_number == 0:
#         print("Can't divide by zero ain't allowed")
#     else:
#         print(f"Result = {first_number / second_number}")
# elif operator == "*":
#     print(f"Result = {first_number * second_number}")



# leap year exercise

# year = int(input("Enter year: "))


# if year % 400 == 0:
#     print("leap year")
# else:
#     if year % 4 == 0:
#         if year % 100 == 0:
#             print("not a leap year")
#         else:
#             print("leap year")

year = int(input("enter year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not leap")

# A year is leap if:
# - Divisible by 4 AND not divisible by 100
# - OR divisible by 400
# Test with years: 2000, 1900, 2024, 2023