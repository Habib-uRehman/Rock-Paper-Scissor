#ROCK PAPER, SCISSORS GAME
import random
rock = '''
            ROCK
            _______
          ---'   ____)
               (_____)
               (_____)
               (____)
         ---.__(___)
'''
paper = '''
PAPER
        --_______
---'    __________)
           _______)
          ________)
         _________)
---._____________)
'''
scissors= '''
Scissors
     _______
---'   ______)
          ______)
       __________)
      (____)
---.__(___)

'''
mychoice = ""
sysChoice = ""
system = random.randint(0,2)
choice = int(input("Enter 0 for Rock, 1 for paper, 2 for Scissors "))
if choice == 0:
    mychoice = rock
elif choice == 1:
    mychoice= paper
elif choice == 2:
    mychoice = scissors
else:
    print("please enter from 0 to 2")
print(mychoice)
# computer turn.
if system == 0:
    sysChoice = rock
elif system == 1:
    sysChoice= paper
elif system == 2:
    sysChoice = scissors
print(sysChoice)

if mychoice == rock and sysChoice == rock:
    print("Tie, Try Agian")
elif mychoice == rock and sysChoice == scissors:
    print("You Win")
elif mychoice == rock and sysChoice == paper:
    print("you win")
elif mychoice == paper and sysChoice == rock:
    print("you Lose")
elif mychoice == paper and sysChoice == paper:
    print("Tie, Try again")
elif mychoice == paper and sysChoice == scissors:
    print("You Lose")
elif mychoice == scissors and sysChoice == rock:
    print("You Lose")
elif mychoice == scissors and sysChoice == paper:
    print("YOu Win")
elif mychoice == scissors and sysChoice == scissors:
    print("Tie, Try again")
