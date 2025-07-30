# declaration
phone_book = {
    "The Man": "1234567",
    "Baracks": "0876543",
    "Dungeon": "7655654"
}

text = "good $bad home  house!"
words = text.split()
for word in words:
    print(word.strip("!$"))

print(words)