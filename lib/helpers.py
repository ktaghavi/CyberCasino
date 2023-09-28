# lib/helpers.py
import random
import time

# Slot Machine

def slots(session, user):
    random_symbols = ["🍀", "💎", "🍒"]
    print("Thanks for playing slots.")
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
        print(f"{first_symbol} |  {second_symbol} | {third_symbol}")
        if len(set([first_symbol, second_symbol, third_symbol])) == 1:
            print(f"YOU WON ${int(bet)*3}!")
            user_balance = int(bet)*3 + int(user.balance)
            print(user_balance)
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


# Roullette

def roullette(session, user):
    random_spin = [""]
    print("Thanks for playing slots.")
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
        print(f"{first_symbol} |  {second_symbol} | {third_symbol}")
        if len(set([first_symbol, second_symbol, third_symbol])) == 1:
            print(f"YOU WON ${int(bet)*3}!")
            user_balance = int(bet)*3 + int(user.balance)
            print(user_balance)
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