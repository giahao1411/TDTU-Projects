import java.util.Scanner;

public class TranGiaHao_Bai05
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

		System.out.print("Enter a year: ");
		int year = sc.nextInt();

		checkyear(year);	
	}

	public static void checkyear(int year)
	{
		if(year % 400 == 0)
			System.out.print(year + " is a leap year");
		else if(year % 4 == 0 && year % 100 != 0)
			System.out.print(year + " is a leap year");
		else
			System.out.print(year + " is not a leap year");
	}
}
