def reverse(s):
    rs = ""
    for i in s:
        rs = i + rs
    print("The reversed string is ", rs)


string = input("Enter a string: ")
reverse(string)