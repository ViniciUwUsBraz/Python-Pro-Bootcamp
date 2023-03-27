import random

guess=0
random_number=random.randint(1,100)
attempts=0
print("""
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
                                                                                          
""")

print("\n\nWelcome to the Number Guessing Game!!")

print("Im thinking of a number between 1 and 100.")
dificult=input("Chose a difficulty. Type 'Easy' or 'Hard':").lower()

if(dificult=="hard"):
    attempts=5
    print(f"You have {attempts} attempts to guess the number.")
else:
    attempts=10
    print(f"You have {attempts}  attempts to guess the number.")

while(guess!=random_number and attempts>0):
    guess=int(input("Guess a number: "))
    attempts-=1
    
    if(guess>random_number):
        print("Too high")
        print(f"You have {attempts} attempts.")
    elif(guess<random_number):
        print("Too low")
        print(f"You have {attempts} attempts.")

if(guess==random_number):
    print(f"You win \nThe number is: {random_number}.")
else:
    print(f"You lose\nThe number is: {random_number}.")