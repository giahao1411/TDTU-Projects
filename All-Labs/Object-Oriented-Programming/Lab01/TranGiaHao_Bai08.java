import java.util.Scanner;

public class TranGiaHao_Bai08
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Nhap vao 1 so: ");
		int n = sc.nextInt();
			
		System.out.println("S1 = " + TongS1(n));
		System.out.println("P = " + TichP(n));	
		System.out.println("S2 = " + TongS2(n));
		System.out.println("S3 = " + TongS3(n));	
		System.out.println("S4 = " + TongS4(n));
	}

	public static int TongS1(int n)
	{
		int s = 0;
		for(int i = 1; i <= n; i++)
			s += i;
		return s;
	}
	
	public static int TichP(int n)
	{
		int s = 1;
		for(int i = 1; i <= n; i++)
			s *= i;
		return s;
	}

	public static int TongS2(int n)
	{
		int s = 0;
		for(int i = 0; i <= n; i++)
			s += Math.pow(2, i);
		return s;
	}

	public static double TongS3(int n)
	{
		double s = 0;
		for(int i = 1; i <= n; i++)
			s += 1.0/(2.0*i);
		return s;
	}

	public static int TongS4(int n)
	{
		int s = 0;
		for(int i = 1; i <= n; i++)
			s += i*i;
		return s;
	}
}
