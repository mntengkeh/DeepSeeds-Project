# body mass index calculator
# weight = float(input("Eneter weight(kg): "))
# height = float(input("Enter height(m): "))

# print(f"BMI: {weight / (height * height)}")

# function with neither input  nor output
# bmi with fxn without input

# def bmi_calculator():
#     weight = float(input("Eneter weight(kg): "))
#     height = float(input("Enter height(m): "))
#     bmi = weight / (height ** 2)
#     # print(f"BMI: {bmi}")
#     if bmi < 18:
#         print("underweight")
#     elif bmi < 25:
#         print("normal weight")
#     elif bmi < 30:
#         print("overweight")
#     else:
#         print("Fat man")


# print(bmi_calculator())

# function with input
# bmi with function accepting input
def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    print(bmi)

weight = float(input("Eneter weight(kg): "))
height = float(input("Enter height(m): "))
bmi_calculator(weight, height)




# funcion with output

def bmi(w, h):
    return w/h*h