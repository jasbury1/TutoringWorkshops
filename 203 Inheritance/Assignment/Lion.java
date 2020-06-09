public class Lion {
    private String name;
    private int age;
    private int temperature;
    public Lion(String name, int age){
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
