import java.util.ArrayList;

public class Player {
    // Fields
    private ArrayList<Card> hand;
    private int score;
    private int bet;
    private int tricksWon;
    private String playerName;

    // Constructor
    public Player(String playerName) {
        hand = new ArrayList<Card>();
        score = 0;
        bet = 0;
        tricksWon = 0;
        this.playerName = playerName;

    }

    // Getters and Setters
    public String getName() {
        return playerName;
    }

    public void setName(String playerName) {
        this.playerName = playerName;
    }

    public ArrayList<Card> getHand() {
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

    public void printHand() {
        System.out.println(playerName + "'s hand:");
        for (int i = 0; i < hand.size(); i++) {
          System.out.println((i + 1) + ". " + hand.get(i));
        }
    }

    public Card playCard(int index, Card.Suit leadSuit) {
        if (index < 0 || index >= hand.size()) {
            throw new IllegalArgumentException("Invalid index: " + index);
        }
        Card card = hand.get(index);
        if (card.getSuit() != leadSuit) {
            boolean hasSuit = false;
            for (Card c : hand) {
                if (c.getSuit() == leadSuit) {
                    hasSuit = true;
                    break;
                }
            }
            if (hasSuit) {
                throw new IllegalArgumentException("You must play a card of the lead suit (" + leadSuit + ")");
            }
        }
        hand.remove(index);
        return card;
    }
}