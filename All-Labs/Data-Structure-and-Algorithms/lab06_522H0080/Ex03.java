public class Ex03 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 4, 23, 9, 57, 56, 62, 56, 91, 51, 50 };

        for (int key : keys) {
            tree.insert(key);
        }

        tree.RNL(tree.root);
    }
}
