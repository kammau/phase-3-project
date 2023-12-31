#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db.models import Player, Card, Deck

from subfunctions.cardSubfunctions import (add_new_card, update_card, remove_card)
from subfunctions.deckSubfunctions import (add_new_deck, update_deck, remove_deck)

def add_data(info):
    session.add(info)
    session.commit()

class PokemonCli:
    def __init__(self):
        self.login()

    def login(self):
        user = input("Please enter your username: ")
        usernames = [name.username for name in session.query(Player)]
        if user in usernames:
            self.main_menu(user)
        else:
            sign_up = input("Looks like your new here, do you want to sign up? (y/n) ")
            if sign_up == "y":
                self.sign_up()
            elif sign_up == "n":
                print("Ok, have a good day!")

    
    def sign_up(self):
        username = input("Please enter a username: ")
        level = input("Please specify a playing level (Beginner, Intermediate, Advanced): ")
        add_data(Player(level=level, username=username))
        self.main_menu(username)

    def main_menu(self, user): 
        print(f"\nWelcome {user}! Please select an option:")
        options = input('c) Look through Card collection \n'
            'd) Look through Deck collection \n'
            'q) Quit program \n')
        
        if options == "c":
            self.card_collection(user)
        elif options == "d":
            self.deck_collection(user)
        elif options == "q":
            print(f"Have a good day {user}!")
        else:
            print("Please type a valid number! \n")
            self.main_menu(user)
        
    def card_collection(self, user):
        user_id = [player.id for player in session.query(Player) if player.username == user]
        cards = [card for card in session.query(Card) if card.player_id in user_id]
        if len(cards) > 0:
            print(f"Here are all the cards in you collection {user}: \n")
            for card in cards:
                print(f"Card ID: {card.id} \n"
                f"Card Name: {card.card_name} \n"
                f"HP: {card.hp} \n"
                f"Type: {card.pokemon_type} \n")
        else:
            print("\nLooks like you don't have any cards in your collection!\n")

        options = input("What would you like to do next?: \n"
            "(u) Update a card \n"
            "(r) Remove a card \n"
            "(a) Add a card \n"
            "(m) Go to Main Menu \n")
        
        if options == "a":
            add_new_card(session, user_id, self.card_collection)
        elif options == "u":
            update_card(session, user_id, self.card_collection)
        elif options == "r":
            remove_card(session, user_id, self.card_collection)
        elif options == "m":
            self.main_menu(user)
            

    
    def deck_collection(self, user):
        user_id = [player.id for player in session.query(Player) if player.username == user]
        decks = [deck for deck in session.query(Deck) if deck.player_id in user_id]
        if len(decks) > 0:
            print(f"Here are all the decks in your collection {user}: \n")
            for deck in decks:
                print(f"Deck ID: {deck.id} \n"
                f"Deck Name: {deck.deck_name} \n"
                f"Deck Set: {deck.set_name} \n")
        else:
            print("\nLooks like you don't have any decks in your collection!\n")

        options = input("What would you like to do next?: \n"
        "(a) Add a Deck \n"
        "(r) Remove a Deck \n"
        "(u) Update a Deck \n"
        "(m) Go to Main Menu \n")

        if options == "a":
            add_new_deck(session, user_id, self.deck_collection)
        elif options == "r":
            remove_deck(session, user_id, self.deck_collection)
        elif options == "u":
            update_deck(session, user_id, self.deck_collection)
        elif options == "m":
            self.main_menu(user)


if __name__ == "__main__":
    engine = create_engine("sqlite:///db/cards.db") # home base for the database
    session = Session(engine, future=True)
    PokemonCli()

