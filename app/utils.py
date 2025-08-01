def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n-1)
