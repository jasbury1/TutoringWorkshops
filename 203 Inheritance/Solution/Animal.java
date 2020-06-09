public abstract class Animal {
    protected String name;
    private int age;
    protected int temperature;
    public Animal(String name, int age){
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
    public abstract void favoriteFood();
    public abstract void babyName();
}
