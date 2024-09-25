num1 = input("Enter the first number: ")
operator = input("Enter the operation to be done (+,-,*,/,%): ")
num2 = input ("Enter the second number: ")

if operator == '+':
    print(int(num1) + int(num2))
if operator == '-':
    print(int(num1) - int(num2))
if operator == '*':
    print(int(num1) * int(num2))
if operator == '/':
    print(int(num1) / int(num2))
if operator == '%':
    print(int(num1) % int(num2))