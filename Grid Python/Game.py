from Card import Card
from Suit import Suit
from Rank import Rank
from Rounds import Rounds
from Deck import Deck
from Hand import Hand
from Player import Player
import sys
import pygame
from pygame.locals import *

class Game:
    def __init__(self):
        self.players = []
        self.deck = Deck()
        self.deck.shuffle()
        self.trump_card = None
        self.input_text = ""
        pygame.init()
        window_width = 1280
        window_height = 720
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
        font = pygame.font.Font(None, 50)
        prompt_text = font.render("Enter the number of players:", True, (0, 0, 0))
        prompt_rect = prompt_text.get_rect(center=(self.window.get_width() // 2, 100))
        self.window.blit(prompt_text, prompt_rect)

        # Calculate the center position of the input box
        input_x = self.window.get_width() // 2 - 100
        input_y = 150

        # Draw the input box
        pygame.draw.rect(self.window, (0, 0, 0), (input_x, input_y, 200, 42), 2)

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
        # Clear the previous elements
        self.window.fill((255, 255, 255))

        # Load the background image
        background_image = pygame.image.load("Grid Python/Images/table_top.png")

        # Scale the background image to fit the size of the game window
        background_image = pygame.transform.scale(background_image, (self.window.get_width(), self.window.get_height()))

        # Draw the background image
        self.window.blit(background_image, (0, 0))

        # Calculate the center position of the deck
        deck_x = self.window.get_width() // 2 + 200
        deck_y = self.window.get_height() // 2 - 100

        # Resize the deck image to a smaller size
        deck_width = 100
        deck_height = 140

        # Draw deck
        deck_image = pygame.image.load("Grid Python/Images/card_back.png")
        deck_image = pygame.transform.scale(deck_image, (deck_width, deck_height))
        self.window.blit(deck_image, (deck_x, deck_y))

        # Calculate the position of the trump card
        trump_x = deck_x - 10
        trump_y = deck_y

        # Resize the trump card image to a smaller size
        trump_width = 100
        trump_height = 140

        # Draw trump card
        trump_image = pygame.transform.scale(self.trump_card.image, (trump_width, trump_height))
        self.window.blit(trump_image, (trump_x, trump_y))

        # Display each player's card near the bottom of the screen
        card_x = 50
        card_y = self.window.get_height() - 200
        card_spacing = 110

        # Resize the card image to a smaller size
        card_width = 100
        card_height = 140

        # Draw the player's card with the resized image
        player_hand = self.players[0].get_hand()
        for i, card in enumerate(player_hand.get_cards()):
            card_image = pygame.transform.scale(card.image, (card_width, card_height))
            self.window.blit(card_image, (card_x + i * card_spacing, card_y))


        # Update the display
        pygame.display.update()


    
    def deal_round(self, players, round):
        if round.value >= 7:
            num_cards = 7
        else:
            num_cards = round.value

        for player in players:
            for i in range(num_cards):
                card = self.deck.draw_card()
                player.get_hand().add_card(card)
        return



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

        # Deal the first round to each player
        self.deal_round(self.players, Rounds.ONE)

        # Calculate trump
        self.trump_card = self.deck.draw_card()

        clock = pygame.time.Clock()
        running = True

        while running:
            self.handle_events()

            self.draw_game()

            clock.tick(240)

        pygame.quit()