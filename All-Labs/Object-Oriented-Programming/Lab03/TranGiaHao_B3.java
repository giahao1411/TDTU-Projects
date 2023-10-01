import java.util.*;
import java.lang.*;

public class TranGiaHao_B3
{
	public static void main(String[] args)
	{
		Scanner sc = new Scanner(System.in);

		System.out.print("Moi nhap ho ten:");
		String name = sc.nextLine();
		
		System.out.println("Cau 1: " + returnFirstLast(name));
		System.out.println("Cau 2: " + returnMiddleName(name));
		System.out.println("Cau 3: " + capitalizeName());
	}

	public static String returnFirstLast(String name)
	{
		String[] words = name.split(" ");
		String kq = words[0] + " " + words[words.length - 1];
		return kq;
	}

	public static String returnMiddleName(String name)	
	{
		String[] words = name.split(" ");
		if(words.length % 2 == 0)
			return words[words.length/2 - 1] + " " + words[words.length/2];
		else
			return words[words.length/2];
	}
}
