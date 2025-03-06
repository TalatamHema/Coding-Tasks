def remove_duplicates(arr):
    return list(set(arr))  # Convert to set to remove duplicates, then back to list

# Example usage:
numbers = [10, 20, 30, 10, 40, 50, 20, 30]
unique_numbers = remove_duplicates(numbers)

print("Array after removing duplicates:", unique_numbers)
