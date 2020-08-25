import java.util.Map;

public class SudokuSolver {
    private SudokuBoard game;

    public SudokuSolver(SudokuBoard game){
        this.game = game;
    }

    public void setGame(SudokuBoard game){
        this.game = game;
    }

    public SudokuBoard getGame(){
        return game;
    }

    //Straight up and down. fuck recursion.
    public boolean solve(){
        // General current idea is to find the least constrained element and search if any of the neighbours have values that
        // are in our potential values that we can remove to allow a single value -> that elements value.

        // Search through game states to find solutions....
        for(Map.Entry<String, SudokuElement> element : game.getBoard().entrySet()) {
            SudokuElement hold = element.getValue();
            if(hold.getPotentialValues().size() == 1){
                hold.setValue((Integer)hold.getPotentialValues().toArray()[0]);
            }

            if(hold.getPotentialValues().size() == 0){
                return false;
            }
        }
        if(game.win()){
            return true;
        }

        return solve();
    }
}
