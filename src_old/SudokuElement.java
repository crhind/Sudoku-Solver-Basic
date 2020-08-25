import java.util.HashSet;
import java.util.Set;

public class SudokuElement {
    private Integer value;
    private Set<Integer> potentialValues;
    private Set<SudokuElement> peers;

    public SudokuElement(Set<Integer> potentialValues){
        this.value = null;
        this.potentialValues = new HashSet<>(potentialValues);
        this.peers = new HashSet<>();
    }

    public void removePotentialValue(Integer remove){
        potentialValues.remove(value);
    }

    public Set<Integer> getPotentialValues(){
        return potentialValues;
    }

    public void setValue(Integer value){
        this.value = value;
        potentialValues = new HashSet<>();
        for(SudokuElement peer : peers){
            peer.removePotentialValue(value);
        }
    }

    public void setPeers(Set<SudokuElement> peers){
        this.peers = peers;
    }

    public Integer getValue(){
        return value;
    }
}
