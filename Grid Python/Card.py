from Suit import Suit
from Rank import Rank
import pygame
from pygame.locals import *

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image = None

    def load_image(self):
        card_name = f"{self.rank.name.lower()}_of_{self.suit.name.lower()}.png"
        self.image = pygame.image.load(f"Grid Python/Images/cards/{card_name}")

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, surface, x, y):
        if self.image is not None:
            surface.blit(self.image, (x, y))