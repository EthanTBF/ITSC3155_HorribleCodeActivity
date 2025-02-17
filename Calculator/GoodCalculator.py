# Simple Calculator - Good Coding Practice

def add(a,b): # Returns the sum of two numbers
    return a+b

def subtract(a,b): # Returns the difference of two numbers
    return a-b

def multiply(a,b): # Returns the product of two numbers
    return a*b

def divide(a,b): # Returns the quotient of two numbers, handling cases of division by 0
    if b == 0:
        raise ZeroDivisionError
    return a/b

def get_number(prompt):
    """Prompts the user for a number and ensures valid numeric input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")

    # User input for operation and numbers
    while True:
        operation = input("Choose an operation (add, subtract, multiply, divide): ").strip().lower()

        operations = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
            "divide": divide
        }

        if operation in operations:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            result = operations[operation](float(num1), float(num2))
            print("Result:", result)
            break
        else:
            print("Invalid operation")
            continue





if __name__ == '__main__':
    main()