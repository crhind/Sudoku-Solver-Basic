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
