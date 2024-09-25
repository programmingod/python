def sum(n):
    if n <= 1:
        return n
    else:
        return (n+sum(n-1))
    

n = int(input("Enter Number: "))

print("Sum of first ", n, " numbers is", sum(n))