def find_index(arr, element):
    try:
        return arr.index(element)  # Get the index of the element
    except ValueError:
        return -1  # Return -1 if the element is not found

# Example usage:
numbers = [10, 20, 30, 40, 50]
element = int(input("Enter element to find: "))

index = find_index(numbers, element)
if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")
