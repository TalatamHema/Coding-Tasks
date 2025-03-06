def find_common_values(arr1, arr2):
    return list(set(arr1) & set(arr2))  # Find intersection using set

# Example usage:
array1 = [10, 20, 30, 40, 50]
array2 = [30, 50, 70, 90, 10]

common_values = find_common_values(array1, array2)
print("Common values:", common_values)
