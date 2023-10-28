public class Ex02 {
    public static BST createTree(String strKey) {
        BST tree = new BST();

        for (String key : strKey.split(" ")) {
            tree.insert(Integer.parseInt(key));
        }

        return tree;
    }

    public static void main(String[] args) {
        String strKey = "42 68 21 58 59 9 80 66 65 45";
        BST tree = createTree(strKey);

        tree.LNR(tree.root);
    }
}
