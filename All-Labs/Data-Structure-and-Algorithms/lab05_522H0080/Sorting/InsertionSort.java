package Sorting;

import java.util.*;

class InsertionSort {
    public static void insertionSort(int[] a) {
        int n = a.length;

        for (int i = 1; i < n; i++) {
            int key = a[i];
            int j = i - 1;

            while (j >= 0 && a[j] > key) {
                a[j + 1] = a[j];
                j--;
            }

            a[j + 1] = key;
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

        insertionSort(a);
    }
}
