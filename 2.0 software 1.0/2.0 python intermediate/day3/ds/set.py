# # stores unique items
# # Creating sets - like building unique collections
# unique_numbers = {1, 2, 3, 4, 5}
# colors = {"red", "blue", "green", "yellow"}
# mixed_set = {1, "hello", 3.14, True}

# # Creating sets from lists (removes duplicates automatically)
# numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
# unique_numbers_from_list = set(numbers_with_duplicates)

# # Empty set (note: {} creates an empty dictionary, not set)
# empty_set = set()

# print(f"Unique numbers: {unique_numbers}")
# print(f"Colors: {colors}")
# print(f"From list with duplicates: {unique_numbers_from_list}")
# print(f"Empty set: {empty_set}")



# # Student enrollment in different courses
# python_students = {"Alice", "Bob", "Charlie", "Diana"}
# java_students = {"Bob", "Charlie", "Eve", "Frank"}
# javascript_students = {"Charlie", "Diana", "Eve", "Grace"}

# # Union - students taking ANY programming course
# all_programming_students = python_students | java_students | javascript_students
# print(f"All programming students: {all_programming_students}")

# # Intersection - students taking BOTH Python AND Java
# python_and_java = python_students & java_students
# print(f"Students taking both Python and Java: {python_and_java}")

# # Difference - students taking Python but NOT Java
# python_only = python_students - java_students
# print(f"Students taking Python but not Java: {python_only}")

# # Symmetric difference - students taking Python OR Java but not both
# python_xor_java = python_students ^ java_students
# print(f"Students taking Python or Java but not both: {python_xor_java}")


my_set = {1, 2, 3, 4, 5}
print(my_set.pop())

