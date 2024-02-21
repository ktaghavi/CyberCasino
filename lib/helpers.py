# lib/helpers.py
import random
import time
from cards import CARDS, get_blank_card_ascii

# Slot Machine

def slots(session, user):
    random_symbols = ["🍀", "💎", "🍒"]
    print("""Thanks for playing 
.----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || |   _____      | || |     ____     | || |  _________   | || |    _______   | |
| |   /  ___  |  | || |  |_   _|     | || |   .'    `.   | || | |  _   _  |  | || |   /  ___  |  | |
| |  |  (__ \_|  | || |    | |       | || |  /  .--.  \  | || | |_/ | | \_|  | || |  |  (__ \_|  | |
| |   '.___`-.   | || |    | |   _   | || |  | |    | |  | || |     | |      | || |   '.___`-.   | |
| |  |`\____) |  | || |   _| |__/ |  | || |  \  `--'  /  | || |    _| |_     | || |  |`\____) |  | |
| |  |_______.'  | || |  |________|  | || |   `.____.'   | || |   |_____|    | || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
    
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
        print('''Thanks for playing
.______        ______    __    __   __       _______ .___________..___________. _______ 
|   _  \      /  __  \  |  |  |  | |  |     |   ____||           ||           ||   ____|
|  |_)  |    |  |  |  | |  |  |  | |  |     |  |__   `---|  |----``---|  |----`|  |__   
|      /     |  |  |  | |  |  |  | |  |     |   __|      |  |         |  |     |   __|  
|  |\  \----.|  `--'  | |  `--'  | |  `----.|  |____     |  |         |  |     |  |____ 
| _| `._____| \______/   \______/  |_______||_______|    |__|         |__|     |_______|
                                                                                       ''')
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

def deal_cards():
    """Returns a card from the deck"""
    card_rank = random.choice(list(CARDS.keys()))
    card_value, card_ascii = CARDS[card_rank]
    return card_value, card_ascii

def calculate_scores(cards):
    """Calculates scores for a given array of cards"""
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score, bet, user, session):
    user_busted = user_score > 21
    computer_busted = computer_score > 21
    
    # Check for user bust first
    if user_busted:
        print(f"You busted with a score of {user_score}. You lost ${bet}.")
        user.balance -= bet
    elif computer_busted:
        print(f"The computer busted. You win ${bet}!")
        user.balance += bet
    # If no one busted, then compare scores for other outcomes
    elif user_score == computer_score:
        print("It's a push!")
    elif user_score > computer_score:
        print(f"You win with a score of {user_score}. You win ${bet}!")
        user.balance += bet
    else:
        print(f"The computer wins with a score of {computer_score}. You lost ${bet}.")
        user.balance -= bet
    
    session.commit()
    return f"Your new balance is ${user.balance}"

def display_hand(hand):
    """Display the hand with ASCII art side by side"""
    card_rows = [card_ascii.split('\n') for _, card_ascii in hand]
    
    for i in range(len(card_rows[0])):
        print('  '.join(row[i] for row in card_rows))

def display_initial_dealer_hand(hand):
    """Display the dealer's first card and a blank card."""
    card_ascii = hand[0][1]  # The actual card's ASCII representation
    blank_card_ascii = get_blank_card_ascii()  # The blank card's ASCII representation
    
    actual_card_rows = card_ascii.split('\n')
    blank_card_rows = blank_card_ascii.split('\n')
    
    for i in range(len(actual_card_rows)):
        print(actual_card_rows[i] + '  ' + blank_card_rows[i])

def play_game(session, user, bet):
    # Deal initial cards
    user_hand = [deal_cards(), deal_cards()]
    computer_hand = [deal_cards(), deal_cards()]

    # Calculate initial scores
    user_score = calculate_scores([card_value for card_value, _ in user_hand])
    computer_score = calculate_scores([card_value for card_value, _ in computer_hand])

    # Display user hand and dealer's initial hand with one card hidden
    print(f"Your score is {user_score}, and your hand is:")
    display_hand(user_hand)

    print("Dealer's hand:")
    display_initial_dealer_hand(computer_hand)

    # User's turn
    is_game_over = False
    while not is_game_over:
        user_score = calculate_scores([card_value for card_value, _ in user_hand])
        if user_score > 21:
            print("Bust! Your score is over 21.")
            is_game_over = True
        else:
            hit = input("Do you want to hit? (y/n): ")
            if hit.lower() == 'y':
                user_hand.append(deal_cards())
                user_score = calculate_scores([card_value for card_value, _ in user_hand])
                print(f"Your new score is {user_score}, and your hand is:")
                display_hand(user_hand)
            else:
                is_game_over = True

    # Dealer's turn
    print("Dealer's hand revealed:")
    display_hand(computer_hand)
    while computer_score < 17:
        computer_hand.append(deal_cards())
        computer_score = calculate_scores([card_value for card_value, _ in computer_hand])

    # Final comparison
    print(compare(user_score, computer_score, bet, user, session))
    print("Your final hand is:")
    display_hand(user_hand)
    print("Dealer's final hand is:")
    display_hand(computer_hand)

def blackjack(session, user):
    print('''Thanks for playing

    .------.            _     _            _    _            _    
    |A_  _ |.          | |   | |          | |  (_)          | |   
    |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
    | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
    `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ 
          |  \/ K|                            _/ |                
          `------'                           |__/           

    ''')

    print(f'Your balance: {user.balance}')
    bet = input('How much do you want to bet? ')
    while not bet.isdigit():
        print("Invalid bet, please enter a number.")
        bet = input('How much do you want to bet? ')

    bet = int(bet)
    if bet > user.balance:
        print("Insufficient balance!")
        time.sleep(1)
    else:
        play_game(session, user, bet)

    # After the game concludes, you can then ask if they want to play again
    play_again_response = input("Do you want to play Blackjack again? (y/n): ")
    while play_again_response == 'y':
        print(f'Your balance: {user.balance}')
        bet = input('How much do you want to bet? ')
        while not bet.isdigit():
            print("Invalid bet, please enter a number.")
            bet = input('How much do you want to bet? ')

        bet = int(bet)
        if bet > user.balance:
            print("Insufficient balance!")
            time.sleep(1)
        else:
            play_game(session, user, bet)

        play_again_response = input("Do you want to play Blackjack again? (y/n): ")
