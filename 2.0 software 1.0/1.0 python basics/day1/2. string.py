# # concatenation
# first_name = "first_name"
# last_name = "last_name"
# full_name = first_name + last_name
# print(full_name)

# # repetition 
# laugh = "Ha" * 3
# print(laugh)

# # string length
# name = "Hello, Python!"
# name_length = len(name)

# # string formating for interpollation
# name = "Alice"
# age = 30
# score = 95.5

# #method 1: f-strings (recommended)
# print(f"Hello, {name}! You are {age} years old.")
# print(f"Your score is {score:.1f}%")

# #method 2: .format() method
# print("Hello, {}! You are {} years old.".format(name, age))

# #method3: the % formater(older syntax)
# print("Hello %s, you are %d years old" % (name, age))

#simple email validator

# email = input("Enter email: ")
# if "@" in email and "." in email:
#     usrname = email.split("@")[0]
#     domain = email.split("@")[1]
#     print("Username : %s" % (usrname))
#     print("Domain: {}".format(domain))
# else:
#     print("Invalid email")




# ex 1: name formarter
# name = "jOhN dOe"
# print(name.title())
# print("Firt name: %s, Last name: %s" % (name.split()[0], name.split()[1])) 

# ex 2: word counter
# sentence = "Python is an amazing programming language"
# number_of_words = len(sentence.split())
# number_of_characters = len(sentence)
# count = sentence.count("a")

# print("Number of words : {}\nNumber of characters: {}\nNumber of a's: {}".format(number_of_words, number_of_characters, len(count)))


# ex 3: simple cipher
# letters = []
# for i in range(26):
#     letters.append(chr(ord('a') + i))

# plaintext = input("Enter plaintext: ")
# ciphertext = []
# for i in plaintext:
#     index = ord(i) - 97 + 1
#     ciphertext.append(letters[index % 26])
# print("".join(ciphertext))



# 24 july
# string methods 


#converting from lowercase to uppercase and vice versa

# message = "Good morning"
# message_lower = message.lower()
# message_upper = message.upper()
# print(f"The lowercase xonversion is: {message_lower} and uppercase conversion is {message_upper}")


# slice method

# greeting = "welcome back"
# how_python_sees_it = list(greeting)
# print(f"Python view: {how_python_sees_it}")
# extract_text = greeting[0:3]
# print(f"Extracted text: {extract_text}")


# strip and replace methods

# message2 = " Welcome back home   "
# print(message2.strip())

# new_message = message2.replace("Welcome", "go")
# print(new_message)



#string exercises
name = "jOhN dOe"
j = name[0].upper()
d = name[5].upper()
print(f"Full name: {j}{name[1:4].lower()} {d}{name[6:8].lower()}")