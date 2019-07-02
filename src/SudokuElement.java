import java.util.HashSet;
import java.util.Set;

public class SudokuElement {
    private Integer value;
    private Set<Integer> potentialValues;
    private Set<SudokuElement> neighbours;

    public SudokuElement(Set<Integer> potentialValues){
        this.value = null;
        this.potentialValues = new HashSet<>(potentialValues);
        this.neighbours = new HashSet<>();
    }

    public void removePotentialValues(Integer remove){
        potentialValues.remove(value);
    }

    public Set<Integer> getPotentialValues(){
        return potentialValues;
    }

    public void setValue(Integer value){
        this.value = value;
        for(SudokuElement neighbour : neighbours){
            neighbour.removePotentialValues(value);
        }
    }

    public void addNeighbout(SudokuElement neighbour){
        neighbours.add(neighbour);
    }
}
