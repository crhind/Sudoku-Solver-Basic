import java.util.HashSet;
import java.util.Set;

public class SudokuBoard extends Board{

    public SudokuBoard(){
        super();
    }

    public void parseBoard(String game) throws MalformedBoardException{
        char[] elements = game.toCharArray();
        if(elements.length != 81){
            throw new MalformedBoardException("Not enough characters in the game");
        }
        for(int i=0; i< elements.length; i++){
            this.setElementValue((int)(i/9), (int)(i%9), Character.getNumericValue(elements[i]));
        }
    }

    @Override
    public boolean win(){
        boolean won = true;
        for(int i =0; i<9; i++){
            if(!gridWin(i/3, i%3) ){
                won = false;
            }
//            if(!columnWin(i)){
//                won = false;
//            }
//            if(!rowWin(i)){
//                won = false;
//            }
        }
        return won;
    }

    private boolean gridWin(int gridrow, int gridcolumn){
        System.out.println("Grid i: " + gridrow + " y: " + gridcolumn);
        Set<Integer> elements = new HashSet<>();
        for(int i= 0; i<3; i++){
            for(int j =0; j<3; j++){
                //Can't have a winning game that contains 0's, may change this later to null to save space.
                //.add method in hashsets returns false when one of the elements already exists.
                //TODO Change uninitiated elements in the boar dto null and not 0.
                SudokuElement element = getElement(gridrow*i, gridcolumn*j);
                if(element.getPotentialValues().size() > 1){

                    return false;
                }
            }
        }
        return true;
    }

//    private boolean rowWin(int row){
//        Set<Integer> elements = new HashSet<>();
//
//        for(int i = 0; i<9; i++){
//            //Can't have a winning game that contains 0's, may change this later to null to save space.
//            //.add method in hashsets returns false when one of the elements already exists.
//            //TODO Change uninitiated elements in the boar dto null and not 0.
//            int element = getElement(row, i);
//            if(element == 0 || !elements.add(element)){
//                return false;
//            }
//        }
//        return true;
//    }
//
//    private boolean columnWin(int column){
//        Set<Integer> elements = new HashSet<>();
//
//        for(int i = 0; i<9; i++){
//            //Can't have a winning game that contains 0's, may change this later to null to save space.
//            //.add method in hashsets returns false when one of the elements already exists.
//            //TODO Change uninitiated elements in the boar dto null and not 0.
//            int element = getElement(i, column);
//            if(element == 0 || !elements.add(element)){
//                return false;
//            }
//        }
//        return true;
//    }

    public void displayBoard(){
        for(int i=0;i<9; i++){
            if(i%3 == 0){
                System.out.println("    - - - - - - - - - - - - - - - - -");
            }
            for(int j=0; j<9; j++){
                if(j%3 == 0){
                    System.out.print("  |");
                }
                System.out.print("  " + this.getElement(i,j));
            }
            System.out.println("  |");
        }
        System.out.println("    - - - - - - - - - - - - - - - - -");
    }
}