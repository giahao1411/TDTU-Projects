import java.util.Scanner;

public class TranGiaHao_Bai11
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nhap vao 1 so nguyen: ");
        int n = sc.nextInt();

        System.out.print("Co " + CountDigit(n) + " phan tu trong " + n);
    }

    public static int CountDigit(int n)
    {
        int count = 0;
        while(n > 0)
        {
            n /= 10;
            count++;
        }
        return count;
    }
}