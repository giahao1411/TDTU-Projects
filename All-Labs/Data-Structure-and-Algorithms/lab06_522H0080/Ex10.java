public class Ex10 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 12, 62, 23, 11, 47, 54, 14, 66, 59, 35 };

        for (int key : keys) {
            tree.insert(key);
        }

        System.out.println(tree.countLeaves());
    }
}
