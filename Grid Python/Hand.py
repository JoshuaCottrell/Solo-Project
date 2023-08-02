import sys
from Card import Card
from Suit import Suit
from Rank import Rank
from Deck import Deck

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)
        return card

    def get_cards(self):
        return self.cards

    def print_playable_cards(self, suit, first):
        if first:
            print("Playable Cards:")
            self.print_hand()
            print("Enter the number of the card you want to play: ")
            selected_card = self.cards[int(input()) - 1]
            print("You played:", selected_card)
            self.cards.remove(selected_card)
            return selected_card

        print("Playable Cards:")
        playable_cards = [card for card in self.cards if card.get_suit() == suit]
        if not playable_cards:
            playable_cards = self.cards

        for i, card in enumerate(playable_cards):
            print(f"{i + 1}. {card}")

        print("Enter the number of the card you want to play: ")
        choice = int(input())
        while not (1 <= choice <= len(playable_cards)):
            print("Invalid choice! Please try again")
            choice = int(input())

        selected_card = playable_cards[choice - 1]
        print("You played:", selected_card)
        self.cards.remove(selected_card)
        return selected_card

    def print_hand(self):
        for i, card in enumerate(self.cards):
            print(f"{i + 1}. {card}")

    def empty_hand(self):
        self.cards.clear()