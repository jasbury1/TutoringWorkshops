/*
Refactor the classes using at least one interface and one abstract class.
All animal classes should be a subclass of the Animal class.  Then write
the filterMonkeys function that is commented out below.
 */

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        ArrayList<Animal> animals = new ArrayList<>();
        animals.add(new Monkey("monkey", 10));
        animals.add(new Lion("lion", 12));
        animals.add(new Snake("snake", 3, 21));
        String[] colors = {"Blue", "Red"};
        animals.add(new Parrot("parrot", 14, colors));
        for(Animal animal : filterMonkeys(animals)){
            System.out.println(animal.getName());
        }
    }


    //returns a list of all of the given animals except for the monkeys
    public static List<Animal> filterMonkeys(List<Animal> animals){
        ArrayList<Animal> non_monkeys = new ArrayList<>();
        for(Animal animal : animals){
            if(!(animal instanceof Monkey)){
                non_monkeys.add(animal);
            }
        }
        return non_monkeys;
    }


}
