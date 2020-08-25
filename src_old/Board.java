import java.util.*;

public abstract class Board {
    private Map<String,SudokuElement> board;
    private Map<Integer, Set<SudokuBoard>> grids; // Corresponds to the grids in the board, ie value 1 - 9.

    public Board(){
        this.board = new HashMap<>();
        String[] rows = {"A", "B", "C", "D", "E", "F", "G", "H", "I"};
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                board.put(rows[i]+Integer.toString(j), new SudokuElement(new HashSet<>(Arrays.asList(1,2,3,4,5,6,7,8,9))));
            }
        }

        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(rows[i].equals("A") || )
            }
        }
    }
    //TODO: Fix up the indexing for this class. Cannot get grids yet.

    public void initialiseBoard(String boardString) throws MalformedBoardException {
        String[] rows = {"A", "B", "C", "D", "E", "F", "G", "H", "I"};
        char[] elements = boardString.toCharArray();
        if(elements.length != 81){
            throw new MalformedBoardException("Not enough characters in the game");
        }
        for(int i=0; i< elements.length; i++){
            String elementName = rows[(int)(1/9)]+Integer.toString(i%9);
            SudokuElement element = board.get(elementName);
            element.setValue(Character.getNumericValue(elements[i]));
            element.setPeers(getPeers(elementName));
        }
    }

    public void setElementValue(int row, int column, int value){
        String element = Integer.toString(row)+Integer.toString(column);
        board.get(element).setValue(value);
    }

    public SudokuElement getElement(int row, int column){
        String element = Integer.toString(row)+Integer.toString(column);
        return board.get(element);
    }

    public Set<SudokuElement> getPeers(String elementName){
        Set<SudokuElement> peers = new HashSet<>();
        for(Map.Entry<String, SudokuElement> entry : board.entrySet()){
            String row = Character.toString(elementName.charAt(0));
            String col = Character.toString(elementName.charAt(1));

            if(entry.getKey().contains(row) || entry.getKey().contains(col)){
                if(!entry.getKey().equals(elementName)){
                    peers.add(entry.getValue());
                }
            }

            // TODO Do something with the grids. to get
        }
        return peers;
    }

    public Map<String, SudokuElement> getBoard(){
        return board;
    }

    public abstract boolean win();
}
