public class Ex07 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 62, 43, 99, 84, 58, 66, 75, 96, 7, 32 };

        for (int key : keys) {
            tree.insert(key);
        }

        System.out.println(tree.height());
    }
}
