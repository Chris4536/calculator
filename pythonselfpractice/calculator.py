import sys

while True:
    # Prompt the user for input
    num1 = input("Enter the first number (or type 'exit' to quit): ")
    
    # Allow the user to exit the program
    if num1.lower() == "exit":
        print("Goodbye!")
        break  # Exit the loop and terminate the program
    
    operator = input("Enter the operation you wish to perform (+, -, *, /): ")
    num2 = input("Enter the second number: ")
    
    try:
        # Convert inputs to float
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue  # Restart the loop
    
    # Perform the calculation based on the operator
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue  # Restart the loop
        result = num1 / num2
    else:
        print("Invalid operator entered.")
        continue  # Restart the loop

    # Correctly format and display the result
    print(f"{num1} {operator} {num2} = {result}")
