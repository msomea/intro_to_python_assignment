# intro_to_python_assignment
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the Python assignment.")
number_1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
number_2 = float(input("Enter the second number: "))
# Perform the operation based on user input
if operation == '+':
    result = number_1 + number_2
    print(f"The result of {number_1} {operation} {number_2} is: {result}")
elif operation == '-':
    result = number_1 - number_2
    print(f"The result of {number_1} {operation} {number_2} is: {result}")
elif operation == '*':
    result = number_1 * number_2
    print(f"The result of {number_1} {operation} {number_2} is: {result}")
elif operation == '/':
    if number_2 != 0:
        result = number_1 / number_2
        print(f"The result of {number_1} {operation} {number_2} is: {result}")
    else:
        result = "Error: Division by zero is not possible."
else:
    print("Error: Invalid operation.")
print(f"Thanks {name} for using the Python assignment calculator!")
