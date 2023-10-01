import java.util.Scanner;

public class TranGiaHao_B4
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nhap vao 1 chuoi: ");
        String str = sc.nextLine();

        System.out.println("- Do dai cua chuoi da nhap la: " + findStringLength(str));
        System.out.println("- So tu trong chuoi da nhap la: " + countWords(str));

        System.out.print("- Nhap vao 1 chuoi muon ghep: ");
        String content = sc.nextLine();

        System.out.println("Chuoi da ghep la: " + concatenateString(str, content));

        if(isPalindrome(str))
            System.out.print("- Chuoi vua nhap la chuoi palindrome");
        else    
        System.out.print("- Chuoi vua nhap khong phai la chuoi palindrome");
    }

    public static int findStringLength(String str)
    {
        return str.length();
    } 

    public static int countWords(String str)
    {
        String[] words = str.split(" ");
        return words.length;
    }

    public static String concatenateString(String str, String content)
    {
        return str.concat(content);
    }

    public static boolean isPalindrome(String str)
    {
        String strCheck = str.toLowerCase().replaceAll(" ", "");
        String reverse = "";

        //dao nguoc chuoi
        for(int i = strCheck.length() - 1; i >= 0; i--)
        {
            reverse += strCheck.charAt(i);
        }

        if(strCheck.equals(reverse))
            return true;
        return false;
    }
}