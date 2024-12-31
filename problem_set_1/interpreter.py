# Asking for the expression from the user
expression = input("Expression: ").strip().split(" ")

# unpack the values to an appropriate variables
num2 = float(expression[-1])
num1 = float(expression[0])
operator = expression[1]

# Checking for the operation to be done
if operator == "+":
    print(f"{(num1 + num2):.1f}")
if operator == "-":
    print(f"{(num1 - num2):.1f}")
if operator == "*":
    print(f"{(num1 * num2):.1f}")
if operator == "/":
    print(f"{(num1 / num2):.1f}")
