public class Ex09 {
    public static void main(String[] args) {
        BST tree = new BST();

        int[] keys = { 98, 71, 93, 63, 38, 45, 65, 9, 60, 96 };

        for (int key : keys) {
            tree.insert(key);
        }

        System.out.println(tree.sumEven());
    }
}