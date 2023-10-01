import java.util.Scanner;
import java.math.BigDecimal;
import java.util.Arrays;

public class TranGiaHao_522H0080_b2
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int[] arr = {1, 9, 65, -4, 45, -99, 2, 10, 50, 7, 11, 13};
        BigDecimal[] arr1 = {new BigDecimal("4.1"), new BigDecimal("78.7"), new BigDecimal("3.99")};

        menu();

        System.out.println(Arrays.toString(arr));

        System.out.print("Nhap vao lua chon: ");
        int userChoice = sc.nextInt();

        switch(userChoice)
        {
            case 0:
                return;
            case 1:
                System.out.println("So lon nhat trong mang la: " + findMax(arr));
                break;
            case 2:
                System.out.println("So be nhat trong mang la: " + findMin(arr));
                break;
            case 3:
                System.out.println("Tong cac phan tu chan la: " + sumOfEven(arr));
                break;
            case 4:
                System.out.print("Moi nhap vao phan tu cu the: ");
                int x = sc.nextInt();

                System.out.println("Phan tu " + x + " xuat hien trong mang " + countElement(arr, x) + " lan"); 
                break;
            case 5:
                System.out.println("Co " + countPrime(arr) + " so nguyen to trong mang");
                break;
            case 6:
                System.out.print("Moi nhap phan tu can tim: ");
                int k = sc.nextInt();
        
                System.out.println("Phan tu can tim nam o vi tri thu " + find(arr, k));
                break;
            case 7:
                square(arr);
                break;
            case 8:
                System.out.println("So lon nhat trong mang arr1 la: " + findMax(arr1));
                break;
            case 9:
                System.out.print("Moi nhap phan tu: ");
                int c = sc.nextInt();
                System.out.println("Cac so chia het cho " + c + " la: " + Arrays.toString(divisibleNumbers(arr, c)));
                break;
            case 10:
                System.out.print("So lon thu ba trong mang la: " + finfThirdLargest(arr));
                break;
        }
    }

    public static void menu()
    {
        System.out.println("0. Exit");
        System.out.println("1. Tim so lon nhat trong mang");
        System.out.println("2. Tim so be nhat trong mang");
        System.out.println("3. Tong cac phan tu chan trong mang");
        System.out.println("4. Dem phan tu x xuat hien bao nhieu lan");
        System.out.println("5. Dem so nguyen to co trong mang");
        System.out.println("6. Tim vi tri cua phan tu nhap vao");
        System.out.println("7. Binh phuong tat ca cac phan tu trong mang");
        System.out.println("8. Tim so lon nhat trong mang dung BigDecimal");
        System.out.println("9. Liet ke cac so chia het cho so nhap vao");
        System.out.println("10. Tim so lon thu ba trong mang");
    }

    public static int findMax(int[] arr)
    {
        int max = Arrays.stream(arr).max().getAsInt();
        return max;
    }

    public static int findMin(int[] arr)
    {
        int min = Arrays.stream(arr).min().getAsInt();
        return min;
    }

    public static int sumOfEven(int[] arr)
    {
        int sum = 0;
        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] % 2 == 0)
            {
                sum += arr[i];
            }
        }
        return sum;
    }

    public static int countElement(int[] arr, int x)
    {
        int count = 0;
        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] == x)
            {
                count++;
            }
        }
        return count;
    }

    public static boolean checkPrime(int n)
    {
        if(n < 2)
            return false;
        for(int i = 2; i <= (int)Math.sqrt(n); i++)
        {
            if(n % i == 0)
                return false;
        }
        return true;
    }

    public static int countPrime(int[] arr)
    {
        int count = 0;
        for(int i = 0; i < arr.length; i++)
        {
            if(checkPrime(arr[i]))
                count++;
        }
        return count;
    }

    public static int find(int[] arr, int k)
    {
        int pos = -1;
        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] == k)
            {
                pos = i + 1;
                break;
            }
        }
        return pos;
    }

    public static void square(int[] arr)
    {
        int[] newArr = new int[arr.length];

        for(int i = 0; i < newArr.length; i++)
        {
            newArr[i] = arr[i]*arr[i];
        }

        for(int i = 0; i < newArr.length; i++)
        {
            System.out.print(newArr[i] + " ");
        }
    }

    public static BigDecimal findMax(BigDecimal[] arr1)
    {
        BigDecimal max = arr1[0];
        for(int i = 1; i < arr1.length; i++)
        {
            if(arr1[i].compareTo(max) > 0)
            {
                max = arr1[i];
            }
        }
        return max;
    }

    public static int[] divisibleNumbers(int[] arr, int c)
    {
        int count = 0;

        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] % c == 0)
                count++;
        }

        int[] divisibleByK = new int[count];
        int j = 0;

        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] % c == 0)
            {
                divisibleByK[j] = arr[i];
                j++;
            }
        }

        return divisibleByK;
    }

    public static int finfThirdLargest(int[] arr)
    {
        int max = arr[0];
        int second = Integer.MIN_VALUE;         //gan ptu lon thu 2 va 3 la gia tri be nhat cua integer
        int third = Integer.MIN_VALUE;
        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] > max)
            {
                third = second;         //loai phan tu thu 3, gan phan tu lon thu 2 = phan tu lon thu 3
                second = max;           //day phan tu lon thu 1 = phan tu lon thu 2
                max = arr[i];
            }
            else if(arr[i] > second && arr[i] != max)
            {  
                third = second;         //dua phan tu lon thu 2 lam phan tu lon thu 3
                second = arr[i];        //dua phan tu do vao lam phan tu thu lon thu 2
            }
            else if(arr[i] > third && arr[i] != second && arr[i] != max)
            {
                third = arr[i];         //dua phan tu do vao lam phan tu lon thu 3
            }
        }

        return third;
    }
}