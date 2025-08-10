# number error

# def style():
#     print("_"*40)

# def number_error():
#     try:
#         style()
#         user_input = int(input("Please enter your phone number: "))
#         print(f"User input is {user_input}")
#     except:
#         print("Motherfucker")

# number_error()

# def division_error():
#     style()
#     try:
#         first_number = int(input("Enter first number: "))
#         second_number = int(input("Enter second number: "))
#         return first_number/second_number
#     except ZeroDivisionError:
#         print("Second number should be different from zero")

# division_error()

def dictionary_error(data):
    try:
        color = data["name"]
        print(f"Fav color: {color}")
    except KeyError:
        print("You are trying to access a property which isn't present on data")
    pass

data = {"name": "Delsy", "age": 17, "fav_mean":"rice"}
dictionary_error(data)