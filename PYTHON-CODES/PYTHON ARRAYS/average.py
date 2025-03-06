def average_of_array(arr):
    if len(arr) == 0:
        return 0  # Avoid division by zero
    return sum(arr) / len(arr)  # Calculate average

# Example usage:
numbers = [10, 20, 30, 40, 50]
print("Average of array:", average_of_array(numbers))
