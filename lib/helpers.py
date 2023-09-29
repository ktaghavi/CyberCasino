# lib/helpers.py
import random
import time

# Slot Machine

def slots(session, user):
    random_symbols = ["🍀", "💎", "🍒"]
    print("""Thanks for playing Slots.
    
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢸⣿⣿⠛⠻⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⣿⣤⣤⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⣿⠈⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⠁⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⢸⣿⠀⢀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿
⣿⣿⣿⣿⡿⠋⠀⣠⣤⣤⡄⢀⣤⣤⣤⡄⠀⠀⢠⣴⣶⣶⣤⡀⠙⢿⣿⣿⣿⣿
⣿⣿⣿⡏⠀⠀⠚⠛⠛⠛⠁⠘⠛⠛⠛⠀⠀⠀⠈⠙⠛⠛⠉⠀⠀⠀⢹⣿⣿⣿
⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿""")
    bet = input("Please enter your bet amount: ")
    while bet.isdigit() == False:
        print("Invalid bet, please enter a number")
        bet = input("Please enter your bet amount: ")
    
    if int(bet) > int(user.balance):
        print("Insufficient balance!")
        time.sleep(1)    

    else:
        first_symbol = random.choice(random_symbols)
        second_symbol = random.choice(random_symbols)
        third_symbol = random.choice(random_symbols)
        print(f"""⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠿⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠀⢸⣿⣿⠛⠻⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⣿⣤⣤⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇{first_symbol}⢸⡇{second_symbol}⢸⡇{third_symbol}⢸⣿⠀⢸⣿⣿⠈⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⣿⡇⠀⠀⢸⡇⠀⠀⢸⡇⠀⠀⢸⣿⠀⢸⣿⠁⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⢸⣿⠀⢀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⣦⣼⣿⣿⣿
⣿⣿⣿⣿⡿⠋⠀⣠⣤⣤⡄⢀⣤⣤⣤⡄⠀⠀⢠⣴⣶⣶⣤⡀⠙⢿⣿⣿⣿⣿
⣿⣿⣿⡏⠀⠀⠚⠛⠛⠛⠁⠘⠛⠛⠛⠀⠀⠀⠈⠙⠛⠛⠉⠀⠀⠀⢹⣿⣿⣿
⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿""")
        if len(set([first_symbol, second_symbol, third_symbol])) == 1:
            print(f"YOU WON ${int(bet)*3}!")
            user_balance = int(bet)*3 + int(user.balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            session.add(user)
            session.commit()    

        else:
            print(f"You lost ${bet}.")
            user_balance = int(user.balance) - int(bet)
            print(user_balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            session.add(user)
            session.commit()


# Roulette

def roulette(session, user):
        print("Thanks for playing Roulette!")
        print(f'Your balance: {user.balance}')
        bet = input('How much do you want to bet? ')
        while bet.isdigit() == False:
            print("Invalid bet, please enter a number")
            bet = input('Please enter a number: ')
        if int(bet) > int(user.balance):
            print("Insufficient balance!")
            time.sleep(1) 
        print('')
        number = int(input('Which number do you bet on? '))
        print('')
        if number < 0 or number > 36:
            print('Invalid number!')
        spin_number = random.randint(0,36)
        print('')
        if spin_number == number:
            user_balance = int(bet)*36 + int(user.balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            session.add(user)
            session.commit()  
        else:
            print(f"You lost ${bet}.")
            print(f'The number was {spin_number}')
            user_balance = int(user.balance) - int(bet)
            print(user_balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            session.add(user)
            session.commit()

        if user.balance <= 0:
            print('You ran out of money!!!')

#Blackjack

def blackjack (session, user):
    print("Thanks for playing Blackjack!")
    print(f'Your balance: {user.balance}')
    bet = input('How much do you want to bet? ')
    while bet.isdigit() == False:
        print("Invalid bet, please enter a number")
    if int(bet) > int(user.balance):
        print("Insufficient balance!")
        time.sleep(1) 
    print('')
    def deal_cards():
        """Returns a card from the deck"""
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_scores(cards):
        """Calculates scores for a given array of cards"""
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Its a push!"
        elif computer_score == 0 or computer_score == 21:
            print(f"You lost ${bet}.")
            user_balance = int(user.balance) - int(bet)
            print(user_balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            # session.add(user)
            session.commit()
            return "User lost, Computer has a blackjack"

        elif user_score == 0 or user_score == 21:
            user_balance = int(bet)*2 + int(user.balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            # session.add(user)
            session.commit() 
            return "User won, you have a blackjack"

        elif user_score > 21:
            print(f"You lost ${bet}.")
            user_balance = int(user.balance) - int(bet)
            print(user_balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            # session.add(user)
            session.commit()
            return "You bust! The computer wins!"

        elif computer_score > 21:
            user_balance = int(bet)*2 + int(user.balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            # session.add(user)
            session.commit() 
            return "The computer busts! User Wins!"

        elif user_score > computer_score:
            user_balance = int(bet)*2 + int(user.balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            # session.add(user)
            session.commit()
            return "The user cards are closer to 21 than the computer, User wins!"

        else:
            return (f"You lost ${bet}.")
            user_balance = int(user.balance) - int(bet)
            print(user_balance)
            print(f"Your new balance is ${user_balance}")
            user.balance = user_balance
            # session.add(user)
            session.commit()

    def play_game():
        print('')
        user_hand = []
        computer_hand = []
        is_game_over = False
        for _ in range(2):
            user_hand.append(deal_cards())
            computer_hand.append(deal_cards())

        while not is_game_over:
            user_score = calculate_scores(user_hand)
            computer_score = calculate_scores(computer_hand)
            print(f"The user score is {user_score}, and the user hand is {user_hand}")
            print(f"The computer first card is {computer_hand[0]}")

            if user_score > 21 or computer_score > 21:
                is_game_over = True
            else:
                hit = input("Do you want to hit? (y/n): ")
                if hit == 'y':
                    user_hand.append(deal_cards())
                else:
                    is_game_over = True
            
        while computer_score < 17:
            computer_hand.append(deal_cards())
            computer_score = calculate_scores(computer_hand)

        print(compare(user_score, computer_score))
        print(f"The user final hand is {user_hand}, the computer final hand is {computer_hand}")

    while input("Do you want to play Blackjack? (y/n): ") == "y":
        play_game()