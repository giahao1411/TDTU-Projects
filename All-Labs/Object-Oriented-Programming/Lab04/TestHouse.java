public class TestHouse
{
    public static void main(String[] args)
    {
        House h1 = new House();
        House h2 = new House("5522", 5, true, 78.2, 300.0);

        System.out.println("House 1: " + h1);
        System.out.println("House 1: " + h2);
    }
}