import java.util.Scanner;

public class TranGiaHao_Bai03
{	
	public static void main(String[] args)
	{	
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Enter num1: ");
		int num1 = sc.nextInt();
		System.out.print("Enter num2: ");
		int num2 = sc.nextInt();
		
		System.out.print("Remainder of num1 and num2 is: " + remainder_of_division(num1, num2));
	}

	public static int remainder_of_division(int num1, int num2)
	{
		return num1 % num2;
	}
}
