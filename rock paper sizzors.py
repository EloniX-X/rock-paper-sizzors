#imports randint from random (dont import everything from the modual only what you need)
from random import randint

#sets the random list
t = ["rock", "paper", "sizzors"]

#tells computer to pick from rock to sizzors(starts from zero wich is first one)
computer = t[randint(0,2)]

#sets player to false for loop
player = False

#while player is false false it loops
while player == False:

    #if player has same anwser as computer print tie
    if (player==computer):
        print('TIE')

    #players choice for rocck paper or sizzors
    player = input("rock, paper, or scissors")

    #if there any caps it make the input lowercase
    player = player.lower()

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")




play = False
computer = t[randint(0,2)]