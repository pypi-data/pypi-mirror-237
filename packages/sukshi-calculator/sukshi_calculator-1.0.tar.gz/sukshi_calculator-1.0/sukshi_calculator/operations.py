# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"

# Example Usage
a = 10
b = 5

# print("Sum:", add(a, b))  # Output: Sum: 15
# print("Difference:", subtract(a, b))  # Output: Difference: 5
# print("Product:", multiply(a, b))  # Output: Product: 50
# print("Division:", divide(a, b))  # Output: Division: 2.0
