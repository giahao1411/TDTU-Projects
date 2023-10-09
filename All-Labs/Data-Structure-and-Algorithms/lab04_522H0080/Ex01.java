import java.util.*;

class Ex01 {
    public static int[] selectionSort(int[] a) {
        int n = a.length;

        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;

            for (int j = i + 1; j < n; j++) {
                if (a[j] < a[minIdx])
                    minIdx = j;
            }

            int tmp = a[minIdx];
            a[minIdx] = a[i];
            a[i] = tmp;
            // System.out.println(Arrays.toString(a));
        }
        return a;
    }

    public static int[] bubbleSort(int[] a) {
        int n = a.length;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (a[j] > a[j + 1]) {
                    int tmp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = tmp;
                }
            }
            // System.out.println(Arrays.toString(a));
        }
        return a;
    }

    public static int[] insertionSort(int[] a) {
        int n = a.length;

        for (int i = 1; i < n; i++) {
            int key = a[i];
            int j = i - 1;
            while (j >= 0 && a[j] > key) {
                a[j + 1] = a[j];
                j--;
            }
            a[j + 1] = key;
        }
        return a;
    }

    public static void main(String[] args) {
        int[] a = { 3, 4, 6, 1, 9 };
        System.out.println(Arrays.toString(a));
        System.out.println();
        System.out.println(Arrays.toString(insertionSort(a)));
    }
}