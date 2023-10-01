import java.util.Scanner;

public class TranGiaHao_B1
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int[] arr = {1, 3, 3, 3, 6, 7, 6, 60, 60, 78};

        printArr(arr);

        //cau 1
        System.out.println("- Cau 1:");
        System.out.print("Nhap vao 1 so muon xoa:");
        int remove = sc.nextInt();

        System.out.println("" + removeFirstEle(arr, remove));

        //cau 2
        System.out.println("- Cau 2:");
        System.out.print("Nhap vao 1 so muon them vao:");
        int ele = sc.nextInt();
        System.out.print("Nhap vao vi tri muon them:");
        int pos = sc.nextInt();

        insertEle(arr, ele, pos);

        //cau 3
        System.out.println("- Cau 3: in ra cac phan tu trung nhau");
        findDuplicate(arr);
        printArr(arr);
    }

    public static void printArr(int[] arr)
    {
        for(int i = 0; i < arr.length; i++)
        {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }

    public static boolean removeFirstEle(int[] arr, int remove)
    {
        int pos = -1;
        //tim vi tri cua phan tu 
        for(int i = 0; i < arr.length; i++)
        {
            if(arr[i] == remove)
            {
                pos = i;
                break;
            }
        }
        //xoa phan tu da tim
        if(pos == -1)
            return false;
        else
        {
            for(int i = pos; i < arr.length - 1; i++)
            {
                arr[i] = arr[i + 1];
            }
            arr[arr.length - 1] = 0;
            return true;
        }
    }

    public static void insertEle(int[] arr, int ele, int pos)
    {
        if(pos <= 0 || pos > arr.length)
            System.out.println("Loi chon vi tri muon them");
        else
        {
            //lui cac phan tu 1 don vi
            for(int i = arr.length - 1; i >= pos; i--)
            {
                arr[i] = arr[i - 1];
            }
            arr[pos - 1] = ele;        //them phan tu vao vi tri chi dinh
            //in ra mang
            for(int i = 0; i < arr.length; i++)
            {
                System.out.print(arr[i] + " ");
            }
            System.out.println();
        }
    }

    public static void findDuplicate(int[] arr)
    {
        for (int i = 0; i < arr.length; i++)
        {
            for (int j = 0; j < i; j++)         //chay den i - 1 - va tro ve vi tri 0 sau moi lan i lap xong
            {
                if (arr[i] == arr[j]) 
                {
                    System.out.print(arr[i] + " ");
                }
            }  
        }
        System.out.println();
    }

    // public static void removeDuplicate(int[] arr)
    // {
    //     // for(int i = 0)
    // }
}