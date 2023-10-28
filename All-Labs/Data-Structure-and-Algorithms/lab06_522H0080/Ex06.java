public class Ex06 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 42, 64, 32, 68, 85, 26, 86, 36, 89, 15 };

        for (int key : keys) {
            tree.insert(key);
        }

        tree.LNR(tree.root);
        System.out.println();
        tree.delete_pre(tree.root.left.key);
        tree.LNR(tree.root);
        System.out.println();
    }
}
