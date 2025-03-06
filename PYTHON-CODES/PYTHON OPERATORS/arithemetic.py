def arithmetic_operation(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b if b != 0 else "Division by zero error"
    else:
        return "Invalid operator"
result = arithmetic_operation(10, 5, '+')
print(result) 