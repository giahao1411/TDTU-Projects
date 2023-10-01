import java.util.Scanner;

public class TranGiaHao_B2
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        //tao ma tran 3x4
        int[][] matrix1 = {{1, 3, 4, 4}, {5, 6, 8, 6}, {7, 6, 3, 4}};
        int[][] matrix2 = {{2, 6, 5, 8}, {5, 6, 7, 1}, {3, 7, 6, 5}};

        //in ra 2 ma tran dang ma tran 3x4
        printMatrix1(matrix1);
        printMatrix2(matrix2);

        //tong 2 ma tran:
        System.out.println("- Tong 2 ma tran:");
        addTwoMatrices(matrix1, matrix2);
        
        //nhan ma tran voi 1 so
        System.out.println("- Nhan ma tran voi 1 so:");
        System.out.println("Chon 1 ma tran:");
        System.out.println("1. Ma tran 1");
        System.out.println("2. Ma tran 2");
        int chon = sc.nextInt();
        System.out.print("Nhap vao 1 so muon nhan:");
        int x = sc.nextInt();
        //ket qua da in
        multiplyMatrix(matrix1, matrix2, x, chon);
    }

    public static void printMatrix1(int[][] matrix1)
    {
        //in ra ma tran
        System.out.println("Ma tran 1:");
        for(int i = 0; i < 3; i++)              //lap tu hang -> cot
        {
            for(int j = 0; j < 4; j++)      
            {
                System.out.print(matrix1[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void printMatrix2(int[][] matrix2)
    {
        //in ra ma tran
        System.out.println("Ma tran 2:");
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void addTwoMatrices(int[][] matrix1, int[][] matrix2)
    {
        //tao ma tran ket qua rows x cols
        int[][] kq = new int[3][4];

        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                kq[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }

        //in ra ma tran kq
        for(int i = 0; i < 3; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                System.out.print(kq[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public static void multiplyMatrix(int[][] matrix1, int[][] matrix2, int x, int chon)
    {
        //tao ma tran moi
        int[][] kq = new int[3][4];

        //nhan ma tran voi 1 so
        if(chon == 1)
        {
            for(int i = 0; i < 3; i++)
            {
                for(int j = 0; j < 4; j++)
                {
                    kq[i][j] = matrix1[i][j] * x;
                }
            }

            //in ma tran da nhan
            System.out.println("Ket qua da nhan la:");
            for(int i = 0; i < 3; i++)
            {
                for(int j = 0; j < 4; j++)
                {
                    System.out.print(kq[i][j] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
        else if(chon == 2)
        {
            for(int i = 0; i < 3; i++)
            {
                for(int j = 0; j < 4; j++)
                {
                    kq[i][j] = matrix2[i][j] * x;
                }
            }

            //in ma tran da nhan
            System.out.println("Ket qua da nhan la:");
            for(int i = 0; i < 3; i++)
            {
                for(int j = 0; j < 4; j++)
                {
                    System.out.print(kq[i][j] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }
        else
        {
            System.out.println("Khong co lua chon nay!");
        }
    }
}