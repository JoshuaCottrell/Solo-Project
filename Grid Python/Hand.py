import sys
from Card import Card
from Suit import Suit
from Rank import Rank
from Deck import Deck
import pygame

class Hand:
    def __init__(self):
        self.cards = []
        self.card_images = []

    def add_card(self, card):
        self.cards.append(card)
        self.card_images.append(card.image)

    def remove_card(self, card):
        self.cards.remove(card)
        self.card_images.remove(card.image)

    def get_cards(self):
        return self.cards

    def draw(self, surface, x, y):
        for i, card_image in enumerate(self.card_images):
            surface.blit(card_image, (x + i * 20, y))