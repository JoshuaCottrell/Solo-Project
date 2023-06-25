import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class cardTest {
    

    @Test
    public void cardTest() {
        Card card = new Card(Card.Rank.ACE, Card.Suit.SPADES);
        assertEquals("ACE of SPADES", card.toString());
        card.setRank(Card.Rank.EIGHT);
        card.setSuit(Card.Suit.CLUBS);
        assertEquals(Card.Rank.EIGHT, card.getRank());
        assertEquals(Card.Suit.CLUBS, card.getSuit());
    }
}
