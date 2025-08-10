
def average_check(array, target):
    sum_total = 0
    length = 0
    target_seen = False
    
    for number in array:
        sum_total += number
        length += 1
        
        if target == number:
            target_seen = True
    
    message = "Seen" if target_seen else "Unseen"

    average = sum_total / length

    return f"Average: {average:.2f}, Target Status: {message}"
    

nums = [2, 5, 10, 6]
print(average_check(nums, 10))