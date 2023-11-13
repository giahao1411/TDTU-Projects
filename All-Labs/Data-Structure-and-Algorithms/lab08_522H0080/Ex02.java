public class Ex02 {
    public static void main(String[] args) {
        int[] keys = { 1, 4, 34, 23, 45, 23, 54, 12, 312 };

        MinHeap heap = new MinHeap(keys.length);

        for (int key : keys) {
            heap.insert(key);
        }

        heap.buildHeapFast(keys);
        System.out.println(heap.extractMin());
    }
}
