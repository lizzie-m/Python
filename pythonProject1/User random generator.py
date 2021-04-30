#
import random
def computer_guess(x):

   low = 1
   high = x
   feedback = ""
   while feedback != "c":
       if low != high:
           guess = random.randint(low, high)
       else:
           guess = low  # could be low or high it doesn't matter since low = high
       feedback = input( f"Is {guess} too high (H) , low (L) or correct(c)?: ").lower()
       if feedback == "h":
           high = guess-1
       elif feedback == "l":
           low = guess +1
   print(f" Yay I guessed {guess} correctly!")

computer_guess(10)


