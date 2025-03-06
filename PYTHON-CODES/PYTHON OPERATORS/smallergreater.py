def relational_operators(a, b):
    print(f"{a} < {b}: {a < b}")
    print(f"{a} <= {b}: {a <= b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} >= {b}: {a >= b}")
    
    smaller = min(a, b)
    larger = max(a, b)
    
    print(f"Smaller number: {smaller}")
    print(f"Larger number: {larger}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

relational_operators(num1, num2)
