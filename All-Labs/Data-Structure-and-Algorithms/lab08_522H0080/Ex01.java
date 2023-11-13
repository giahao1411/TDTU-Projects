public class Ex01 {
    public static void main(String[] args) {
        int[] keys = { 1, 3, 4, 1, 2, 4, 2, 21, 11, 77 };

        MaxHeap heap = new MaxHeap(keys.length);

        for (int key : keys) {
            heap.insert(key);
        }

        System.out.println(heap.extractMax());
    }
}
