from Card import Card
from Suit import Suit
from Rank import Rank
from Deck import Deck
from Hand import Hand


class Player:
    def __init__(self, name=None):
        self.name = name
        self.hand = None
        self.bet = 0
        self.tricks_won = 0
        self.score = 0
        self.dealer = False

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_hand(self):
        return self.hand

    def set_bet(self, bet):
        self.bet = bet

    def get_bet(self):
        return self.bet

    def add_trick(self, num_tricks):
        self.tricks_won += num_tricks

    def get_tricks_won(self):
        return self.tricks_won
    
    def set_tricks_won(self, tricksWon):
        self.tricks_won = tricksWon

    def add_to_score(self, points):
        self.score += points

    def get_score(self):
        return self.score

    @property
    def is_dealer(self):
        return self.dealer

    def set_dealer(self, is_dealer):
        self.dealer = is_dealer