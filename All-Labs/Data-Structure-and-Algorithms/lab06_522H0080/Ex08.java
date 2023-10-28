public class Ex08 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 65, 52, 62, 53, 21, 78, 61, 77, 7, 23 };

        for (int key : keys) {
            tree.insert(key);
        }

        System.out.println(tree.sum());
    }
}