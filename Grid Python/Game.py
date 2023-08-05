from Card import Card
from Suit import Suit
from Rank import Rank
from Rounds import Rounds
from Deck import Deck
from Hand import Hand
from Player import Player
import enum
import sys
import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.players = []
        self.input_text = ""
        pygame.init()
        window_width = 800
        window_height = 600
        self.window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Card Game")


    def handle_player_prompt(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.run()
                elif event.key == K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def prompt_players(self):

        # Load the background image
        background_image = pygame.image.load("Grid Python/Images/table_top.png")

        # Scale the background image to fit the size of the game window
        background_image = pygame.transform.scale(background_image, (self.window.get_width(), self.window.get_height()))

        self.window.blit(background_image, (0, 0))

        # Draw the input prompt
        font = pygame.font.Font(None, 36)
        prompt_text = font.render("Enter the number of players:", True, (0, 0, 0))
        prompt_rect = prompt_text.get_rect(center=(self.window.get_width() // 2, 100))
        self.window.blit(prompt_text, prompt_rect)

        # Calculate the center position of the input box
        input_x = self.window.get_width() // 2 - 100
        input_y = 150

        # Draw the input box
        pygame.draw.rect(self.window, (0, 0, 0), (input_x, input_y, 200, 30), 2)

        # Draw the entered text
        text_surface = font.render(self.input_text, True, (0, 0, 0))
        self.window.blit(text_surface, (input_x + 5, input_y + 5))

        # Calculate the center position of the button
        button_x = self.window.get_width() // 2 - 50
        button_y = 200

        # Draw the button
        pygame.draw.rect(self.window, (0, 0, 0), (button_x, button_y, 100, 50), 2)
        button_text = font.render("Start", True, (0, 0, 0))
        button_rect = button_text.get_rect(center=(button_x + 50, button_y + 25))
        self.window.blit(button_text, button_rect)

    def draw_game(self):
        # Load the background image
        background_image = pygame.image.load("Grid Python/Images/table_top.png")

        # Scale the background image to fit the size of the game window
        background_image = pygame.transform.scale(background_image, (self.window.get_width(), self.window.get_height()))

        self.window.blit(background_image, (0, 0))



    def start_game(self):

        clock = pygame.time.Clock()
        prompting = True
        while prompting:
            self.handle_player_prompt()

            # Draw game objects on the screen
            self.prompt_players()

            pygame.display.update()
            clock.tick(240)
        

    def run(self):

        # Get the number of players from the input text
        num_players = int(self.input_text)

        # Create players based on the number of players
        for i in range(num_players):
            player_name = f"Player {i+1}"
            player = Player(player_name)
            self.players.append(player)

        clock = pygame.time.Clock()
        running = True

        while running:
            self.handle_events()

            self.draw_game()

            clock.tick(240)

        pygame.quit()