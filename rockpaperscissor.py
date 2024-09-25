from random import randint


t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]

player = False

while player == False:
    player = input("Rock, Paper, Scissors? ")
    if player == computer:
        print("Player: ", player, "   Computer: ", computer)
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("Player: ", player, "   Computer: ", computer)
            print("You lose!", computer, "covers", player)
        else:
            print("Player: ", player, "   Computer: ", computer)
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("Player: ", player, "   Computer: ", computer)
            print("You lose!", computer, "cut", player)
        else:
            print("Player: ", player, "   Computer: ", computer)
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("Player: ", player, "   Computer: ", computer)
            print("You lose...", computer, "smashes", player)
        else:
            print("Player: ", player, "   Computer: ", computer)
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
