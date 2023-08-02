from Card import Card
from Suit import Suit
from Rank import Rank
from Rounds import Rounds
from Deck import Deck
from Hand import Hand
from Player import Player

import enum
import sys

class Game:
    def __init__(self):
        num_players = self.prompt_num_players()
        self.players = [Player() for _ in range(num_players)]
        self.create_players()
        self.prompt_player_names()
        self.dealer_index = 0
        self.current_player_index = self.dealer_index + 1

    def prompt_num_players(self):
        print("Enter the number of players: ")
        return int(input())

    def create_players(self):
        for player in self.players:
            player.hand = Hand()

    def prompt_player_names(self):
        for i, player in enumerate(self.players):
            print(f"Enter the name for Player {i + 1}: ")
            name = input()
            player.set_name(name)

    def get_players(self):
        return self.players

    def start_round(self, round):
        # Set the dealer for the first round
        self.players[self.dealer_index].set_dealer(True)

        # Print Round
        print(f"Round {round} - Dealer: {self.players[self.dealer_index].get_name()}")

        # Get cards and maxBet
        num_cards = round.value + 1
        if num_cards > 7:
            num_cards = 7

        # Clear all players hands and then distribute new cards to each player
        deck = Deck()
        deck.shuffle()
        for player in self.players:
            player.get_hand().empty_hand()
            for _ in range(num_cards):
                card = deck.draw_card()
                player.get_hand().add_card(card)

        trump = Suit.CLUBS
        # Get Trump
        if round != Rounds.NO_TRUMP:
            trump = deck.draw_card().get_suit()

        # Get bets from all players
        total_bet = 0
        for _ in range(len(self.players)):
            current_player = self.players[self.current_player_index]
            # If not blind, print hand first
            if round != Rounds.BLIND:
                print("Current Hand:")
                current_player.get_hand().print_hand()
            if round!= Rounds.NO_TRUMP:
                print("Trump:", trump)
            # Get bet from the player
            current_player.set_bet(self.prompt_bet(0, num_cards, current_player, total_bet))
            total_bet += current_player.get_bet()
            # Move to the next player
            self.current_player_index = (self.current_player_index + 1) % len(self.players)

        # Start playing the round
        winning_player = self.players[self.current_player_index]  # Starts as left of dealer
        winning_player_index = self.current_player_index
        winning_card = Card(Suit.CLUBS, Rank.ACE)  # Placeholder card, card values don't matter.
        lead_card = Card(Suit.CLUBS, Rank.ACE)  # Placeholder card, card values don't matter.
        for _ in range(num_cards):
            for _ in range(len(self.players)):
                current_player = self.players[self.current_player_index]
                # Play turn
                print()
                print(current_player.get_name() + ":")
                if current_player == winning_player:  # First player sets lead
                    lead_card = current_player.get_hand().print_playable_cards(lead_card.get_suit(), True)
                    winning_card = lead_card
                else:  # Non-first player turn
                    card = current_player.get_hand().print_playable_cards(lead_card.get_suit(), False)
                    if self.compare_card(winning_card, card, trump, round) == card:
                        winning_player = current_player
                        winning_player_index = self.current_player_index
                        winning_card = card
                print()
                print("Winning card:", winning_card)
                print("Played by:", winning_player.get_name())
                # Move to the next player
                self.current_player_index = (self.current_player_index + 1) % len(self.players)
            winning_player.add_trick(1)
            print(winning_player.get_name() + " wins that trick!")
            self.current_player_index = winning_player_index

        # Calculate score for the round
        for player in self.players:
            if player.get_bet() == player.get_tricks_won():
                player.add_to_score(num_cards + player.get_bet())
            player.set_tricks_won(0)
            player.set_bet(0)

    def prompt_bet(self, min_bet, max_bet, player, total_bet):
        bet = None
        while True:
            print(player.get_name() + ", enter your bet (between", min_bet, "and", max_bet, "): ")
            bet = int(input())
            if bet < min_bet or bet > max_bet:
                print("Invalid bet. Please enter a bet between", min_bet, "and", max_bet, ".")
            if player.is_dealer and (bet + total_bet == max_bet):
                print("Invalid bet. The dealer cannot bet such that everyone wins.")
            else:
                break
        return bet

    def compare_card(self, winning_card, new_card, trump, cur_round):
        if new_card.get_suit() == winning_card.get_suit():
            if new_card.get_rank().value > winning_card.get_rank().value:
                return new_card
        elif new_card.get_suit() == trump:  # If both are trump previous if statement accounts for it
            if cur_round != Rounds.NO_TRUMP:  # Do nothing if this is a no trump round
                return new_card
        return winning_card

    def main(self):
        players = self.get_players()

        print()
        print("Number of players:", len(players))
        for i, player in enumerate(players):
            print(f"Player {i + 1}: {player.get_name()}")
        print()

        # Play to blind
        for i in range(8, len(Rounds)+1):
            self.start_round(Rounds(i))

        # Play to 1
        for i in range(len(Rounds)-1, 8, -1):
            self.start_round(Rounds(i))

        # Print Results
        winner = players[0]  # Random initialization, doesn't matter.
        top_score = 0
        winners = []
        for player in players:
            if player.get_score() > top_score:
                top_score = player.get_score()
                winner = player
                winners.append(winner)
            elif player.get_score() == top_score:
                winners.append(player)
        if len(winners) > 1:
            winnersNames = [winer.get_name() for winer in winners]
            names_with_and = " and ".join(winnersNames)
            print(f"{names_with_and} win with the scores of {top_score}!")
        else:
            print(f"{winner.get_name()} wins with a score of {top_score}!")
        # TODO: Account for ties and such.
        # TODO: Print Scoreboard/Leaderboard

if __name__ == "__main__":
    game = Game()
    game.main()