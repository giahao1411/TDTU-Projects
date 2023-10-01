import java.util.Scanner; 

public class TranGiaHao_Bai07
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);
		
		System.out.print("Nhap vao 1 ki tu: ");
		String ch = sc.nextLine();
		char c = ch.charAt(0);
		
		boolean kq = check(c);

		if(kq)
			System.out.print("Dung");
		else
			System.out.print("Sai");
	}
	
	public static boolean check(char c)
	{
		if((c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9') || (c >= 'a' && c <= 'z'))
			return true;
		else
			return false;
	}
}