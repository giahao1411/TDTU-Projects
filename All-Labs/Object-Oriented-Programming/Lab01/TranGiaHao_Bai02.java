import java.util.Scanner;

public class TranGiaHao_Bai02
{	
	public static void main(String[] args)
	{	
		Scanner sc = new Scanner(System.in);

		System.out.print("Enter height: ");
		double height = sc.nextDouble();
		System.out.print("Enter base: ");
		double base = sc.nextDouble();

		double area = 1.0/2.0 * base * height;

		System.out.print("Area = " + area);
	}
}

