public class Lion extends Animal implements WarmBlooded{
    public Lion(String name, int age){
        super(name, age);
    }

    public void metabolize(){
        System.out.println("That buffalo was good!");
        temperature++;
    }
    public void favoriteFood(){
        System.out.println("Buffalo");
    }
    public void babyName(){
        System.out.println("Cub");
    }
}
