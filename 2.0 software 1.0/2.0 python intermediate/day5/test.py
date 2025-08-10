# python record book
from datetime import datetime

print("******* Python Record Book ********/n/n")

try:
    with open("./record.txt", "w") as file:
        file.write("\n******** RECORD BOOK ********\n\n")
        file.write(f"Today's date: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n")
        while True:
            lesson = input("\nWhat did you learn in python today?\n(enter 'exit' to quit) ")
            if lesson.lower() != "exit":
                file.write(f"\n{lesson}\n")
            else:
                break
        print("\n\nSaving today's work")

except FileNotFoundError:
    print("File not found")
