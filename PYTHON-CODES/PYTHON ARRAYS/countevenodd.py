def count_even_odd(arr):
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = len(arr) - even_count  # Total length - even count gives odd count
    return even_count, odd_count

# Example usage:
numbers = [10, 15, 20, 25, 30, 35, 40, 45]
even_count, odd_count = count_even_odd(numbers)

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
