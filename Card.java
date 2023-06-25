public class Card {
    // Enumerations
    public enum Rank {
        TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING, ACE
    }

    public enum Suit {
        HEARTS, SPADES, CLUBS, DIAMONDS
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