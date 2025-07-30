import random

# fizz buzz game

# n = int(input("Enter n: "))
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz ")
#     elif i % 5 == 0:
#         print("buzz ")
#     elif i % 3 == 0:
#         print("fizz ")
#     else:
#         print(f"{i} ")


# swap

# a = 5
# b = 6
# print(f"Before a: {a}, b: {b}")
# c = a
# a = b
# b = c
# print(f"After a: {a}, b: {b}")


# guessing game
print("*************WELCOME TO GUESSING GAME***************\n")
target = random.randint(1, 20)
print(target)
for i in range (3):
    guess = int(input("Guess a number between 1 and 20(inclusive): "))
    
    if guess > target:
        print("Sorry, your guess is greater than the target, try again\n")
    elif guess < target:
        print("Sorry, your guess is less than the target, try again\n")
    else:
        print(f"You win baby! {guess} is the correct number!")
        break
    
    if(i == 2):
        print(f"Sorry you failed!\nTarget was {target}")





