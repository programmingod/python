# Prints factorial of a given number using recursion

def factorial(n):
    if n == 1:
        return 1
    else:
        return(n * factorial(n-1))

        
n = int(input("Enter a number: "))
if n <= 0:
    print("Invalid Input")
else:
    print("Factorial is: ", factorial(n))