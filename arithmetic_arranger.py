
num1 = int(input("Enter first number: "))
op = input("Enter operator: ")
num2 = int(input("Enter second number: "))


if op == "+":
    result = num1 + num2
    print(f"  {num1:>5}\n+ {num2:>5}\n-----\n{result}")
elif op == "-":
    result = num1 - num2
    print(f"  {num1:>5}\n- {num2:>5}\n-----\n{result}")
elif op == "*":
    result = num1 * num2
    print(f"  {num1:>5}\n* {num2:>5}\n-----\n{result}")
elif op == "/":
    result = num1 / num2
    print(f"  {num1:>5}\n/ {num2:>5}\n-----\n{result}")
else:
    print("Invalid Operator!")
