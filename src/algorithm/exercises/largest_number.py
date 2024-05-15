# Defining a function to find the largest number in the list
def find_largest_number(lst):
    largest = lst[0]

    for num in lst:
        if num > largest:
            largest = num
    
    return largest

# Example 
numbers = [5, 9, 2, 15, 3, 7]
largest_number = find_largest_number(numbers)
print("The largest number in the list is:", largest_number)
