# lib/helpers.py
import random
import time

# Slot Machine

def slots(session, user):
    random_symbols = ["🍀", "💎", "🍒"]
    print("Thanks for playing Slots.")
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

    # random_spin = [""]
    # print("Thanks for playing roullete.")
    # number = int(input("Which number do you want to bet on?"))
    # if number < 0 or number > 36:
    #     print("Invalid number! Please enter a number between 0 and 36")
    # bet = input("Please enter your bet amount: ")
    # while bet.isdigit() == False:
    #     print("Invalid bet, please enter a number.")
    #     bet = input("Please enter your bet amount: ")
    
    # if int(bet) > int(user.balance):
    #     print("Insufficient balance!")
    #     time.sleep(1)    
        
    # else:
    #     first_symbol = random.choice(random_symbols)
    #     second_symbol = random.choice(random_symbols)
    #     third_symbol = random.choice(random_symbols)
    #     print(f"{first_symbol} |  {second_symbol} | {third_symbol}")
    #     if len(set([first_symbol, second_symbol, third_symbol])) == 1:
    #         print(f"YOU WON ${int(bet)*3}!")
    #         user_balance = int(bet)*3 + int(user.balance)
    #         print(user_balance)
    #         print(f"Your new balance is ${user_balance}")
    #         user.balance = user_balance
    #         session.add(user)
    #         session.commit()    

    #     else:
    #         print(f"You lost ${bet}.")
    #         user_balance = int(user.balance) - int(bet)
    #         print(user_balance)
    #         print(f"Your new balance is ${user_balance}")
    #         user.balance = user_balance
    #         session.add(user)
    #         session.commit()