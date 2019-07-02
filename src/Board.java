import java.util.*;

public abstract class Board {
    private Map<String,SudokuElement> board;

    public Board(){
        this.board = new HashMap<>();
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                board.put(Integer.toString(i)+Integer.toString(j), new SudokuElement(new HashSet<>(Arrays.asList(1,2,3,4,5,6,7,8,9))));
            }
        }

        for(Map.Entry<String, SudokuElement> entry : board.entrySet()){
            char[] index = entry.getKey().toCharArray();
            for(int i = 0; i<9; i++){
                entry.getValue()
                        .addNeighbout(getElement(Character.getNumericValue(index[0]), i));
                entry.getValue()
                        .addNeighbout(getElement(i, Character.getNumericValue(index[1])));
            }
        }
    }
    //TODO: Sort out the predefined set of gris and rows. has to be in board class. 

    public void setElementValue(int row, int column, int value){
        String element = Integer.toString(row)+Integer.toString(column);
        board.get(element).setValue(value);
    }

    public SudokuElement getElement(int row, int column){
        String element = Integer.toString(row)+Integer.toString(column);
        return board.get(element);
    }

    public Map<String, SudokuElement> getBoard(){
        return board;
    }

    public abstract boolean win();
}
