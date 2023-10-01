import java.util.Scanner;

public class Calculator
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number a: ");
        int a = sc.nextInt();

        System.out.print("Enter number b: ");
        int b = sc.nextInt();

        Calculator cal = new Calculator();

        //try-catch divide
        try 
        {
            double res = cal.divide(a, b);
            System.out.println("Divide: " + res);
        }
        catch (ArithmeticException e)
        {
            System.err.println(e.getMessage());
        }
        catch (NumberOutOfRangeException e)
        {
            System.err.println(e.getMessage());
        }

        //try-catch multiply
        try
        {
            int res = cal.multiply(a, b);
            System.out.println("Multiply: " + res);
        }
        catch (NumberOutOfRangeException e) 
        {
            System.err.println(e.getMessage());
        }

        sc.close();
    }

    public double divide(int a, int b) throws ArithmeticException, NumberOutOfRangeException
    {
        if(b == 0)
        {
            ArithmeticException obj = new ArithmeticException("divide by zero");
            throw obj;
        }
        if((a < -1000 || a > 1000) || (b < -1000 || b > 1000))
        {
            NumberOutOfRangeException obj = new NumberOutOfRangeException("Number is outside the computation");
            throw obj;
        }
        return (double)a/(double)b;
    }

    public int multiply(int a, int b) throws NumberOutOfRangeException
    {
        if((a < -1000 || a > 1000) || (b < -1000 || b > 1000))
        {
            NumberOutOfRangeException obj = new NumberOutOfRangeException("Number is outside the computation");
            throw obj;
        }
        return a * b;
    }

    class NumberOutOfRangeException extends Exception
    {
        public NumberOutOfRangeException(String s)
        {
            super(s);
        }
    }
}