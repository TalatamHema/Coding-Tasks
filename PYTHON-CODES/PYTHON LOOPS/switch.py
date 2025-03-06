def check_even_odd(num):
    switch = {
        0: "Even",
        1: "Odd"
    }
    print(f"{num} is {switch[num % 2]}.")

# Example usage:
num = int(input("Enter a number: "))
check_even_odd(num)
