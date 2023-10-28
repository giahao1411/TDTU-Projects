public class Ex11 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 35, 67, 69, 78, 76, 97, 26, 77, 64, 72 };

        for (int key : keys) {
            tree.insert(key);
        }

        System.out.println(tree.sumEvenKeysAtLeaves());
    }
}
