public class TestRectangle
{
    public static void main(String[] args)
    {
        Rectangle r1 = new Rectangle();
        Rectangle r2 = new Rectangle(3.5f, 6.6f);

        System.out.println("Rectangle 1= " + r1);
        System.out.println("Area r1 = " + r1.getArea() + ", Perimeter r1 = " + r1.getPerimeter());
        System.out.println("Rectangle 2= " + r2);
        System.out.println("Area r2 = " + r2.getArea() + ", Perimeter r2 = " + r2.getPerimeter());
    }
}