import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards=[1,2,3,4,5,6,7,8,9,10,'J','Q','K']
dealer_cards=[]
your_cards=[]

dealer_visible_points=0
dealer_points=0
your_points=0

dealer_play=0
game_run='y'
round_run='y'
run=""
 

def dealer_round(dealer_points):
    if dealer_points>=21 :
        dealer_round=0
    elif dealer_points<=11:
        dealer_round=1
    elif dealer_points<=17:
            aux=random.randint(1,100)
            if aux>80:
                dealer_round=1
            else:
                dealer_round=0
    else:
        dealer_round=0
    return dealer_round
    
def count_points(p_cards):
    points=0
    for card in p_cards:
        if card=='J' or card=='Q' or card=='K':
            card=10
        points+= int(card)
    return points

def card_choice(p_cards):
    p_cards.append(random.choice(cards))

if input("Do you want to play a game of BlackJack? 'Y' or 'N': ").lower()=='y':
    print(logo)
    run='y'

while(run=='y'):

    dealer_cards=[]
    your_cards=[]
    dealer_points=0
    your_points=0

    while(game_run=='y'):

        card_choice(your_cards)
        card_choice(dealer_cards)
        card_choice(your_cards)
        card_choice(dealer_cards)

        print(f"Your cards {your_cards}")
        print(f"Dealer cards ['{dealer_cards[0]}',*]")

        if str(dealer_cards[0]).isnumeric():
            dealer_visible_points=int(dealer_cards[0])
        else:
            dealer_visible_points=10

        dealer_points=count_points(dealer_cards)
        your_points=count_points(your_cards)

        print(f"Your {your_points} \nDealer min points {dealer_visible_points}")
        round_run=input("Type 'y' for another card or 'n' to pass: ").lower()
        dealer_play=dealer_round(dealer_points)

        if(round_run=='n' and dealer_round==0):
            print("Era pra finalizar o game")
            game_run='n'

        while(round_run=='y' or dealer_play==1):

            if(round_run=='y'):
                card_choice(your_cards)
                your_points=count_points(your_cards)
                print(f"\n\nYour cards: {your_cards}\nYour points: {your_points}")

            if(dealer_play==1):
                print("Dealer draw")
                card_choice(dealer_cards)
                dealer_points=count_points(dealer_cards)
                dealer_play=dealer_round(dealer_points)
            else:
                print("Dealer pass")

            if(round_run=='y'):
                round_run=input("\n\nType 'y' for another card or 'n' to pass: ")
        
        if(round_run=='n' and dealer_play==0):

            print(f"\n\nDealer finish\nYour point:{your_points}\nDealer points:{dealer_points}")

            if(your_points==dealer_points):
                print("Draw")
            elif(dealer_points>your_points and dealer_points>21):
                print("You win")
            elif(your_points>dealer_points and your_points<=21):
                print("You win")
            else:
                print("You lose")

            game_run='n'

    game_run=input("\n\nDo you want to play again? 'Y' or 'N': ").lower()
    os.system("clear")


