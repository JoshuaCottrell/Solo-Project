import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class DeckTest {
    private Deck deck;

    @Before
    public void setUp() {
        deck = new Deck();
    }

    @Test
    public void testInitializeDeck() {
        assertEquals(52, deck.getRemainingCards());
    }

    @Test
    public void testShuffle() {
        Card firstCardBeforeShuffle = deck.drawCard();
        deck.shuffle();
        Card firstCardAfterShuffle = deck.drawCard();

        assertNotEquals(firstCardBeforeShuffle, firstCardAfterShuffle);
    }

    @Test
    public void testDrawCard() {
        int initialRemainingCards = deck.getRemainingCards();
        Card card = deck.drawCard();

        assertNotNull(card);
        assertEquals(initialRemainingCards - 1, deck.getRemainingCards());
    }

    @Test(expected = IllegalStateException.class)
    public void testDrawCardFromEmptyDeck() {
        while (deck.getRemainingCards() > 0) {
            deck.drawCard();
        }
        deck.drawCard(); // This should throw an exception
    }

    @Test
    public void testGetRemainingCards() {
        assertEquals(52, deck.getRemainingCards());
        deck.drawCard();
        assertEquals(51, deck.getRemainingCards());
    }
}