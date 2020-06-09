public class Monkey extends Animal implements WarmBlooded{
    public Monkey(String name, int age){
        super(name, age);
    }

    public void metabolize(){
        System.out.println("Those bananas was good!");
        temperature++;
    }
    public void favoriteFood(){
        System.out.println("Bananas");
    }
    public void babyName(){
        System.out.println("Infant");
    }
}
