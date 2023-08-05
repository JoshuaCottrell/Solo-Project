from Card import Card
from Suit import Suit
from Rank import Rank
from Deck import Deck
from Hand import Hand
import pygame

class Player:
    def __init__(self, name=None):
        self.name = name
        self.hand = Hand()
        self.bet = 0
        self.tricks_won = 0
        self.score = 0
        self.dealer = False

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_hand(self, hand):
        self.hand = hand

    def get_hand(self):
        return self.hand

    def set_bet(self, bet):
        self.bet = bet

    def get_bet(self):
        return self.bet

    def add_trick(self, amount=1):
        self.tricks_won += amount

    def get_tricks_won(self):
        return self.tricks_won

    def set_tricks_won(self, tricks):
        self.tricks_won = tricks

    def add_to_score(self, amount):
        self.score += amount

    def get_score(self):
        return self.score

    def is_dealer(self):
        return self.dealer

    def set_dealer(self, is_dealer):
        self.dealer = is_dealer

    def draw_hand(self, surface, x, y):
        self.hand.draw(surface, x, y)