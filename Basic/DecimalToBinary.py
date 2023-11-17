def binary(n):
    if n > 1:
        binary(n//2)
    print (n%2, end = "")

n =int(input("Enter a number here: "))
print ("The given decimal value in binary is: ")
binary(n)