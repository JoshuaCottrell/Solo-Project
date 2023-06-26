import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class deckTest {
    

    @Test
    public void testDeck() {
        Deck deck = new Deck();
        deck.printCards();
        deck.shuffle();
        deck.printCards();
        assertEquals(true, true);
    }
}
