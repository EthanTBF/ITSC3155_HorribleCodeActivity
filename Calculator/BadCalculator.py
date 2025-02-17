# Simple Calculator - Bad Practices

print("Simple Calculator")
print("Operations: add, subtract, multiply, divide")

operation = input("Enter Operation (add, subtract, multiply, divide): ")
operation = operation.strip()
operation = operation.lower()

if operation != 'add' and operation != 'subtract' and operation != 'multiply' and operation != 'divide':
    print("Invalid Operation")
else:
    if operation == 'add':
        num1 = input("Enter first number: ")
        if num1.isalpha():
            print("Invalid input. Please enter a valid number.")
        else:
            num2 = input("Enter second number: ")
            if num2.isalpha():
                print("Invalid input. Please enter a valid number.")
            else:
                num1 = float(num1)
                num2 = float(num2)
                print("Result:", num1 + num2)
    if operation == 'subtract':
        num1 = input("Enter first number: ")
        if num1.isalpha():
            print("Invalid input. Please enter a valid number.")
        else:
            num2 = input("Enter second number: ")
            if num2.isalpha():
                print("Invalid input. Please enter a valid number.")
            else:
                num1 = float(num1)
                num2 = float(num2)
                print("Result:", num1 - num2)
    if operation == 'multiply':
        num1 = input("Enter first number: ")
        if num1.isalpha():
            print("Invalid input. Please enter a valid number.")
        else:
            num2 = input("Enter second number: ")
            if num2.isalpha():
                print("Invalid input. Please enter a valid number.")
            else:
                num1 = float(num1)
                num2 = float(num2)
                print("Result:", num1 * num2)
    if operation == 'divide':
        num1 = input("Enter first number: ")
        if num1.isalpha():
            print("Invalid input. Please enter a valid number.")
        else:
            num2 = input("Enter second number: ")
            if num2.isalpha():
                print("Invalid input. Please enter a valid number.")
            else:
                num1 = float(num1)
                num2 = float(num2)
                print("Result:", num1 / num2)
