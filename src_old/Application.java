import org.omg.CORBA.SystemException;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Application {
    public static void main(String[] args){
        //Start a game element, instantiate the game (How to validate?)
        SudokuBoard board = new SudokuBoard();
        String b = "103020600900305001001806400008102900700000008006708200002609500800203009005010301";
        try {
            BufferedReader reader = new BufferedReader(new FileReader("Sudoku Games.txt"));
            b = reader.readLine();
            b = b.split(" ")[0];
            System.out.println(b.length());

            board.parseBoard(b);
            board.displayBoard();
        }catch(MalformedBoardException e){
            System.out.println(e.getMessage());
        }catch (FileNotFoundException e){
            System.out.println(e.getMessage());
            e.printStackTrace();
        }catch (IOException e){
            System.out.println(e.getMessage());
            e.printStackTrace();
        }
    }
}
