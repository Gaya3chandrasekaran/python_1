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

choice=input ("enter your choice: 0 for 'rock', 1 for 'paper',2 for 'scissors':\n")
choice_int=int(choice)
game=[rock,paper,scissors]
#user_choice
user_choice=game[choice_int]
print("user choice:")
print(user_choice)
#bot choice
robot_choice=random.randint(0,2)
print("the computer chose:")
print(game[robot_choice])
#game rule
if (choice_int==robot_choice):
    print("it's a draw")
elif(choice_int==0 and robot_choice==1):
    print("you've lost")
elif(choice_int==0 and robot_choice==2):
    print("you win")
elif(choice_int==1 and robot_choice==0):
    print("you win")
elif(choice_int==1 and robot_choice==2):
    print("you've lost")
elif(choice_int==2 and robot_choice==0):
    print("you've lost")
elif(choice_int==2 and robot_choice==1):
    print("you win")
else:
    print("invalid choice")
