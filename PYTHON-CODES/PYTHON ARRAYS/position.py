def insert_element(arr, value, position):
    arr.insert(position, value)  # Inserts value at the given index
    return arr

# Example usage:
numbers = [10, 20, 30, 40, 50]
element = int(input("Enter element to insert: "))
position = int(input("Enter position (index) to insert at: "))

updated_array = insert_element(numbers, element, position)
print("Updated array:", updated_array)

