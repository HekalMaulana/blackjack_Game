import random
import os

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # Hint 6: Create a function called calculate_score() that takes a List of cards as input
    # and returns the score.
    # Look up the sum() function to help you do this.
    """ calculate the cards and return the score """
    score = sum(cards)
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if score == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score

def compare(user_scores, computer_scores):
    # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    if computer_scores == user_scores:
        return "then it's a draw"
    elif computer_scores == 0:
        return "You Loses"
    elif user_scores == 0:
        return "You Wins"
    elif user_scores > 21:
        return "Your score greater than 21, You Lose"
    elif computer_scores > 21:
        return "The computer score greater than 21, You win"
    elif computer_scores > user_scores:
        return "The computer score greater than you, You Lose"
    else:
        return "Your score greater than computer, You Win"


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def blackjack_game():
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_card())

    for i in range(2):
        computer_cards.append(deal_card())


    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    game_over = False

    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"your cards is {user_cards} and current score is {user_score}")
        print(f"The first computer cards is {computer_cards[0]}")


        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
            # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            user_draw = input("You wanna draw another card ? Type 'y' if yes or type 'n' if not : ")
            if user_draw == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

        # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

        the_winners = compare(user_score, computer_score)
        print(f"\n\nYour last cards is {user_cards} then the score is {user_score}")
        print(f"The computer cards is {computer_cards} then the computer score is {computer_score}")
        print(the_winners)

    # Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
        user_restart_the_game = input("You wanna restart the game ? Type 'y' for yes or type 'n' for not : ")
        if user_restart_the_game == 'y':
            os.system('cls')
            blackjack_game()
        else:
            print("Thanks for playing")

blackjack_game()
