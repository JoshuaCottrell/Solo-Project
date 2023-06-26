import java.util.ArrayList;
import java.util.Scanner;

public class Grid {
    // Enumeration for round
    public enum Round {
        ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, SEVEN_NT, SEVEN_B
    }

    // Fields
    private Round round;
    private int numberOfPlayers;
    private ArrayList<Player> players;
    private boolean halfway;
    private boolean gameEnded;
    private Deck deck;

    // Constructor
    public Grid(int numberOfPlayers) {
        round = Round.ONE;
        this.numberOfPlayers = numberOfPlayers;
        players = new ArrayList<Player>();
        halfway = false;
        gameEnded = false;
        deck = new Deck();
    }

    public void startGame() {
        Scanner s = new Scanner(System.in);
        String name;
        System.out.println("Welcome to Grid! Who are the players?");
        for (int i = 0; i < numberOfPlayers; i++) {
            System.out.println("Player " + (i+1) + ": ");
            name = s.nextLine();
            players.add(i, new Player(name));
        }
        System.out.println("Great! Let's start playing!");
        while(!gameEnded) {
            playRound();
            printGameState();
            incrementRound();
        }
        s.close();
    }

    public void playRound() {
        Player currentPlayer;
        if (round.ordinal() > 6) {
            // Give everyone cards
            for (int i = 0; i < numberOfPlayers; i++) {
                currentPlayer = players.get(i);
                for (int j = 0; j < round.ordinal()+1; j++) {
                    currentPlayer.addCardToHand(deck.dealCard());
                }
            }
            // Everyone Bets
            Scanner s = new Scanner(System.in);
            for (int i = 0; i < numberOfPlayers; i++) {
                currentPlayer = players.get(i);
                System.out.println("What do you bet, " + currentPlayer.getName() + "?");
                currentPlayer.setBet(s.nextInt());
            }

            // Play the round
            Card.Suit leadSuit = Card.Suit.CLUBS;
            int playCard;
            for (int i = 0; i < round.ordinal()+1; i++) {
                for (int j = 0; j < numberOfPlayers; j++) {
                    currentPlayer = players.get(i);
                    currentPlayer.printHand();
                    System.out.println("What card will you play?");
                    playCard = s.nextInt();
                    if (j == 0) {
                        leadSuit = currentPlayer.getHand().get(playCard).getSuit();
                    }
                    currentPlayer.playCard(playCard, leadSuit);
                    
                }
            }
            s.close();
        }
    }

    // Getters and Setters
    public void newDeck() {
        deck = new Deck();
        deck.shuffle();
    }

    public Round getRound() {
        return round;
    }

    public void setRound(Round round) {
        this.round = round;
    }

    public int getNumberOfPlayers() {
        return numberOfPlayers;
    }

    public void setNumberOfPlayers(int numberOfPlayers) {
        this.numberOfPlayers = numberOfPlayers;
    }

    public boolean isHalfway() {
        return halfway;
    }

    public void setHalfway(boolean halfway) {
        this.halfway = halfway;
    }

    public boolean isGameEnded() {
        return gameEnded;
    }

    public void setGameEnded(boolean gameEnded) {
        this.gameEnded = gameEnded;
    }

    // Print the current game state
    public void printGameState() {
        System.out.println("Current Round: " + round);
        System.out.println("Number of Players: " + numberOfPlayers);
        System.out.println("Halfway: " + halfway);
        System.out.println("Game Ended: " + gameEnded);
        System.out.println("Scoreboard: ");
        for (int i = 0; i < numberOfPlayers; i++) {
            System.out.println(players.get(i).getName() + ": " + players.get(i).getScore());
        }
    }

    // Increment or decrement the round by 1
    public void incrementRound() {
        int currentRound = round.ordinal();
        if (halfway) {
            if (round == Round.ONE) {
                gameEnded = true;
            }
            else {
                round = Round.values()[currentRound - 1];
            }
        }
        else {
            round = Round.values()[currentRound + 1];
            if (round == Round.SEVEN_B) {
                halfway = true;
            }
        }
    }

    // public Player playRound() {

    // }
}