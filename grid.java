public class Grid {
    // Enumeration for round
    public enum Round {
        ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, SEVEN_NT, SEVEN_B
    }

    // Fields
    private Round round;
    private int numberOfPlayers;
    private boolean halfway;
    private boolean gameEnded;

    // Constructor
    public Grid(int numberOfPlayers) {
        round = Round.ONE;
        this.numberOfPlayers = numberOfPlayers;
        halfway = false;
        gameEnded = false;
    }

    // Getters and Setters
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
    }

    // Increment or decrement the round by 1
    public void incrementRound() {
        int currentRound = round.ordinal();
        if (halfway) {
            round = Round.values()[currentRound - 1];
            if (round == Round.ONE) {
                gameEnded = true;
            }
        }
        else {
            round = Round.values()[currentRound + 1];
            if (round == Round.SEVEN_B) {
                halfway = true;
            }
        }
    }
}