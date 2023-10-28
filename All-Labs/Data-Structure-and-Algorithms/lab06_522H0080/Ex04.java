public class Ex04 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 86, 78, 91, 43, 90, 97, 1, 54, 36, 93 };

        for (int key : keys) {
            tree.insert(key);
        }

        System.out.println(tree.contains(2));
    }
}
