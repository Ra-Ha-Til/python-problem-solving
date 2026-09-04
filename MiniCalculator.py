#basic mini calculator
a = float(input("Enter the first number:"))
b = int(input("Enter the 2nd number:"))
op = input("Which you want to do:(+, -, *, /, **, %):")

if op == '+':
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    print(a/b)
elif op == "**":
    print(a**b)
elif op == "%":
    print(a%b)
else:
    print("Syntax Error")