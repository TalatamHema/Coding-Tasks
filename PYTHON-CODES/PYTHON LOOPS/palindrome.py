def is_palindrome(num):
    return str(num) == str(num)[::-1]  # Check if the number is the same when reversed

# Example usage:
num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
