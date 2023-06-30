import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class PlayerTest {
    private Player player;

    @Before
    public void setUp() {
        player = new Player();
    }

    @Test
    public void testGetHand() {
        assertNotNull(player.getHand());
    }

    @Test
    public void testAddCardToHandAndRemoveCardFromHand() {
        System.out.println("Add card to player hand and print:");
        player.getHand().addCard(new Card(Suit.CLUBS, Rank.ACE));
        player.getHand().printHand();
        System.out.println("Remove card from players hand and print:");
        player.getHand().removeCard(player.getHand().getCards().get(0)); // Edit this later
        player.getHand().printHand();
        // Manually verify the output
    }


    @Test
    public void testIsDealer() {
        assertFalse(player.isDealer());
    }

    @Test
    public void testSetDealer() {
        player.setDealer(true);
        assertTrue(player.isDealer());
    }

    @Test
    public void testGetTricksWon() {
        assertEquals(0, player.getTricksWon());
    }

    @Test
    public void testSetTricksWon() {
        player.setTricksWon(5);
        assertEquals(5, player.getTricksWon());
    }

    @Test
    public void testAddTrick() {
        player.addTrick(3);
        assertEquals(3, player.getTricksWon());
    }

    @Test
    public void testGetBet() {
        assertEquals(0, player.getBet());
    }

    @Test
    public void testSetBet() {
        player.setBet(10);
        assertEquals(10, player.getBet());
    }

    @Test
    public void testGetScore() {
        assertEquals(0, player.getScore());
    }

    @Test
    public void testAddToScore() {
        player.addToScore(20);
        assertEquals(20, player.getScore());
    }
}