ketchup  = input("Do you want ketchup? (yes/no): ")
if ketchup.lower() == 'yes':
    ketchup = 1
else:
    ketchup = 0

onion = input("Do you want onion? (yes/no): ")
if onion.lower() == 'yes':
    onion = 1
else:
    onion = 0

mustard = input("Do you want mustard? (yes/no): ")
if mustard.lower() == 'yes':
    mustard = 1
else:
    mustard = 0

def toppings(k, o, m):
    num_toppings = int(k + o + m)

    print("Number of toppings: ", num_toppings)
    if k == 1:
        print("Ketchup")
    if o == 1:
        print("Onion")
    if m == 1:
        print("Mustard")

toppings(ketchup,onion,mustard)