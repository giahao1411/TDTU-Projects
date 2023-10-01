import java.util.ArrayList;

public class TestPoint <T>
{
    private ArrayList<T> p = new ArrayList<T>();

    public void add(T obj)
    {
        p.add(obj);
    }

    public void display()
    {
        for(T obj : p)
        {
            System.out.println(obj);
        }
    }

    public void isInside()
    {
        for(T obj : p)
        {
            if(((Point) obj).getDistance() <= 1.0)
            {
                System.out.println(obj + ": is inside circle(0,0), radius = 1");
            }
            else
            {
                System.out.println(obj + ": is not inside circle(0,0), radius = 1");
            }
        }
    }

    public static void main(String[] args)
    {
        TestPoint<Point> point = new TestPoint<Point>();
        
        point.add(new Point(1.2, 5.3));
        point.add(new Point(2.0, 3.0));
        point.add(new Point(0.0, 0.1));
        point.display();
        
        System.out.println();

        point.isInside();
    }
}