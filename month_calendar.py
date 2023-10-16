import calendar

y = int(input("Enter Year: "))
m = int(input("Enter month (in numbers): "))

cal = calendar.month(y,m)

print(cal)