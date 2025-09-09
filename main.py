import random
from art import logo

def deal_card():
    #Returns a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    #Take a list of cards and return the score calculated from the cards
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, c_score):
    if c_score == user_score:
        return "***IT IS A DRAW!***"
    elif c_score == 0:
        return "***YOU LOSE!***"
    elif user_score == 0:
        return "***YOU WIN!***"
    elif user_score > 21:
        return "***YOU LOSE!***"
    elif c_score > 21:
        return "***YOU WIN!***"
    elif user_score > c_score:
        return "***YOU WIN!***"
    else:
        return "***YOU LOSE!***"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_another = input("Do you want to draw another card?(y or n):").lower()
            if draw_another == "y":
                user_cards.append(deal_card())
                calculate_score(user_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards}, Final Score: {user_score}")
    print(f"Computer's final hand is {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score, computer_score))



while input("Do you want to play a game of blackjack? (y or n):") == "y":
    print("\n" * 40)
    play_game()

while input("Are you sure?") == "y":
    print("Alright, Goodbye!")
    break
