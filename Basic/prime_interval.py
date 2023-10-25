# Prints all prime numbers in a given interval

lowerlimit = int(input("Enter lower limit of interval: "))
upperlimit = int(input("Enter upper limit of interval: "))

for num in range(lowerlimit, upperlimit+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
                print(num)