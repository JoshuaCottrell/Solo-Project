import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Hand {
    private List<Card> cards;

    public Hand() {
        cards = new ArrayList<>();
    }

    public void addCard(Card card) {
        cards.add(card);
    }

    public Card removeCard(Card card) {
        cards.remove(card);
        return card;
    }

    public List<Card> getCards() {
        return cards;
    }

    public Card printPlayableCards(Suit suit) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Playable Cards:");
        List<Card> playableCards = new ArrayList<>();
        for (Card card : cards) {
            if (card.getSuit() == suit) {
                playableCards.add(card);
            }
        }
        if (playableCards.isEmpty()) {
            playableCards.addAll(cards);
        }
        for (int i = 0; i < playableCards.size(); i++) {
            System.out.println((i + 1) + ". " + playableCards.get(i));
        }
        System.out.println("Enter the number of the card you want to play: ");
        int choice = scanner.nextInt();
        while (!(choice >= 1 && choice <= playableCards.size())) {
            System.out.println("Invalid choice! Please try again");
            choice = scanner.nextInt();
        }
        Card selectedCard = playableCards.get(choice - 1);
        System.out.println("You played: " + selectedCard);
        cards.remove(selectedCard);
        return selectedCard;
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