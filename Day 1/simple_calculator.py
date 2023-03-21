"""
AUTHOR: Mary Grizelle Hamor
DESCRIPTION: This program is a simple command-line calculator.
"""

def main(): 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Operations:\n" \
        "+ : Addition\n" \
        "- : Subtraction\n" \
        "* : Multiplication\n" \
        "/ : Division\n" \
        "^ : Power\n")

    op = input("Your chosen operation: ")

    if op in ['+', '-', '*', '/', '^']:
        if op == '+':
            add(a,b)
        elif op == '-':
            subtract(a,b)
        elif op == '*':
            multiply(a,b)
        elif op == '/':
            divide(a,b)
        else:
            power(a,b)
    else:
        print("WARNING: You have chosen an invalid operation")

def add(a, b):
    result = a + b
    print("\nOutput:\n" \
        f"{a} + {b} = {result}")

def subtract(a, b):
    result = a - b
    print("\nOutput:\n" \
        f"{a} - {b} = {result}")

def multiply(a, b):
    result = a * b
    print("\nOutput:\n" \
        f"{a} * {b} = {result}")

def divide(a, b):
    result = a / b
    print("\nOutput:\n"
        f"{a} / {b} = {result}")

def power(a, b):
    result = a ** b
    print("\nOutput:\n" \
        f"{a}^{b} = {result}")

if __name__ == "__main__":
    main()