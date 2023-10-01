class Ex05 {
    public static int convertBinary(int n) {
        if (n <= 0)
            return 0;
        return n % 2 + 10 * convertBinary(n / 2);
    }

    public static void main(String[] args) {
        System.out.println(convertBinary(8));
    }
}
