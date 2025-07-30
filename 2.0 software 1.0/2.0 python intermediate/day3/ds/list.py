# creating lists

# shoppin_cart = ["apples", "bread", "milk", "eggs"]
# numbers = [1, 2, 3, 4, 5]
# mixed_items = ["Alice", 25, True, 3.14]
# empty_list = []


# print(f"Shopping cart: {shoppin_cart}")
# print(f"Numbers: {numbers}")
# print(f"Mixed items: {mixed_items}")

# accessing list items

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# # accessing items by index

# print(f"First item: {fruits[0]}")
# print(f"Second item: {fruits[1]}")
# print(f"Last item: {fruits[-1]}")

# # slicing lists

# print(f"items from index 1 - 3 inclusive {fruits[1:4]}")


# mutating lists


# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# fruits.append("mangoes")
# fruits.extend(["oranges", "avocado"])
# fruits.insert(0, "zzzzz")
# fruits.pop()
# fruits.pop(5)
# print(fruits)



#list methods

# scores = [64, 13, 54, 78, 98, 76, 59, 29, 31, 25, 72, 85]
# print(f"Reverse sorted scores: {sorted(scores, reverse=True)}")



# analyse numbers

def analyse_numbers(numbers):
    sm = sum(numbers)
    count = len(numbers)
    average = sm / count
    even_count = len([i for i in numbers if i % 2 == 0])
    odd_count = len([i for i in numbers if i % 2 == 1])

    return {
        "Sum": sm,
        "Average": average,
        "Min": min(numbers),
        "Max": max(numbers),
        "Even_count": even_count,
        "Odd_count": odd_count
    }


numbers = [2, 3, 3, 4, 5, 6, 5, 6, 8, 9]
print(analyse_numbers(numbers))