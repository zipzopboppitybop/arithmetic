
num1 = int(input("Enter first number: "))
op = input("Enter operator: ")
num2 = int(input("Enter second number: "))


if op == "+":
    result = num1 + num2
    print(f"  {num1:>5}\n+ {num2:>5}\n-------\n {result:>6}")
elif op == "-":
    result = num1 - num2
    print(f"  {num1:>5}\n- {num2:>5}\n-------\n {result:>6}")
elif op == "*":
    result = num1 * num2
    print(f"  {num1:>5}\n* {num2:>5}\n-------\n {result:>6}")
elif op == "/":
    result = num1 / num2
    print(f"  {num1:>5}\n/ {num2:>5}\n-------\n {result:>6}")
else:
    print("Invalid Operator!")
