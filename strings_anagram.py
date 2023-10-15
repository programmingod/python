s1 = input("Enter String 1: ")
s2 = input("Enter String 2: ")

def check(s1, s2):
    
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")

check(s1, s2)