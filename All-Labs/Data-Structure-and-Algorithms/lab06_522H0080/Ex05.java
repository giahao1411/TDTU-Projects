public class Ex05 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 2, 18, 21, 37, 67, 16, 23, 87, 93, 7 };

        for (int key : keys) {
            tree.insert(key);
        }

        tree.LNR(tree.root);
        System.out.println();
        tree.deleteMax();
        tree.LNR(tree.root);
    }
}
