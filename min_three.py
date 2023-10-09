a = int(input('First number  : '))
b = int(input('Second number : '))
c = int(input('Third number  : '))
smallest = 0
if a < b and a < c :
    smallest = a
if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c
print(smallest, "is the smallest of three numbers.")