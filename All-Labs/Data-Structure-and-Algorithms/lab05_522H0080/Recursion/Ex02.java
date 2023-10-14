package Recursion;

public class Ex02 {
    public static int recursionA(int n) {
        return (n == 1) ? 2 : (int) Math.pow(2, n) + recursionA(n - 1);
    }

    public static int iterationA(int n) {
        int res = 0;
        for (int i = 1; i <= n; i++) {
            res += (int) Math.pow(2, i);
        }
        return res;
    }

    public static double recursionB(int x) {
        return (x == 0) ? 1.0 / 2.0 : (x + 1.0) / 2.0 + recursionB(x - 1);
    }

    public static double iterationB(int x) {
        double res = 0;
        for (int i = 0; i <= x; i++) {
            res += (i + 1.0) / 2.0;
        }
        return res;
    }

    private static int factorial(int n) {
        return (n == 0 || n == 1) ? 1 : n * factorial(n - 1);
    }

    public static double recursionC(int i) {
        return (i == 1) ? 1 : (double) (factorial(i) / factorial(i - 1)) + recursionC(i - 1);
    }

    public static double iterationC(int n) {
        double res = 0;
        for (int i = 1; i <= n; i++) {
            res += factorial(i) / factorial(i - 1);
        }
        return res;
    }

    public static int recursionD(int x) {
        return (x == 1) ? 0 : ((int) Math.pow(x, 2) - x) + recursionD(x - 1);
    }

    public static int iterationD(int x) {
        int res = 0;
        for (int i = 1; i <= x; i++) {
            res += (int) Math.pow(i, 2) - i;
        }
        return res;
    }

    public static int recursionE(int x) {
        return (x == 1) ? 1 : x * recursionE(x - 1);
    }

    public static int iterationE(int x) {
        int res = 1;
        for (int i = 1; i <= x; i++) {
            res *= i;
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(recursionA(3));
        System.out.println(iterationA(3));

        System.out.println(recursionB(2));
        System.out.println(iterationB(2));

        System.out.println(recursionC(3));
        System.out.println(iterationC(3));

        System.out.println(recursionD(4));
        System.out.println(iterationD(4));

        System.out.println(recursionE(3));
        System.out.println(iterationE(3));
    }
}
