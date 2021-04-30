#A game of rock paper scissors with the computer
#        return
 #
import random

def play():
    user1 = input(f"Pick a choice. Rock (r), Paper(p) or Scissors (s)?")
    computer = random.choice(["r","p","c"])
    if user1 == computer:
        return "Tie!"
    if rules(user1,computer): #calling rules function
        return "Congratulations you win!"
    return " Sorry, you lost, try again!"


def rules(user,opponent):
    if (user == "r" and opponent == "s") or (user == "s" and opponent == "p") or (user == "p" and opponent =="r"):
        return True

print(play())