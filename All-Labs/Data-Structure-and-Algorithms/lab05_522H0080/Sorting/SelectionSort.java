package Sorting;

import java.util.*;

class SelectionSort {
    public static void selectionSort(int[] a) {
        int n = a.length;

        for (int i = 0; i < n - 1; i++) {
            int idx = i;

            for (int j = i + 1; j < n; j++) {
                if (a[j] < a[idx])
                    idx = j;
            }

            int tmp = a[idx];
            a[idx] = a[i];
            a[i] = tmp;

            System.out.println(Arrays.toString(a));
        }
    }

    public static void main(String[] args) {
        int n = 5;
        int[] a = new int[n];

        Random rand = new Random();
        for (int i = 0; i < n; i++) {
            a[i] = rand.nextInt() % 100 + 100;
        }

        System.out.println(Arrays.toString(a));
        System.out.println();

        selectionSort(a);
    }
}
