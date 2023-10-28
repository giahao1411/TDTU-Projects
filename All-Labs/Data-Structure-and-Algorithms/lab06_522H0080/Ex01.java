public class Ex01 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 41, 96, 82, 74, 4, 43, 64, 96, 19, 46 };

        for (int key : keys) {
            tree.insert(key);
        }

        tree.LNR(tree.root);
        System.out.println();
        tree.delete(tree.root.key);
        tree.LNR(tree.root);
        System.out.println();
    }
}
