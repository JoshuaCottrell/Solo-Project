from Suit import Suit
from Rank import Rank
import pygame
from pygame.locals import *

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image = None
        self.rect = None
        self.card_width = 100
        self.card_height = 140

    def load_image(self):
        card_name = f"{self.rank.name.lower()}_of_{self.suit.name.lower()}.png"
        self.image = pygame.image.load(f"Grid Python/Images/cards/{card_name}")
        self.image = pygame.transform.scale(self.image, (self.card_width, self.card_height))
        self.rect = self.image.get_rect()  # Set the rect attribute


    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, surface, x, y):
        if self.image is not None:
            surface.blit(self.image, (x, y))