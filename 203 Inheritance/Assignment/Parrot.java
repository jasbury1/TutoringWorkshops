public class Parrot {
    private String name;
    private int age;
    private String[] colors;
    private int temperature;
    public Parrot(String name, int age, String[] colors){
        this.name = name;
        this.age = age;
        this.colors = colors;
        this.temperature = 100;
    }

    public String getName() {
        return name;
    }
    public int getAge(){
        return age;
    }
    public int getNumColors(){
        return colors.length;
    }
    public void Talk(){
        System.out.println("My name is " + name + "!");
    }
    public int getTemperature(){
        return temperature;
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
