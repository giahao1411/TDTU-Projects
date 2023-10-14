package Recursion;

class Ex01 {
    public double prod_recur(int a, int b) {
        return (a == 0 || b == 0) ? 0 : a + prod_recur(a, b - 1);
    }

    private int bin2dec(int n, int exp) {
        return (n == 0) ? 0 : (n % 10) * (int) Math.pow(2, exp) + bin2dec(n / 10, exp + 1);
    }

    public int bin2dec(int n) {
        return bin2dec(n, 0);
    }

    public int maxDigit(int n) {
        return (n < 10) ? n : (n % 10 > maxDigit(n / 10)) ? n % 10 : maxDigit(n / 10);
    }

    private int maxElement(int a[], int n) {
        return (n == 0) ? a[0] : a[n - 1] > maxElement(a, n - 1) ? a[n - 1] : maxElement(a, n - 1);
    }

    public int maxElement(int[] a) {
        return maxElement(a, a.length);
    }

    private int search(int a[], int n, int key) {
        return (n == 0) ? -1 : (a[n - 1] == key) ? n - 1 : search(a, n - 1, key);
    }

    public int search(int[] a, int key) {
        return search(a, a.length, key);
    }

    public static void main(String[] args) {
        Ex01 test = new Ex01();
        System.out.println(test.prod_recur(2, 5));

        System.out.println(test.bin2dec(1000));

        System.out.println(test.maxDigit(15429));

        int[] a = { 1, 4, 6, 8, 23 };
        System.out.println(test.maxElement(a));

        System.err.println(test.search(a, 8));
    }
}