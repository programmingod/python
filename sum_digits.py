n = int(input("Enter a Number: "))
result = 0
while n>0:
    digit = n%10
    result += digit
    n = n//10


print("Sum of digits is: ", result)