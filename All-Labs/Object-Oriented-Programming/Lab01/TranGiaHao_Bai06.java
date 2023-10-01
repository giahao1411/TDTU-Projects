import java.util.Scanner;

public class TranGiaHao_Bai06
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Enter num1: ");
		int n1 = sc.nextInt();
		System.out.print("Enter num2: ");
		int n2 = sc.nextInt();
		System.out.print("Enter num3: ");
		int n3 = sc.nextInt();

		System.out.print("Min of 3 numbers is: " + findmin(n1, n2, n3));
	}
	
	public static int findmin(int n1, int n2, int n3)
	{
		int min;
		if(n1 < n2)
		{
			if(n1 < n3)
				min = n1;
			else
				min = n3;
		}
		else
		{
			if(n2 < n3)
				min = n2;
			else
				min = n3;
		}
		return min;
	}
}
