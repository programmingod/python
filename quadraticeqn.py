import cmath

print("Input the coefficients of x^2, x and 1")

a = int(input("Coeff. of x^2 (!=0): "))
b = int(input("Coeff. of x: "))
c = int(input("Coeff. of 1: "))

d = (b**2)-(4*a*c)

sol1 = ((-b-cmath.sqrt(d))/(2*a))
sol2 = ((-b+cmath.sqrt(d))/(2*a))

print ("the roots are: ",sol1,sol2)
