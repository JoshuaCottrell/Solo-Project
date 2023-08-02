import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.List;

import static org.junit.Assert.*;

public class HandTest {
    private Hand hand;

    @Before
    public void setUp() {
        hand = new Hand();
    }

    @Test
    public void testAddCard() {
        Card card = new Card(Suit.HEARTS, Rank.ACE);
        hand.addCard(card);
        List<Card> cards = hand.getCards();
        assertEquals(1, cards.size());
        assertTrue(cards.contains(card));
    }

    @Test
    public void testRemoveCard() {
        Card card = new Card(Suit.DIAMONDS, Rank.KING);
        hand.addCard(card);
        hand.removeCard(card);
        List<Card> cards = hand.getCards();
        assertEquals(0, cards.size());
        assertFalse(cards.contains(card));
    }

    @Test
    public void testGetCards() {
        Card card1 = new Card(Suit.SPADES, Rank.QUEEN);
        Card card2 = new Card(Suit.CLUBS, Rank.JACK);
        hand.addCard(card1);
        hand.addCard(card2);
        List<Card> cards = hand.getCards();
        assertEquals(2, cards.size());
        assertTrue(cards.contains(card1));
        assertTrue(cards.contains(card2));
    }

    @Test
    public void testPrintPlayableCardsWithMatchingSuit() {
        Card card1 = new Card(Suit.HEARTS, Rank.ACE);
        Card card2 = new Card(Suit.HEARTS, Rank.KING);
        Card card3 = new Card(Suit.DIAMONDS, Rank.QUEEN);
        hand.addCard(card1);
        hand.addCard(card2);
        hand.addCard(card3);

        // Provide input to simulate player's choice
        InputStream inputStream = new ByteArrayInputStream("1".getBytes());
        System.setIn(inputStream);

        // Call the method and verify the output
        Card playedCard = hand.printPlayableCards(Suit.HEARTS, false);
        assertEquals(card1, playedCard);

        // Provide input to simulate player's choice
        inputStream = new ByteArrayInputStream("1".getBytes());
        System.setIn(inputStream);

        playedCard = hand.printPlayableCards(Suit.DIAMONDS, false);
        assertEquals(card3, playedCard);

        // Restore System.in
        System.setIn(System.in);
    }

    @Test
    public void testPrintPlayableCardsWithoutMatchingSuit() {
        Card card1 = new Card(Suit.SPADES, Rank.ACE);
        Card card2 = new Card(Suit.CLUBS, Rank.KING);
        Card card3 = new Card(Suit.DIAMONDS, Rank.QUEEN);
        hand.addCard(card1);
        hand.addCard(card2);
        hand.addCard(card3);

        // Provide input to simulate player's choice
        InputStream inputStream = new ByteArrayInputStream("1".getBytes());
        System.setIn(inputStream);

        // Call the method and verify the output
        Card playedCard = hand.printPlayableCards(Suit.HEARTS, false);
        assertEquals(card1, playedCard);

        // Restore System.in
        System.setIn(System.in);
    }

    @Test
    public void testPrintHand() {
        Card card1 = new Card(Suit.SPADES, Rank.ACE);
        Card card2 = new Card(Suit.CLUBS, Rank.KING);
        Card card3 = new Card(Suit.DIAMONDS, Rank.QUEEN);
        hand.addCard(card1);
        hand.addCard(card2);
        hand.addCard(card3);

        hand.printHand();
        // Manually verify the output

    }

    @Test
    public void testEmptyHand() {
        Card card1 = new Card(Suit.HEARTS, Rank.ACE);
        Card card2 = new Card(Suit.DIAMONDS, Rank.KING);
        hand.addCard(card1);
        hand.addCard(card2);
        hand.emptyHand();
        List<Card> cards = hand.getCards();
        assertEquals(0, cards.size());
    }
}