public class Snake {
    private String name;
    private int age;
    private float lenght;
    private int temperature;
    public Snake(String name, int age, float length){
        this.name = name;
        this.age = age;
        this.lenght = length;
        this.temperature = 100;
    }
    public String getName() {
        return name;
    }
    public int getAge(){
        return age;
    }
    public int getTemperature(){
        return temperature;
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
