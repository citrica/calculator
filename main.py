x = int(input("Enter the number X: "))
y = int(input("Enter the number Y: "))
operation = input("Enter an operator (+, -, * or /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("The operator is invalid. ")