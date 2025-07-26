# looping || repetition

#for loop: -> starting point && condition && increemt or decrement

# prospect database
names = ["Will", "Leo", "Kate", "Kilian", "fsafdsmbom", "fasfsdfambom", "afdsfasmbom"]

#without loops-----gross
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

# with for loop
# for name in names:
#     # print(name)
#     if name.endswith("mbom"):
#         print(f"We dan catch you: {name}")
#     else:
#         print(f"Welcome to the party: {name}")


# exercise
#wrange
# for i in range(len(names)):
#     print(f"{i+1} {names[i]}")

# without range
# count = 1
# for name in names:
#     print(f"{count} {name}")
#     count += 1


# range function
# runs from 0 to n-1
# for i in range(5):
#     print(i)


# #runs from 2 to 7
# for i in range(2, 7):
#     print(i)

# # runs from 2 to 10 with an increment of 2
# for i in range(0, 10, 2):
#     print(i)


# # countdown
# for i in range(10, 0, -1):
#     print(i)


#while loops

# count = 1
# while count <= 5:
#     print(f"Count is: {count}")
#     count += 1


#user input
# user_input = ""
# while user_input != "quit":
#     user_input = input("Enter 'quit' to exit: ")
#     if user_input != "quit":
#         print(f"You entered: {user_input}")
# print("Goodbye")


# loop control statements

# print("Finding the first even number")
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f"First even number found: {i}")
#         break
#     print(f"{i} is odd")


# printing only odd numbers

# for i in range(1, 10):
#     if i % 2 == 0:
#         continue


# nested loops

# multiplication table

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")
#     print()


# lame triangle
# for i in range(1, 6):
#     print("*" * i)


# pattern printing

# print("Triangle pattern:")
# for row in range(1, 6):
#     for star in range(row):
#         print("*", end="")
#     print()






# equilateral triangle

rows = int(input("Number of rows: "))
for i in range(rows):
    for j in range(rows + i):
        if j < rows - i + 1:
            print("  ", end="")
            continue
        print("* ", end="")
    print()