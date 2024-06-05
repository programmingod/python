def toppings(ketchup, onion, mustard):
    num_toppings = int(ketchup + onion + mustard)

    print("Number of toppings: ", num_toppings)
    if ketchup == 1:
        print("Ketchup")
    if onion == 1:
        print("Onion")
    if mustard == 1:
        print("Mustard")


toppings(1,0,1)