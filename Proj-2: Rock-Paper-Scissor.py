# Importing the library
import random

# Creating Figures
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors] # List of possible choices

print("What do you choose? \n Type 0 for Rock \n Type 1 for Paper\n Type 2 for Scissors.\n ") # Printing Instruction about how to interact with the program
while True: # Infinite loop is used otherwise after one run program will stop . 
  user_choice = int(input("Enter your Choice : ")) # Taking user's choice
 # Game Play Logic
  if user_choice >= 3 or user_choice < 0: 
      print("You typed an invalid number, you lose!") # Avoiding error messages
  else:
      print(game_images[user_choice])
      computer_choice = random.randint(0, 2) # Choosing random integer in range of 0 to 2
      print("Computer chose:")
      print(game_images[computer_choice]) # Showing computer's chosen option
      # Result
      if user_choice == 0 and computer_choice == 2:
          print("You win!")
      elif computer_choice == 0 and user_choice == 2:
          print("You lose")
      elif computer_choice > user_choice:
          print("You lose")
      elif user_choice > computer_choice:
          print("You win!")
      elif computer_choice == user_choice:
          print("It's a draw")
  # Checking if the user wants to play the game again or not
  ask = input("want to continue ? Type Y for yes or N for no. ")
  if ask.lower() != 'y':
    break
