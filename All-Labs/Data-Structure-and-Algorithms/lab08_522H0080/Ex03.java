import java.util.Arrays;

public class Ex03 {
    // using build heap slow
    public static void heapSortAsc(int[] arr) {
        MinHeap heap = new MinHeap(arr.length);
        for (int key : arr) {
            heap.insert(key);
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = heap.extractMin();
        }
    }

    // using build heap slow
    public static void heapSortDesc(int[] arr) {
        MaxHeap heap = new MaxHeap(arr.length);
        for (int key : arr) {
            heap.insert(key);
        }
        for (int i = 0; i < arr.length; i++) {
            arr[i] = heap.extractMax();
        }
    }

    // using build heap fast
    public static void heapSortAscF(int[] arr) {
        MinHeap heap = new MinHeap(arr.length);
        heap.buildHeapFast(arr);

        for (int i = 0; i < arr.length; i++) {
            arr[i] = heap.extractMin();
        }
    }

    // using build heap fast
    public static void heapSortDescF(int[] arr) {
        MaxHeap heap = new MaxHeap(arr.length);
        heap.buildHeapFast(arr);

        for (int i = 0; i < arr.length; i++) {
            arr[i] = heap.extractMax();
        }
    }

    public static void main(String[] args) {
        int[] arr = { 15, 23, 18, 63, 21, 35, 36, 21, 66, 12, 42, 35, 75, 23, 64, 78, 39 };

        System.out.println(Arrays.toString(arr));
        System.out.println("Sort using build heap slow");
        heapSortAsc(arr);
        System.out.println(Arrays.toString(arr));
        heapSortDesc(arr);
        System.out.println(Arrays.toString(arr));
        System.out.println("Sort using build heap fast");
        heapSortAscF(arr);
        System.out.println(Arrays.toString(arr));
        heapSortDescF(arr);
        System.out.println(Arrays.toString(arr));
    }
}
