def find_min_max(arr):
    if not arr:
        return None, None  # Handle empty array case
    return min(arr), max(arr)  # Get min and max values

# Example usage:
numbers = [10, 20, 5, 40, 50]
minimum, maximum = find_min_max(numbers)

print("Minimum value:", minimum)
print("Maximum value:", maximum)
