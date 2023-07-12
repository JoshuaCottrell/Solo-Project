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

        // Distribute cards to each player
        int numCards = round.ordinal() + 1;
        Deck deck = new Deck();
        deck.shuffle();
        for (Player player : players) {
            for (int i = 0; i < numCards; i++) {
                Card card = deck.drawCard();
                player.getHand().addCard(card);
            }
        }

        // Get bets from all players
        int totalBet = 0;
        for (int i = 0; i < players.length; i++) {
            Player currentPlayer = players[currentPlayerIndex];
            // Get bet from the player
            int maxBet = currentPlayer.getHand().getCards().size();
            currentPlayer.setBet(promptBet(0, maxBet, currentPlayer, totalBet));
            totalBet += currentPlayer.getBet();
            // Move to the next player
            currentPlayerIndex = (currentPlayerIndex + 1) % players.length;
        }

        // Start playing the round
        // TODO: Implement the logic for playing the round
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
            if (player.isDealer() && (bet + totalBet == player.getHand().getCards().size())) {
                System.out.println("Invalid bet. The dealer cannot bet such that everyone wins.");
            }
        } while (bet < minBet || bet > maxBet || (player.isDealer() && (bet + totalBet == player.getHand().getCards().size())));
        return bet;
    }

    public static void main(String[] args) {
        Game game = new Game();
        Player[] players = game.getPlayers();

        System.out.println("Number of players: " + players.length);
        for (int i = 0; i < players.length; i++) {
            System.out.println("Player " + (i + 1) + ": " + players[i].getName());
        }

        game.startRound(Rounds.ONE);
    }
}