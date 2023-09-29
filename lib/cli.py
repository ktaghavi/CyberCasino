# lib/cli.py
from models.model_1 import Users, PlayedGames
from sqlalchemy.orm import (sessionmaker)
from sqlalchemy import create_engine
import inquirer
import time


from helpers import (
    slots,
    roulette,
    blackjack
)

if __name__ == "__main__":
    engine = create_engine('sqlite:///casino.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    in_game = True
    print("Thanks for coming to Cyber Casino!!!")
    name = input("Please enter your name: ")
    user = session.query(Users).filter(Users.username == name).first()
    if user:
        print(f"Welcome back to Cyber Casino {user.username}!")
        print (f"You have a balance of {user.balance}")
    else:
        print("Since you're a NEW patron, we will give you a $1000 Welcome Bonus!")
        new_user = Users(username=name, balance=1000)
        session.add(new_user)
        session.commit()
        user = session.query(Users).filter(Users.username == name).first()
   
    while in_game:

        questions = [
        inquirer.List('games',
                        message="What Game do you want to play?",
                        choices=['Slots', 'Roulette', 'Blackjack',"Update Username", "Delete Account", "Exit the Casino"],
                    ),
        ]
        answers = inquirer.prompt(questions)
        print(answers["games"])
        if answers["games"] == "Slots":
            print("Slots game loading...")
            time.sleep(1)
            in_slots = True
            while in_slots:
                slots(session, user)
                slots_continue = input("Play again? [y/n]: ")
                if slots_continue == "n":
                    in_slots = False

        elif answers["games"] == "Roulette":
            print("Roulette game loading...")
            time.sleep(1)
            in_roulette = True
            while in_roulette:
                roulette(session, user)
                roulette_continue = input("Play again? [y/n]: ")
                if roulette_continue == "n":
                    in_roulette = False

        elif answers["games"] == "Blackjack":
            print("Blackjack game loading...")
            time.sleep(1)
            in_blackjack = True
            while in_blackjack:
                blackjack(session, user)
                blackjack_continue = input("Play again? [y/n]: ")
                if blackjack_continue == "n":
                    in_blackjack = False

        elif answers["games"] == "Update Username":
            new_name = input("Please enter your new username: ")
            user.username = new_name
            session.add(user)
            session.commit()

        elif answers["games"] == "Delete Account":
            session.delete(user)
            session.commit()
            in_game = False

        elif answers["games"] == "Exit the Casino":
            in_game = False

    
    print("Thanks for visiting Cyber Casino!")