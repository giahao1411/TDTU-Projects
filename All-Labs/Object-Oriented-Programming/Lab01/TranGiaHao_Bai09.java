import java.util.Scanner;

public class TranGiaHao_Bai09
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

		System.out.print("Nhap vao 1 so: ");
		int n = sc.nextInt();

		Hailstone(n);
	}
		
	public static void Hailstone(int n)
	{
		while(n > 1)
		{
			System.out.print(n + " ");
			if(n % 2 == 0)
				n /= 2;
			else
				n = n*3 + 1;
		}
			System.out.print(n + " ");
	}
}