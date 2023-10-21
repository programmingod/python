# Gives remarks on your performance based on marks out of 100
# If your score out of 100 is less than 33, then you fail.
# If your score is above 33 but less than 75, then you pass, but do not qualify for IIT and BITS
# If youa re between 75 and 90, you are above average.
# If your marks are above 90, you are a topper.


def grading(marks):
    if marks < 33:
        print("Fail")
    elif marks > 33 and marks < 75:
        print("Pass, but no IIT/BITS")
    elif marks > 75 and marks < 90:
        print("Above average")
    else:
        print("Topper")

grading(int(input("Enter your marks: ")))