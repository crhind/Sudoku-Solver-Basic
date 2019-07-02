public class Application {
    public static void main(String[] args){
        //Start a game element, instantiate the game (How to validate?)
        SudokuBoard board = new SudokuBoard();
        String b = "103020600900305001001806400008102900700000008006708200002609500800203009005010301";
        System.out.println(b.length());
        try{
            board.parseBoard(b);
        }catch(MalformedBoardException e){
            System.out.println(e.getMessage());
        }
    }
}
