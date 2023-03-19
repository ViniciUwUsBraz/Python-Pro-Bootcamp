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

chose=input("What do you choose? 'Rock', 'Paper' or 'Scissors': ").lower()
bot_chose=random.randint(1,3)

if(chose=='rock'):
    print(rock)
    chose=1
elif(chose=='paper'):
    print(paper)
    chose=2
elif(chose=='scissors'):
    print(scissors)
    chose=3


print("Computer chose:")

if(bot_chose==1):
    print(rock)
elif(bot_chose==2):
    print(paper)
elif(bot_chose==3):
    print(scissors)


if(chose==bot_chose):
    print("Draw")
elif((chose==1 and bot_chose==3) or (chose==2 and bot_chose==1) or (chose==3 and bot_chose==2)):
    print("You Win")
else:
    print("You Lose")