a = int(input("Enter first variable: "))
b = int(input("Enter second variable: "))
temp = a
a = b
b = temp
print("After swap,")
print("Value of first var: ", a)
print("Value of second var: ", b)

# Let's try another way to do this, without a temp variable

a = int(input("Enter first variable: "))
b = int(input("Enter second variable: "))
a,b = b,a
print("After swap,")
print("Value of first var: ", a)
print("Value of second var: ", b)