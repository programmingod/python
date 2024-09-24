print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter Your Choice: "))

if choice == 1:
    celsius = int(input("Enter temperature in celsius: "))
    fahrenheit = (celsius*(1.8))+32
    print("The converted value is ", fahrenheit,"F")

elif choice == 2:
    fah = int(input("Enter temp in Fahrenheit"))
    cel = (fah-32)/1.8
    print("The converted value is ", cel,"C")


