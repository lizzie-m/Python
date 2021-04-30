#A random number generator game
import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 9 # to define the guess, however value r
    # not important
    while guess != random_number:
        guess = int(input(f"Insert a number between 1 and {x}: "))
        print(guess)
        if guess > random_number:
            print(" Sorry to high, guess again! ")
        elif guess < random_number:
            print(" Sorry to low, guess again!")
    print(f"congratulations you guessed the number {random_number} correctly")

def computer_guess(x):
   low = 1
   high = x
   feedback = ""
   while feedback != "c":
       if low != high:
           guess = random.randint(low,high)
       else:
           guess = low
           feedback = input( f"Is {guess} too high (H) , low (L) or correct(c)?: ").lower()
       if feedback == "h":
           high = guess-1
       elif feedback == "l":
           low = guess +1
   print(f"congradulations you guessed {guess} correctly!")


guess(10)
