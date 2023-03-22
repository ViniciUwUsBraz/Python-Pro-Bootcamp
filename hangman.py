import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
""")
      
words=["Monkey","Snake","Panda","Shark","Sheep","Cow","Horse","Chicken","Zebra","Dolphin"]
chosen_word=random.choice(words)
underline=[]

lives=6
correct=0
aux1=0

for i in range(len(chosen_word)):
    underline.append("_")

def print_word():
    for i in underline:
        print(i,end=" ")

while(lives>0 and correct!=len(chosen_word)):

    guess=input("\n\nGuess a letter: ").upper()

    for i in range(len(chosen_word)):
        if(guess==chosen_word[i].upper()):
            underline[i]=guess
            correct+=1

    print_word()
    if(correct<=aux1):
        lives-=1
        print(f"\nLives:{lives}")
    print(stages[lives])

    aux1=correct
    
if(correct==len(chosen_word)):
    print("You Win!!")
else:
    print("You lose!!")