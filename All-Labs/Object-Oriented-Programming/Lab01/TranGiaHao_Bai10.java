import java.util.Scanner;

public class TranGiaHao_Bai10
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nhap vao 1 so nguyen: ");
        int n = sc.nextInt();

        System.out.print("Tong so dau va so cuoi la: " + SumFirstAndLastDigit(n));
    }

    public static int SumFirstAndLastDigit(int n)
    {
        int r = n % 10;     //find last digit
        while(n >= 10)
            n /= 10;
        return n + r;
    }
}