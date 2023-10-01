import java.util.Scanner;

public class TranGiaHao_Bai13
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nhap vao 1 so nguyen: ");
        int n = sc.nextInt();

        boolean kq = CheckPalindrome(n);
        if(kq)
            System.out.print("Dung");
        else    
            System.out.print("Sai");
    }

    public static boolean CheckPalindrome(int n)
    {
        int reverse = 0;
        int temp = n;
        while(temp != 0)
        {
            reverse = reverse*10 + temp % 10;
            temp /= 10;
        }
        
        if(reverse == n)
            return true;
        else    
            return false;
    }
}