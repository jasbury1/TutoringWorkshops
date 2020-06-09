public class Monkey {
    private String name;
    private int age;
    private int temperature;
    public Monkey(String name, int age){
        this.name = name;
        this.age = age;
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
    public void metabolize(){
        System.out.println("Those bananas were good!");
        temperature++;
    }
    public void favoriteFood(){
        System.out.println("Bananas");
    }
    public void babyName(){
        System.out.println("Infant");
    }
}
