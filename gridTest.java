import static org.junit.Assert.assertEquals;

import org.junit.Test;


public class gridTest {
    
    @Test
    public void testGrid() {

        // Number of players test
        Grid game = new Grid(4);
        assertEquals(4, game.getNumberOfPlayers());

        // Round Order Test
        for (int i = 0; !game.isHalfway(); i++) {
            assertEquals(Grid.Round.values()[i], game.getRound());
            game.incrementRound();
        }
        for (int i = 8; !game.isGameEnded(); i--) {
            assertEquals(Grid.Round.values()[i], game.getRound());
            game.incrementRound();
        }
    }
}
