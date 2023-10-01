class Ex02 {
    public static int a(int n) {
        return (n == 1 || n == 0) ? 1 : n * a(n - 1);
    }

    public static int b(int x, int n) {
        return n == 0 ? 1 : x * b(x, n - 1);
    }

    public static int c(int n) {
        // if (n < 10)
        // return 1;
        // return 1 + c(n / 10);
        return n < 10 ? 1 : 1 + c(n / 10);
    }

    public static int d(int a, int b) {
        // if (b == 0)
        // return a;
        // return d(b, a % b);
        return b == 0 ? a : d(b, a % b);
    }

    public static void main(String[] args) {
        System.out.println(c(1245));
        System.out.println(d(2, 4));
    }
}
