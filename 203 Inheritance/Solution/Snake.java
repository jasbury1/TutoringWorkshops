public class Snake extends Animal{
    private float lenght;
    public Snake(String name, int age, float length){
        super(name, age);
        this.lenght = length;
    }
    public float getLenght(){
        return lenght;
    }
    public void sunBath(){
        System.out.println("The sun is nice!");
        temperature++;
    }
    public void favoriteFood(){
        System.out.println("Rodents");
    }
    public void babyName(){
        System.out.println("Hatchling");
    }
}
