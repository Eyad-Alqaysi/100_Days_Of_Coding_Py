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

images = [rock, paper, scissors]

user = int(input("Type 0 for Rock, 1 for Paper, 2 for Pistol.\n"))
print(images[user])

computer = random.randint(0, 2)
print("Computer chose:")
print(images[computer])

if user >= 3 or user < 0: 
  print("invalid number") 
elif user == 0 and computer== 2:
  print("You win")
elif computer == 0 and user == 2:
  print("You lose")
elif computer > user:
  print("You lose")
elif user > computer:
  print("You win")
elif computer == user:
  print("It's a draw")