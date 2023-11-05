public class Test {
    public static void main(String[] args) {
        AVL tree = new AVL();

        int[] keys = { 1, 4, 45, 12, 64, 18, 66, 53, 80, 10 };

        for (int key : keys) {
            tree.insert(key);
        }

        tree.NLR(tree.root);
        System.out.println();
        tree.LNR(tree.root);
        System.out.println();
        tree.LRN(tree.root);
        System.out.println();
        tree.printBF(tree.root);
    }
}
