public class Player {
    private Hand hand;
    private boolean isDealer;
    private int tricksWon;
    private int bet;
    private int score;

    public Player() {
        hand = new Hand();
        isDealer = false;
        tricksWon = 0;
        bet = 0;
        score = 0;
    }

    public Hand getHand() {
        return hand;
    }

    public boolean isDealer() {
        return isDealer;
    }

    public void setDealer(boolean dealer) {
        isDealer = dealer;
    }

    public int getTricksWon() {
        return tricksWon;
    }

    public void setTricksWon(int tricksWon) {
        this.tricksWon = tricksWon;
    }

    public void addTrick(int trick) {
        tricksWon += trick;
    }

    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }

    public int getScore() {
        return score;
    }

    public void addToScore(int points) {
        score += points;
    }
}