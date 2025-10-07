def addition(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test the functions
if __name__ == "__main__":
    print("Add: 2 + 3 =", add(2, 3))
    print("Subtract: 5 - 2 =", subtract(5, 2))
    print("Multiply: 4 * 3 =", multiply(4, 3))
    print("Divide: 10 / 2 =", divide(10, 2))
