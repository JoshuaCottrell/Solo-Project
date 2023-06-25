import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Deck {
    // Fields
    private List<Card> cards;

    // Constructor
    public Deck() {
        cards = new ArrayList<>();
        initializeDeck();
        shuffle();
    }

    // Initialize the deck with 52 cards
    private void initializeDeck() {
        for (Card.Suit suit : Card.Suit.values()) {
            for (Card.Rank rank : Card.Rank.values()) {
                cards.add(new Card(rank, suit));
            }
        }
    }

    // Getters
    public List<Card> getCards() {
        return cards;
    }

    // Shuffle the deck
    public void shuffle() {
        Collections.shuffle(cards);
    }

    // Deal a card from the deck
    public Card dealCard() {
        if (cards.isEmpty()) {
            return null; // No more cards in the deck
        }
        return cards.remove(cards.size() - 1);
    }

    // Print all the cards in the deck
    public void printCards() {
        for (Card card : cards) {
            System.out.println(card);
        }
    }
}