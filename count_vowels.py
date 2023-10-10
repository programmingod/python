string = input("Enter text here: ")

vowels = "aeiou"
string = string.casefold()

count = {key:sum([1 for char in string if char == key]) for key in vowels}

print (count)

