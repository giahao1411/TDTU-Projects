class Ex07 {
    // exercise a:
    public static int findMin(int[] a, int n) {
        // if (n == 0)
        // return a[0];
        // if (a[n - 1] < findMin(a, n - 1))
        // return a[n - 1];
        // return findMin(a, n - 1);
        return n == 0 ? a[0] : a[n - 1] < findMin(a, n - 1) ? a[n - 1] : findMin(a, n - 1);
    }

    public static int sumEle(int[] a, int n) {
        // if (n == 0)
        // return 0;
        // return a[n - 1] + sumEle(a, n - 1);
        return n == 0 ? 0 : a[n - 1] + sumEle(a, n - 1);
    }

    public static int countEven(int[] a, int n) {
        // if (n == 0)
        // return 0;
        // if (a[n - 1] % 2 == 0)
        // return 1 + countEven(a, n - 1);
        // return countEven(a, n - 1);
        return n == 0 ? 0 : a[n - 1] % 2 == 0 ? 1 + countEven(a, n - 1) : countEven(a, n - 1);
    }

    public static void main(String[] args) {
        int[] a = { 2, 5, 9, 7, 6, 3 };
        System.out.println(findMin(a, a.length));
        System.out.println(sumEle(a, a.length));
        System.out.println(countEven(a, a.length));
    }
}
