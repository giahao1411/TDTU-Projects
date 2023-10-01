class Ex04 {
    public static int a(int n) {
        return n == 1 ? 3 : (2 * n + 1) + a(n - 1);
    }

    private static int factorial(int n) {
        return (n == 1 || n == 0) ? 1 : n * factorial(n - 1);
    }

    public static int b(int n) {
        return n == 1 ? 1 : factorial(n) + b(n - 1);
    }

    public static int c(int n) {
        return n == 1 ? 1 : factorial(n) * c(n - 1);
    }

    public static int d(int n, int r) {
        if (n <= 0 || r <= 0 || n < r)
            return 1;
        return n * d(n - 1, r - 1);
    }

    public static int e(int n) {
        return n == 1 ? 3 : (int) Math.pow(2, n) + n * n + e(n - 1);
    }

    public static void main(String[] args) {
        System.out.println(a(2));
        System.out.println(b(3));
        System.out.println(c(3));
        System.out.println(d(5, 2));
        System.out.println(e(2));
    }
}
