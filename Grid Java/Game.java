import java.util.Scanner;

public class Game {
    private Player[] players;
    private int currentPlayerIndex;
    private int dealerIndex;
    

    public Game() {
        int numPlayers = promptNumPlayers();
        players = new Player[numPlayers];
        createPlayers();
        promptPlayerNames();
        dealerIndex = 0;
        currentPlayerIndex = dealerIndex + 1;
    }

    private int promptNumPlayers() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of players: ");
        return scanner.nextInt();
    }

    private void createPlayers() {
        for (int i = 0; i < players.length; i++) {
            players[i] = new Player();
        }
    }

    private void promptPlayerNames() {
        Scanner scanner = new Scanner(System.in);
        for (int i = 0; i < players.length; i++) {
            System.out.print("Enter the name for Player " + (i + 1) + ": ");
            String name = scanner.nextLine();
            players[i].setName(name);
        }
    }

    public Player[] getPlayers() {
        return players;
    }

    public void startRound(Rounds round) {
        // Set the dealer for the first round
        players[dealerIndex].setDealer(true);

        // Print Round
        System.out.println("Round " + round + " - Dealer: " + players[dealerIndex].getName());

        // Get cards and maxBet
        int numCards = round.ordinal() + 1;
        if (numCards > 7) {
            numCards = 7;
        }

        // Clear all players hands and then distribute new cards to each player
        Deck deck = new Deck();
        deck.shuffle();
        for (Player player : players) {
            player.getHand().emptyHand();
            for (int i = 0; i < numCards; i++) {
                Card card = deck.drawCard();
                player.getHand().addCard(card);
            }
        }

        Suit trump = Suit.CLUBS;
        // Get Trump
        if (round != Rounds.NO_TRUMP) {
            trump = deck.drawCard().getSuit();
        }

        // Get bets from all players
        int totalBet = 0;
        Player currentPlayer;
        for (int i = 0; i < players.length; i++) {
            currentPlayer = players[currentPlayerIndex];
            // If not blind, print hand first
            if (round != Rounds.BLIND) {
                System.out.println("Current Hand:");
                currentPlayer.getHand().printHand();
            }
            System.out.println("Trump: " + trump.toString());
            // Get bet from the player
            currentPlayer.setBet(promptBet(0, numCards, currentPlayer, totalBet));
            totalBet += currentPlayer.getBet();
            // Move to the next player
            currentPlayerIndex = (currentPlayerIndex + 1) % players.length;
        }

        // Start playing the round
        Player winningPlayer = players[currentPlayerIndex]; // Starts as left of dealer
        int winningPlayerIndex = currentPlayerIndex;
        Card winningCard = new Card(Suit.CLUBS, Rank.ACE); // Placeholder card, card values don't matter.
        Card leadCard = new Card(Suit.CLUBS, Rank.ACE); // Placeholder card, card values don't matter.
        Card card;
        for (int j = 0; j < numCards; j++) {
            for (int i = 0; i < players.length; i++) {
                currentPlayer = players[currentPlayerIndex];
                // Play turn
                System.out.println();
                System.out.println(currentPlayer.getName() + ":");
                if (currentPlayer == winningPlayer) { // First player sets lead
                    leadCard = currentPlayer.getHand().printPlayableCards(leadCard.getSuit(), true);
                    winningCard = leadCard;
                }
                else { // Non-first player turn
                    card = currentPlayer.getHand().printPlayableCards(leadCard.getSuit(), false);
                    if (compareCard(winningCard, card, trump, round) == card) {
                        winningPlayer = currentPlayer;
                        winningPlayerIndex = currentPlayerIndex;
                        winningCard = card;
                    }
                }
                System.out.println();
                System.out.println("Winning card: " + winningCard);
                System.out.println("Played by: " + winningPlayer.getName());
                // Move to the next player
                currentPlayerIndex = (currentPlayerIndex + 1) % players.length;
            }
            winningPlayer.addTrick(1);
            System.out.println(winningPlayer.getName() + " wins that trick!");
            currentPlayerIndex = winningPlayerIndex;
        }
        // Calculate score for the round
        for (Player player : players) {
             if (player.getBet() == player.getTricksWon()) {
                player.addToScore(numCards + player.getBet());
             }
             player.setTricksWon(0);
             player.setBet(0);
        }
        return;
    }

    private int promptBet(int minBet, int maxBet, Player player, int totalBet) {
        Scanner scanner = new Scanner(System.in);
        int bet;
        do {
            System.out.print(player.getName() + ", enter your bet (between " + minBet + " and " + maxBet + "): ");
            bet = scanner.nextInt();
            if (bet < minBet || bet > maxBet) {
                System.out.println("Invalid bet. Please enter a bet between " + minBet + " and " + maxBet + ".");
            }
            if (player.isDealer() && (bet + totalBet == maxBet)) {
                System.out.println("Invalid bet. The dealer cannot bet such that everyone wins.");
            }
        } while (bet < minBet || bet > maxBet || (player.isDealer() && (bet + totalBet == maxBet)));
        return bet;
    }

    private Card compareCard(Card winningCard, Card newCard, Suit trump, Rounds curRound) {
        if (newCard.getSuit() == winningCard.getSuit()) {
            if (newCard.getRank().ordinal() > winningCard.getRank().ordinal()) {
                return newCard;
            }
        }
        else if (newCard.getSuit() == trump) { // If both are trump previous if statement accounts for it
            if (curRound != Rounds.NO_TRUMP) { // Do nothing if this is a no trump round
                return newCard;
            }
        }
        return winningCard;
    }
    public static void main(String[] args) {
        Game game = new Game();
        Player[] players = game.getPlayers();

        System.out.println();
        System.out.println("Number of players: " + players.length);
        for (int i = 0; i < players.length; i++) {
            System.out.println("Player " + (i + 1) + ": " + players[i].getName());
        }
        System.out.println();

        // Play to blind
        for (int i = 6; i < Rounds.values().length; i++) {
            game.startRound(Rounds.values()[i]);
        }

        // Play to 1
        for (int i = Rounds.values().length-2; i >= 6; i--) {
            game.startRound(Rounds.values()[i]);
        }

        // Print Results
        Player winner = players[0]; // Random initialization, doesn't matter.
        int topScore = 0;
        for (Player player : players) {
            if (player.getScore() > topScore) {
                topScore = player.getScore();
                winner = player;
            }
        }
        System.out.println(winner.getName() + " wins with a score of " + topScore + "!");
        // TODO: Account for ties and such.
        // TODO: Print Scoreboard/Leaderboard
    }
}