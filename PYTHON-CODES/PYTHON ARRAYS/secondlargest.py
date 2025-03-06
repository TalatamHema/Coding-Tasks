def second_largest(arr):
    unique_numbers = list(set(arr))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None  # Return None if there is no second largest
    unique_numbers.sort(reverse=True)  # Sort in descending order
    return unique_numbers[1]  # Return the second element

# Example usage:
numbers = [10, 20, 30, 40, 50, 50, 30]
result = second_largest(numbers)

if result is not None:
    print("Second largest number:", result)
else:
    print("No second largest number found.")
