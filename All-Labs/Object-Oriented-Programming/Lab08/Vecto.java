//using Scanner and Vector in java.util.
import java.util.*;

public class Vecto
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the length of vecto x: ");
        int xLen = sc.nextInt();

        Vector<Integer> x = new Vector<>();

        for(int i = 0; i < xLen; i++)
        {
            System.out.print("Enter ele " + i + ": ");
            int ele = sc.nextInt();
            x.add(ele);
        }
        System.out.println("Vector x: ");

        output(x);

        Vector<Integer> y = new Vector<>();
        for(int i = 0; i < xLen; i++)
        {
            int ele = 2 * x.get(i) * x.get(i) + 1;
            y.add(ele);
        }
        System.out.println("Vector y: ");

        output(y);
        sc.close();
    }

    public static void output(Vector<Integer> x)
    {
        for(Integer ele: x)
        {
            System.out.print(ele + "  ");
        }
        System.out.println();
    }
}