import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 10, 10, 10, 10]

def deal_card():
   card = random.choice(cards)
   return card
# Mendapatkan random card

def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)
# Menghitung score dari jumlah card yang didapat

def compare(user_scores,computer_scores):
    if computer_scores == user_scores:
        return print(f"You Draw")
    elif computer_scores == 0:
        return print("Computer have a blackjack card. Computer win")
    elif user_scores == 0:
        return print("You have a blackjack card. You Win")
    elif computer_scores > 21:
        return print("Computer score greater than 21. You Win")
    elif user_scores > 21:
        return print("Your score greater than 21. You Lose")
    elif user_scores > computer_scores:
        return print(f"Your score is {user_scores} greater than computer score {computer_scores}. You Win")
    else:
        return print(f"Computer score is {computer_scores} greater then your score {user_scores}. You Lose")\
# membandingkan user score dan computer score serta menentukan pemenang

def black_jack():
    # Mendapatkan 2 card untuk user dan computer
    user_card = []
    computer_card = []

    for i in range(2):
        user_card.append(deal_card())

    for i in range(2):
        computer_card.append(deal_card())

    # menampilkan card dari user dan first card dari computer. Serta juga mengulang mendapatkan card baru jika user ingin draw new card
    game_over = False
    while not game_over:
        user_score = calculate_score(user_card)

        if user_score == 0 and len(user_card) == 2:
            print(f"Your card is {user_card} then your score is 21. You Have a BLACK JACK")
        else:
            print(f"Your card is {user_card} then the score is {user_score}")

        print(f"The first computer card is {computer_card[0]}")

        if user_score > 21:
            game_over = True

        user_draw_new_card = input("Wanna draw new card ? Type 'y' for yes or type 'n' for no : ")
        if user_draw_new_card == "y":
            user_card.append(deal_card())
            game_over = False
        else:
            game_over = True

    # Mengulang kondisi dimana apabila score dari computer tidak sama dengan 0 dan kurang dari 17
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    # Menampilkan pemenang dari black jack card game
    if user_score == 0 and len(user_card) == 2:
        print(f"\n\nYour card is {user_card} then your score is 21. You Have a BLACK JACK")
    else:
        print(f"\n\nYour card is {user_card} then the score is {user_score}")
    print(f"Computer card is {computer_card} then the score is {computer_score}")
    compare(user_score,computer_score)

    # Restart the game
    restart_game = input("Wanna play a black jack card game again ? type 'y' for yes or type 'n' for no : ")
    if restart_game == "y":
        black_jack()
    else:
        print("Thanks for play")
# Black jack game

black_jack()
