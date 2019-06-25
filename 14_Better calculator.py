num1 = float(input('First Number:'))
op = input('Operator:')
num2 = float(input('Second number:'))

if op == '+':
    print(num2 + num1)
elif op == '-':
    print(num1 - num2)
elif op == '/':
    print(num1 / num2)
elif op == '*':
    print(num1 * num2)
else:
    print("Invalid Operator")