# tuples are essentially immutatable lists, although they are slightly faster and use less memory than lists

my_tuple = ("Critical thinking", 1885, "Some Thinker", "Some gerne")

# tuple elements are accessed in the same way as list elements; with square brackets and index numbers

# print(my_tuple[3])

## destructuring or unpacking a tuple

# title, year, author, gerne = my_tuple

# print("Title: {}\nYear: {}\nAuthor: {}\nGerne: {}".format(title, year, author, gerne))

# partial unpacking

# title, year, *other = my_tuple
# print(f"{title}, {year} {other}")


employee_records = [
    ("Yuji", "Itadori", "Jujutsu socerer", 12345),
    ("Gojo", "Saturo", "Jujutsu master", 54321),
]

for name, surname, *other in employee_records:
    print(f"{name}, {surname}, {other}")