public class Card {
    // Enumerations
    public enum Rank {
        ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING
    }

    public enum Suit {
        SPADES, DIAMONDS, CLUBS, HEARTS
    }

    // Fields
    private Rank rank;
    private Suit suit;

    // Constructor
    public Card(Rank rank, Suit suit) {
        this.rank = rank;
        this.suit = suit;
    }

    // Getters and Setters
    public Rank getRank() {
        return rank;
    }

    public void setRank(Rank rank) {
        this.rank = rank;
    }

    public Suit getSuit() {
        return suit;
    }

    public void setSuit(Suit suit) {
        this.suit = suit;
    }

    // toString method
    @Override
    public String toString() {
        return rank + " of " + suit;
    }
}