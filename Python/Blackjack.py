import os
import random
logo = """
 .------.            _     _            _    _            _    
 |A_  _ |.          | |   | |          | |  (_)          | |   
 |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
 | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
 |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
 `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_/
       |  \/ K|                            _/ |                
       `------'                           |__/           
"""


def deal_card():
    """Returns a random card from the deck."""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.randint(0, len(deck) - 1)
    random_card = deck[random_card]
    return random_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

bank = 1000  

again = "y"
while again == "y":
    
    user_cards = []
    computer_cards = []
    
    for _ in range(2):
    #append 'cause of list
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    print(logo)
    print(f"Your current bank is: {bank}$")
    bid = int(input("How much do you want to bid: $"))
    while bid > bank:
        bid = int(input("Not enough cash! Input valid bid value! \nHow much do you want to bid: $"))
    os.system("cls")
    print(logo)
    print(f"\nYour cards are: {user_cards}, current score: {calculate_score(user_cards)} ")
    print(f"Computer's first card: [{computer_cards[0]}, ?]")

    option = ""
    while option != "stand":
        option = input("\nType 'hit' to get another card, type 'stand' to pass: ").lower()
        while option != "hit" and option != "stand":
            option = input("Wrong choice! \nType 'hit' to get another card, type 'stand' to pass: ").lower()
        if option == "hit":
            os.system("cls")
            print(logo)
            user_cards.append(deal_card())
            if sum(user_cards) > 21 and 11 not in user_cards:
                break
            print(f"\nYour cards are: {user_cards}, current score: {calculate_score(user_cards)} ")
            print(f"Computer's first card: [{computer_cards[0]}, ?]")
    if 11 in computer_cards and 10 in computer_cards:
        print()
    else:
        while calculate_score(computer_cards) <= 16:
            computer_cards.append(deal_card())
        if user_cards[0] <= 5 and sum(computer_cards) <= 18:
            computer_cards.append(deal_card())
        
    os.system("cls")
    print(logo)
    print(f"\n\nYour final hand: {user_cards}, with score of: {calculate_score(user_cards)}")
    print(f"Dealer's final hand: {computer_cards}, with score of: {calculate_score(computer_cards)}")

    if calculate_score(user_cards) == 0:
        print("Blackjack! \nPlayer win!")
        bank += bid
        print(f"You gain {bid}$ \nCurrent bank: {bank}$")
    elif calculate_score(computer_cards) == 0:
        print("Blackjack! \nDealer win!")
        bank -= bid
        print(f"You lose {bid}$ \nCurrent bank: {bank}$")
    elif sum(user_cards) > 21:
            print("\nBust!")
            print("Dealer win!\n")
            bank -= bid
            print(f"You lose {bid}$ \nCurrent bank: {bank}$")
    elif sum(computer_cards) > 21:
            print("\nDealer bust!")
            print("Player win!\n")
            bank += bid
            print(f"You gain {bid}$ \nCurrent bank: {bank}$")
    elif sum(user_cards) > sum(computer_cards) and sum(user_cards) <= 21:
        print("\nPlayer win!\n")
        bank += bid
        print(f"You gain {bid}$ \nCurrent bank: {bank}$")
    elif sum(user_cards) < sum(computer_cards) and sum(computer_cards) <= 21 :
        print("\nDealer win!\n")
        bank -= bid
        print(f"You lose {bid}$ \nCurrent bank: {bank}$")
    elif sum(user_cards) == sum(computer_cards):
        print("\nDraw!\n")
        
    if bank == 0:
        print("Game over!")
        break
    
    again = input("\nWant another one? y/n -> ").lower()
    if again == "y":
        os.system("cls")
    else:
        break