def find_duplicates(arr):
    duplicates = []
    seen = set()
    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        seen.add(num)
    return duplicates

# Example usage:
numbers = [10, 20, 30, 10, 40, 50, 20, 30]
duplicates = find_duplicates(numbers)

print("Duplicate values:", duplicates)
