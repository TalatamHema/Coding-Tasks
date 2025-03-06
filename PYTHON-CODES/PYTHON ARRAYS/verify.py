def contains_elements(arr, elem1=12, elem2=23):
    return elem1 in arr and elem2 in arr  # Check if both elements exist

# Example usage:
numbers = [10, 12, 15, 23, 30, 40]
result = contains_elements(numbers)

print("Array contains both 12 and 23:", result)
