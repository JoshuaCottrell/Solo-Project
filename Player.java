import java.util.ArrayList;
import java.util.List;

public class Player {
    // Fields
    private List<Card> hand;
    private int score;
    private int bet;
    private int tricksWon;

    // Constructor
    public Player() {
        hand = new ArrayList<>();
        score = 0;
        bet = 0;
        tricksWon = 0;
    }

    // Getters and Setters
    public List<Card> getHand() {
        return hand;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }

    public int getBet() {
        return bet;
    }

    public void setBet(int bet) {
        this.bet = bet;
    }

    public int getTricksWon() {
        return tricksWon;
    }

    public void setTricksWon(int tricksWon) {
        this.tricksWon = tricksWon;
    }

    // Add a card to the player's hand
    public void addCardToHand(Card card) {
        hand.add(card);
    }

    // Remove a card from the player's hand
    public void removeCardFromHand(Card card) {
        hand.remove(card);
    }

    // Clear the player's hand
    public void clearHand() {
        hand.clear();
    }
}