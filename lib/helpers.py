# lib/helpers.py
import random

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()


def slots():
    random_symbols = ["a", "b", "c", "d", "e"]
    print("Thanks for playing slots.")
    bet = input("Please enter your bet amount: (choose 10, 15, 20)")
    # print("Each spin is $10")
    first_symbol = random.choice(random_symbols)
    second_symbol = random.choice(random_symbols)
    third_symbol = random.choice(random_symbols)
    print(f"{first_symbol} |  {second_symbol} | {third_symbol}")
    print(f"you lost {bet}")
    # print(random.choice(random_symbols))
    # print(random.choice(random_symbols))
