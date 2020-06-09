public class Parrot extends Animal implements WarmBlooded{
    private String[] colors;
    public Parrot(String name, int age, String[] colors){
        super(name, age);
        this.colors = colors;

    }
    public int getNumColors(){
        return colors.length;
    }
    public void Talk(){
        System.out.println("My name is " + name + "!");
    }
    public void metabolize(){
        System.out.println("Those seeds were good!");
        temperature++;
    }
    public void favoriteFood(){
        System.out.println("Seeds");
    }
    public void babyName(){
        System.out.println("Chick");
    }
}
