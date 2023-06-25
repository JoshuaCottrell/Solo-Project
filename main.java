public class Main {
    public static void main(String[] args) {
        // Create a new grid with 4 players
        Grid grid = new Grid(4);

        // Print the current game state
        grid.printGameState();

        while(!grid.isGameEnded()) {
            grid.incrementRound();
            grid.printGameState();
        }
        
    }
}