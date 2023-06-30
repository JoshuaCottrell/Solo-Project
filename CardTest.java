import org.junit.Test;
import static org.junit.Assert.*;

public class CardTest {

    @Test
    public void testGetSuit() {
        Card card = new Card(Suit.HEARTS, Rank.ACE);
        assertEquals(Suit.HEARTS, card.getSuit());
    }

    @Test
    public void testGetRank() {
        Card card = new Card(Suit.DIAMONDS, Rank.KING);
        assertEquals(Rank.KING, card.getRank());
    }

    @Test
    public void testToString() {
        Card card = new Card(Suit.SPADES, Rank.QUEEN);
        assertEquals("QUEEN of SPADES", card.toString());
    }
}