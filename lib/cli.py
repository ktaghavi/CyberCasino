# lib/cli.py
from models.model_1 import Users, PlayedGames
from sqlalchemy.orm import (sessionmaker)
from sqlalchemy import create_engine
import inquirer
import time


from helpers import (
    exit_program,
    helper_1,
    slots
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            helper_1()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Play Roullette")
    print("1. Play Slots")



if __name__ == "__main__":
    engine = create_engine('sqlite:///casino.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    in_game = True

    while in_game:
        print("Thanks for coming to our casino")
        name = input("Please enter your name: ")
        user = session.query(Users).filter(Users.username == name).first()
        if user:
            print(f"Welcome back to Cyber Casino {user.username}!")
        else:
            print("Since your a lonely scum, we will start you with $1000")
            new_user = Users(username=name, balance=1000)
            session.add(new_user)
            session.commit()
        
        questions = [
        inquirer.List('games',
                        message="What Game do you want to play?",
                        choices=['slots', 'roullette', 'blackjack',"update username", "delete account", "exit the casino"],
                    ),
        ]
        answers = inquirer.prompt(questions)
        print(answers["games"])
        if answers["games"] == "slots":
            print("Slots game loading...")
            time.sleep(1)
            slots()

        elif answers["games"] == "update username":
            new_name = input("Please enter your new username: ")
            user.username = new_name
            session.add(user)
            session.commit()

        elif answers["games"] == "delete account":
            session.delete(user)
            session.commit()
            in_game = False

        elif answers["games"] == "exit the casino":
            in_game = False

        
        # in_game = False

    print("Thanks for visiting our casino")


