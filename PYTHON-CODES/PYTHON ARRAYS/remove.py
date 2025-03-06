def remove_element(arr, value):
    if value in arr:
        arr.remove(value)  # Removes the first occurrence of the value
    return arr

# Example usage:
numbers = [10, 20, 30, 40, 50]
element = int(input("Enter element to remove: "))

updated_array = remove_element(numbers, element)
print("Updated array:", updated_array)
