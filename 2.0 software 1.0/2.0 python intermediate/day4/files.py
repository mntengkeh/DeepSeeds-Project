# def read_simple_file():
#     """demo for file read"""
#     file = open("./sample.txt", "r")
#     content = file.read()
#     print(file)
#     print(f"Here is the content of the file read: {content}")
#     file.close()
#     return content


# read_simple_file()

# def eff_read_simple_file():
#     try:
#         with open("sample.txt", "r") as file:
#             return file.read()
#     except FileNotFoundError:
#         return "File not found dude, please try again"
    
# print(eff_read_simple_file())

def lbl_read_sample_file():
    try:
        with open("sample.txt", "r") as file:
            print("\nReading line by line")
            for i, line in enumerate(file, 1):
                print(f"\nLine {i}: {line.strip()}")
    except FileNotFoundError:
        pass

lbl_read_sample_file()

