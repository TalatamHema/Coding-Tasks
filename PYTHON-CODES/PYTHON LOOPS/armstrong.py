def is_armstrong(num):
    sum_of_digits = sum(int(digit) ** len(str(num)) for digit in str(num))
    return num == sum_of_digits

# Example usage:
num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
