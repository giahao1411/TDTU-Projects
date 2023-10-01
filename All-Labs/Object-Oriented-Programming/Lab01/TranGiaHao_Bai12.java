import java.util.Scanner;

public class TranGiaHao_Bai12
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nhap vao 1 so nguyen: ");
        int n = sc.nextInt();

        System.out.print("So dao cua " + n + " la " + ReverseNum(n));
    }

    public static int ReverseNum(int n)
    {
        int reverse = 0, r;
        while(n != 0)
        {
            r = n % 10;
            reverse = reverse*10 + r;
            n /= 10;
        }
        return reverse;
    }
}