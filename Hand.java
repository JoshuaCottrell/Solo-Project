import java.util.ArrayList;
import java.util.List;

public class Hand {
    private List<Card> cards;

    public Hand() {
        cards = new ArrayList<>();
    }

    public void addCard(Card card) {
        cards.add(card);
    }

    public void removeCard(Card card) {
        cards.remove(card);
    }

    public List<Card> getCards() {
        return cards;
    }

    public void printPlayableCards(Suit suit) {
        System.out.println("Playable Cards:");
        boolean hasMatchingSuit = false;
        for (int i = 0; i < cards.size(); i++) {
            Card card = cards.get(i);
            if (card.getSuit() == suit) {
                System.out.println((i + 1) + ". " + card);
                hasMatchingSuit = true;
            }
        }
        if (!hasMatchingSuit) {
            for (int i = 0; i < cards.size(); i++) {
            System.out.println((i + 1) + ". " + cards.get(i));
            }
        }
    }

    public void printHand() {
        System.out.println("Current Hand:");
        for (int i = 0; i < cards.size(); i++) {
            System.out.println((i + 1) + ". " + cards.get(i));
        }
    }

    public void emptyHand() {
        cards.clear();
    }
}