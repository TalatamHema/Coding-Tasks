def difference_max_min(arr):
    if not arr:
        return None  # Handle empty array case
    return max(arr) - min(arr)  # Calculate difference

# Example usage:
numbers = [10, 20, 5, 40, 50]
difference = difference_max_min(numbers)

print("Difference between largest and smallest value:", difference)
