import java.util.Scanner;

public class TranGiaHao_Bai04
{	
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

		System.out.print("Enter fahrenheit: ");
		double Fahrenheit = sc.nextDouble();
		System.out.print("Enter celsius: ");
		double Celsius = sc.nextDouble();
		
		System.out.println(Fahrenheit + " Fahrenheit = " + FtoC(Fahrenheit) + " Celsius");
		System.out.print(Celsius + " Celsius = " + CtoF(Celsius) + " Fahrenheit");
	}

	public static double FtoC(double Fahrenheit)
	{
		return 5.0/9.0 * (Fahrenheit - 32);
	}

	public static double CtoF(double Celsius)
	{
		return 9.0/5.0 * Celsius + 32;
	}
}