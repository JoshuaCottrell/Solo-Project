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
        self.current_player_index = 0
        self.winning_card = None
        self.winning_card_player = None
        self.turn_first_player = None
        self.descend_rounds = False
        self.new_round = True
        self.running = True
        self.loop_bets = None
        self.total_bets = 0
        self.first_card = None
        self.dealer_index = 0
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
                            if (self.winning_card): # If there is already a winning card
                                if (card == self.compare_card(card)): # And the card clicked beats it
                                    # create a copy and move it to the middle of the screen
                                    card_copy = Card(card.suit, card.rank)
                                    card_copy.load_image()
                                    self.winning_card = card_copy
                                    self.winning_card_player = self.current_player
                            else:
                                # create a copy and move it to the middle of the screen
                                self.turn_first_player = self.current_player
                                card_copy = Card(card.suit, card.rank)
                                card_copy.load_image()
                                self.winning_card = card_copy
                                self.first_card = card_copy
                                self.winning_card_player = self.current_player

                            # Remove card
                            self.current_player.get_hand().remove_card(card)

                            # Go to next player
                            self.current_player_index = (self.current_player_index + 1) % len(self.players)
                            self.current_player = self.players[self.current_player_index]

                            # If every player has played a card, reset round
                            if self.current_player == self.turn_first_player:
                                self.winning_card_player.add_trick()
                                self.winning_card = None
                                self.winning_card_player = None
                                self.first_card = None

                                # If players have no cards left, reset and go to next round
                                if len(self.current_player.get_hand().get_cards()) == 0:
                                    self.new_round = True
                                    # If Blind, start descending
                                    if (self.round == Rounds.BLIND):
                                        self.descend_rounds = True
                                        self.round = Rounds(self.round.value - 1)
                                    # If One and Descending, end the game
                                    elif (self.round == Rounds.ONE and self.descend_rounds):
                                        self.running = False
                                    elif (self.descend_rounds == False):
                                        self.round = Rounds(self.round.value + 1)
                                    else:
                                        self.round = Rounds(self.round.value - 1)

                                    # Reset for new round
                                    self.deck = Deck()
                                    self.deck.shuffle()
                                    self.trump_card = self.deck.draw_card()
                                    if self.round.value > 7:
                                        round_score = 7
                                    else:
                                        round_score = self.round.value
                                    for player in self.players:
                                        if player.get_bet() == player.get_tricks_won():
                                            player.add_to_score(player.get_bet() + round_score)
                                        player.set_tricks_won(0)
                                    # Set new dealer and first player
                                    self.players[self.dealer_index].set_dealer(False)
                                    self.dealer_index = (self.dealer_index + 1) % len(self.players)
                                    self.players[self.dealer_index].set_dealer(True)
                                    self.current_player_index = (self.dealer_index + 1) % len(self.players)
                                        

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

        # Draw submit information
        submit_text = font.render("Press ENTER to submit", True, (0, 0, 0))
        submit_text_rect = submit_text.get_rect(center = (self.window.get_width() // 2, 250))
        self.window.blit(submit_text, submit_text_rect)

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

        #Draw trump text
        font = pygame.font.Font(None, 30)
        trump_text = font.render(f"Trump: {self.trump_card.get_suit()}", True, (0, 0, 0))
        trump_text_rect = trump_text.get_rect(center=(self.window.get_width() // 2 + 250, self.window.get_height() // 2 - 120))
        self.window.blit(trump_text, trump_text_rect)

    def draw_info(self):
        # Draw current player
        font = pygame.font.Font(None, 50)
        curr_player_text = font.render(f"{self.current_player.get_name()}", True, (0, 0, 0))
        curr_player_text_rect = curr_player_text.get_rect(center=(100, 50))
        self.window.blit(curr_player_text, curr_player_text_rect)

        # Draw tricks won
        tricks_won_text = font.render(f"Tricks Won: {self.current_player.get_tricks_won()}", True, (0, 0, 0))
        tricks_won_text_rect = tricks_won_text.get_rect(center = (120, 100))
        self.window.blit(tricks_won_text, tricks_won_text_rect)

        # Draw Bet
        bet_text = font.render(f"Bet: {self.current_player.get_bet()}", True, (0, 0, 0))
        bet_text_rect = bet_text.get_rect(center = (120, 150))
        self.window.blit(bet_text, bet_text_rect)

        # Draw Total Score
        bet_text = font.render(f"Score: {self.current_player.get_score()}", True, (0, 0, 0))
        bet_text_rect = bet_text.get_rect(center = (120, 200))
        self.window.blit(bet_text, bet_text_rect)

        # Draw Round
        round_text = font.render(f"Round: {self.round}", True, (0, 0, 0))
        if self.round != Rounds.NO_TRUMP:
            round_text_rect = round_text.get_rect(center = (120, 250))
        else:
            round_text_rect = round_text.get_rect(center = (150, 250))
        self.window.blit(round_text, round_text_rect)
            

        #Draw winning card and winning card player
        font = pygame.font.Font(None, 30)
        winning_card_text = font.render("Winning Card", True, (0, 0, 0))
        winning_card_text_rect = winning_card_text.get_rect(center=(self.window.get_width() // 2 + 50, self.window.get_height() // 2 - 120))
        self.window.blit(winning_card_text, winning_card_text_rect)
        if (self.winning_card_player):
            winning_card_player_text = font.render(f"Played By: {self.winning_card_player.get_name()}", True, (0, 0, 0))
        else:
            winning_card_player_text = font.render("Played By: ", True, (0, 0, 0))
        winning_card_player_text_rect = winning_card_player_text.get_rect(center=(self.window.get_width() // 2 + 50, self.window.get_height() // 2 + 60))
        self.window.blit(winning_card_player_text, winning_card_player_text_rect)
        
    def draw_players_hand(self):
        # Display each player's card near the bottom of the screen
        card_x = 50
        card_y = self.window.get_height() - 200
        card_spacing = 110

        valid_cards = []
        if self.first_card:
            for card in self.current_player.get_hand().get_cards():
                if card.get_suit() == self.first_card.get_suit():
                    valid_cards.append(card)

        # Draw the player's cards
        # If they have cards matching the suit of the first card played, only show those cards
        if len(valid_cards) > 0:
            for i, card in enumerate(valid_cards):
                card.rect.center = (card_x + i * card_spacing, card_y)
                self.window.blit(card.image, (card_x + i * card_spacing, card_y))
        # Otherwise show all cards
        else:
            for i, card in enumerate(self.current_player.get_hand().get_cards()):
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


    def get_bets(self):
        # Draw player name
        font = pygame.font.Font(None, 50)
        curr_player_text = font.render(f"{self.current_player.get_name()}", True, (0, 0, 0))
        curr_player_text_rect = curr_player_text.get_rect(center=(100, 50))
        self.window.blit(curr_player_text, curr_player_text_rect)

        # Draw the input prompt
        font = pygame.font.Font(None, 50)
        prompt_text = font.render("Enter your bet for this round:", True, (0, 0, 0))
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

        # Draw Round
        submit_text = font.render(f"Round: {self.round}", True, (0, 0, 0))
        submit_text_rect = submit_text.get_rect(center = (self.window.get_width() // 2, 250))
        self.window.blit(submit_text, submit_text_rect)


    def handle_bets(self):
         for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN:
                    # Check valid bet
                    max_bet = self.round.value
                    if max_bet > 7:
                        max_bet = 7
                    if int(self.input_text) > max_bet:
                        self.input_text = ""
                        break
                    elif self.current_player.is_dealer() and int(self.input_text) + self.total_bets == max_bet:
                        self.input_text = ""
                        break
                    else:
                        self.current_player.set_bet(int(self.input_text))
                        self.total_bets += int(self.input_text)

                    # End loop on dealer
                    if self.current_player.is_dealer():
                        self.loop_bets = False
                    else:
                        # Prompt next player
                        self.current_player_index = (self.current_player_index + 1) % len(self.players)
                        self.current_player = self.players[self.current_player_index]
                    # Reset input text
                    self.input_text = ""
                elif event.key == K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode


    def get_bets_loop(self):
        clock = pygame.time.Clock()
        self.loop_bets = True
        self.input_text = ""
        while self.loop_bets:
            self.handle_bets()

            self.draw_background()

            if (self.round != Rounds.BLIND):
                self.draw_players_hand()
            
            if (self.round != Rounds.NO_TRUMP):
                self.draw_trump()

            self.get_bets()

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

        # Set dealer
        self.players[self.dealer_index].set_dealer(True)

        # Set first player
        self.current_player_index = (self.dealer_index + 1) % len(self.players)
        self.current_player = self.players[self.current_player_index]



        clock = pygame.time.Clock()

        while self.running:

            if self.new_round:
                self.deal_round()
                self.get_bets_loop()
                self.new_round = False

            self.handle_events()

            self.draw_background()

            self.draw_deck()

            if self.round != Rounds.NO_TRUMP:
                self.draw_trump()

            self.draw_info()

            self.draw_players_hand()

            self.draw_winning_card()

            pygame.display.update()

            clock.tick(240)

        pygame.quit()
        print("Thanks for playing!")
        sys.exit()