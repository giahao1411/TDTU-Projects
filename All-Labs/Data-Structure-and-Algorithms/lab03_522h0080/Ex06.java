class Ex06 {
    // exercise a:
    public static int findMin(int[] a, int n) {
        int minEle = a[0];
        for (int i = 1; i < n; i++) {
            if (a[i] < minEle)
                minEle = a[i];
        }
        return minEle;
    }

    // ecercise b:
    public static int sumEle(int[] a, int n) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += a[i];
        }
        return sum;
    }

    // exercise c:
    public static int countEven(int[] a, int n) {
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (a[i] % 2 == 0)
                count++;
        }
        return count;
    }

    public static void main(String[] args) {
        int[] a = { 1, 5, 6, 8, 61, 92 };

        System.out.println(findMin(a, a.length));
        System.out.println(sumEle(a, a.length));
        System.out.println(countEven(a, a.length));
    }
}
