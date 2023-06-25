import java.util.List;

public class Main {
    public static void main(String[] args) {
        // Create a new deck
        Deck deck = new Deck();

        // Print the deck
        System.out.println("Deck:");
        deck.printCards();

        // Shuffle the deck
        deck.shuffle();

        // Print the shuffled deck
        System.out.println("\nShuffled Deck:");
        deck.printCards();

        // Check if the deck is correct
        if (isCorrectDeck(deck)) {
            System.out.println("\nCorrect deck");
        } else {
            System.out.println("\nIncorrect deck");
        }
    }

    // Check if the deck is correct
    public static boolean isCorrectDeck(Deck deck) {
        List<Card> cards = deck.getCards();

        // Check if the deck has 52 cards
        if (cards.size() != 52) {
            return false;
        }

        // Check if each rank has 4 cards (1 per suit)
        for (Card.Rank rank : Card.Rank.values()) {
            int count = 0;
            for (Card card : cards) {
                if (card.getRank() == rank) {
                    count++;
                }
            }
            if (count != 4) {
                return false;
            }
        }

        return true;
    }
}