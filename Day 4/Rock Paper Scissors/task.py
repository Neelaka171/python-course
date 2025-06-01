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

image = [rock,paper,scissors]
your_choice = int(input("what is your choice rock(0) paper(1) or scissor(2):"))
if   0<= your_choice <=2:
    print("your choice is:\n")
    print(image[your_choice])

computer_choice = random.randint(0,2)
print("computer choice is:\n")
print(image[computer_choice])

if your_choice == computer_choice :
    print("game draw")
elif your_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and your_choice == 2:
    print("You lose!")
elif your_choice > 2:
    print("invalid")
elif computer_choice > your_choice:
    print("You lose!")
elif your_choice > computer_choice:
    print("You win!")



