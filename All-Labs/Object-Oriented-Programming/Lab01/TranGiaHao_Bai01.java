import java.util.Scanner;

public class TranGiaHao_Bai01
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("enter your name: ");
        String s1 = sc.nextLine();

        System.out.printf("\nenter your birthday: ");
        String s2 = sc.nextLine();

        System.out.printf("\nenter your student ID: ");
        String s3 = sc.nextLine();

        System.out.println("Name: " + s1);
	System.out.println("Birthday: " + s2);
	System.out.println("Student ID: " + s3);
    }
}