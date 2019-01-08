
num1 = float(input("Enter a number: "))
op = input("Enter a operator: ")
num2 = float(input("Enter another number: "))

try:
    if op == "+":
        print(num1+num2)
    elif op == "-":
        print(num1-num2)
    elif op == "/":
        print(num1/num2)
    elif op == "*":
        print(num1*num2)
    else:
        print("Invalid operator")

except ZeroDivisionError:
        print("divide by zero error")

