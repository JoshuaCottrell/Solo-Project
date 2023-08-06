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
        self.round = Rounds.THREE
        self.current_player = None
        self.winning_card = None
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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button clicked
                    mouse_pos = pygame.mouse.get_pos()
                    for card in self.current_player.get_hand().get_cards(): # If a card was clicked
                        if card.rect.collidepoint(mouse_pos):
                            # Card clicked, see if it is new winning card
                            if (self.winning_card):
                                if (card == self.compare_card(card)):
                                    # create a copy and move it to the middle of the screen
                                    card_copy = Card(card.suit, card.rank)
                                    card_copy.load_image()
                                    self.winning_card = card_copy
                            else:
                                # create a copy and move it to the middle of the screen
                                    card_copy = Card(card.suit, card.rank)
                                    card_copy.load_image()
                                    self.winning_card = card_copy
                            self.current_player.get_hand().remove_card(card)
                            break

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

    def draw_background(self):
        # Clear the previous elements
        self.window.fill((255, 255, 255))

        # Load the background image
        background_image = pygame.image.load("Grid Python/Images/table_top.png")

        # Scale the background image to fit the size of the game window
        background_image = pygame.transform.scale(background_image, (self.window.get_width(), self.window.get_height()))

        # Draw the background image
        self.window.blit(background_image, (0, 0))

    def draw_deck(self):
        # Calculate the center position of the deck
        deck_x = self.window.get_width() // 2 + 200
        deck_y = self.window.get_height() // 2 - 100

        # Draw deck
        deck_image = pygame.image.load("Grid Python/Images/card_back.png")
        deck_image = pygame.transform.scale(deck_image, (100, 140))
        self.window.blit(deck_image, (deck_x, deck_y))

    def draw_trump(self):
        # Calculate the position of the trump card
        trump_x = self.window.get_width() // 2 + 190
        trump_y = self.window.get_height() // 2 - 100

        # Draw trump card
        self.trump_card.rect.center = (trump_x, trump_y)
        self.window.blit(self.trump_card.image, (trump_x, trump_y))

    def draw_info(self):
        # Draw current player
        font = pygame.font.Font(None, 50)
        prompt_text = font.render(f"{self.current_player.get_name()}", True, (0, 0, 0))
        prompt_rect = prompt_text.get_rect(center=(100, 50))
        self.window.blit(prompt_text, prompt_rect)

    def draw_players_hand(self):
        # Display each player's card near the bottom of the screen
        card_x = 50
        card_y = self.window.get_height() - 200
        card_spacing = 110

        # Draw the player's card with the resized image
        player_hand = self.players[0].get_hand()
        for i, card in enumerate(player_hand.get_cards()):
            card.rect.center = (card_x + i * card_spacing, card_y)
            self.window.blit(card.image, (card_x + i * card_spacing, card_y))

    def draw_winning_card(self):
        # Draw cards in middle
        if self.winning_card:
            self.winning_card.rect.center = (self.window.get_width() // 2, self.window.get_height() // 2 - 100)
            self.window.blit(self.winning_card.image, (self.window.get_width() // 2, self.window.get_height() // 2 - 100))

    def deal_round(self):
        if self.round.value >= 7:
            num_cards = 7
        else:
            num_cards = self.round.value

        for player in self.players:
            for i in range(num_cards):
                card = self.deck.draw_card()
                player.get_hand().add_card(card)
        self.round = Rounds(self.round.value+1) # Increment round by 1
        return

    def compare_card(self, new_card):
        if new_card.get_suit() == self.winning_card.get_suit():
            if new_card.get_rank().value > self.winning_card.get_rank().value:
                return new_card
        elif new_card.get_suit() == self.trump_card.get_suit():  # If both are trump previous if statement accounts for it
            if self.round != Rounds.NO_TRUMP:  # Do nothing if this is a no trump round
                return new_card
        return self.winning_card


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

        # Calculate trump
        self.trump_card = self.deck.draw_card()

        # Set first player
        self.current_player = self.players[0]

        new_round = True

        clock = pygame.time.Clock()
        running = True

        while running:

            if new_round:
                self.deal_round()
                new_round = False

            self.handle_events()

            self.draw_background()

            self.draw_deck()

            self.draw_trump()

            self.draw_info()

            self.draw_players_hand()

            self.draw_winning_card()

            pygame.display.update()

            clock.tick(240)

        pygame.quit()