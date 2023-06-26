public class Main {
    public static void main(String[] args) {
        // Create a new grid with 4 players
        Grid game = new Grid(4);

        game.startGame();
        game.printGameState();
        
    }
}