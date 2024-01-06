import random

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

#Write your code below this line 👇

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: \n"))

computer_choice = random.randint(0, 2)

if player_choice == 0:
  print(rock)
  if computer_choice == 0:
    print("Computer chose: \n" + rock)
    print("It's a tie!")
  elif computer_choice == 1:
    print("Computer chose: \n" + paper)
    print("You lose!")
  else:
    print("Computer choice: \n" + scissors)
    print("You win!")
elif player_choice == 1:
  print(paper)
  if computer_choice == 0:
    print("Computer chose: \n" + rock)
    print("You win!")
  elif computer_choice == 1:
    print("Computer chose: \n" + paper)
    print("It's a tie!")
  else:
    print("Computer choice: \n" + scissors)
    print("You lose!")
elif player_choice == 2:
  print(scissors)
  if computer_choice == 0:
    print("Computer chose: \n" + rock)
    print("You lose!")
  elif computer_choice == 1:
    print("Computer chose: \n" + paper)
    print("You win!")
  else:
    print("Computer choice: \n" + scissors)
    print("It's a tie!")
else:
  print("You typed an invalid number")
  
  
