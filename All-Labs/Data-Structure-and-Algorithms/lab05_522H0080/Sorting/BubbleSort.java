package Sorting;

import java.util.*;

class BubbleSort {
    public static void bubbleSort(int[] a) {
        int n = a.length;

        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (a[j + 1] < a[j]) {
                    int tmp = a[j];
                    a[j] = a[j + 1];
                    a[j + 1] = tmp;
                }
            }
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

        bubbleSort(a);
    }
}
