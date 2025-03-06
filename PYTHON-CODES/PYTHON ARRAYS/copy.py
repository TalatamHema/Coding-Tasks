def copy_array(arr):
    return arr[:]  # Creates a copy using slicing

# Example usage:
original_array = [10, 20, 30, 40, 50]
copied_array = copy_array(original_array)

print("Original array:", original_array)
print("Copied array:", copied_array)
