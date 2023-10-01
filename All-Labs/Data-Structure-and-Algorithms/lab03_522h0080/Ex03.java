class Ex03 {
    public static boolean checkPrime(int n, int d) {
        return d == 1 ? true : n % d == 0 ? false : checkPrime(n, d - 1);
    }

    public static boolean checkPrime(int n) {
        return checkPrime(n, n - 1);
    }

    public static void main(String[] args) {
        System.out.println(checkPrime(17, 16));
        System.out.println(checkPrime(23));
        System.out.println(checkPrime(21));
    }
}
