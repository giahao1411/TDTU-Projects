class BST {
    Node root;

    public void insert(Integer key) {
        root = insert(root, key);
    }

    private Node insert(Node x, Integer key) {
        if (x == null)
            return new Node(key);
        int cmp = key.compareTo(x.key);
        if (cmp < 0)
            x.left = insert(x.left, key);
        else if (cmp > 0)
            x.right = insert(x.right, key);
        else
            x.key = key;
        return x;
    }

    public Node search(Integer key) {
        return search(root, key);
    }

    private Node search(Node x, Integer key) {
        if (x == null)
            return null;
        int cmp = key.compareTo(x.key);
        if (cmp < 0)
            return search(x.left, key);
        else if (cmp > 0)
            return search(x.right, key);
        else
            return x;
    }

    public Node min() {
        return min(root);
    }

    private Node min(Node x) {
        if (x.left == null)
            return x;
        else
            return min(x.left);
    }

    public Node max() {
        return max(root);
    }

    private Node max(Node x) {
        if (x.right == null)
            return x;
        else
            return max(x.right);
    }

    public Node deleteMin() {
        return deleteMin(root);
    }

    private Node deleteMin(Node x) {
        if (x.left == null)
            return x.right;
        x.left = deleteMin(x.left);
        return x;
    }

    public void delete(Integer key) {
        root = delete(root, key);
    }

    private Node delete(Node x, Integer key) {
        if (x == null)
            return null;
        int cmp = key.compareTo(x.key);
        if (cmp < 0)
            x.left = delete(x.left, key);
        else if (cmp > 0)
            x.right = delete(x.right, key);
        else {
            // node with only one child or no child
            if (x.right == null)
                return x.left;
            if (x.left == null)
                return x.right;
            // node with two children: Get the successor (smallest in the right subtree)
            x.key = min(x.right).key;
            x.right = deleteMin(x.right);
        }
        return x;
    }

    public void NLR(Node x) {
        if (x != null) {
            System.out.print(x.key + " ");
            NLR(x.left);
            NLR(x.right);
        }
    }

    public void LNR(Node x) {
        if (x != null) {
            LNR(x.left);
            System.out.print(x.key + " ");
            LNR(x.right);
        }
    }

    public void LRN(Node x) {
        if (x != null) {
            LNR(x.left);
            LNR(x.right);
            System.out.print(x.key + " ");
        }
    }

    // Exercise 3:
    public void RNL(Node x) {
        if (x != null) {
            RNL(x.right);
            System.out.print(x.key + " ");
            RNL(x.left);
        }
    }

    // Exercise 4:
    public boolean contains(Integer key) {
        return search(key) != null;
    }

    // Exercise 5:
    public void deleteMax() {
        deleteMax(root);
    }

    private Node deleteMax(Node x) {
        if (x.right == null)
            return x.left;
        x.right = deleteMax(x.right);
        return x;
    }

    // Exercise 6:
    public void delete_pre(Integer key) {
        root = delete_pre(root, key);
    }

    private Node delete_pre(Node x, Integer key) {
        if (x == null)
            return null;
        int cmp = key.compareTo(x.key);
        if (cmp < 0)
            x.left = delete(x.left, key);
        else if (cmp > 0)
            x.right = delete(x.right, key);
        else {
            // node with only one child or no child
            if (x.right == null)
                return x.left;
            if (x.left == null)
                return x.right;
            // node with two children: Get the predecessor (largest in the left subtree)
            x.key = max(x.left).key;
            x.left = deleteMax(x.left);
        }
        return x;
    }

    // Exercise 7:
    public int height() {
        return height(root);
    }

    private int height(Node x) {
        if (x == null)
            return -1;
        int lh = height(x.left);
        int rh = height(x.right);
        return Math.max(lh, rh) + 1;
    }

    // Exercise 8:
    public Integer sum() {
        return sum(root);
    }

    private Integer sum(Node x) {
        if (x == null)
            return 0;
        return x.key + sum(x.left) + sum(x.right);
    }

    // Exercise 9:
    public Integer sumEven() {
        return sumEven(root);
    }

    private Integer sumEven(Node x) {
        if (x == null)
            return 0;
        if (x.key % 2 == 0)
            return x.key + sumEven(x.left) + sumEven(x.right);
        return sumEven(x.left) + sumEven(x.right);
    }

    // Exercise 10:
    public int countLeaves() {
        return countLeaves(root);
    }

    private int countLeaves(Node x) {
        if (x == null)
            return 0;
        if (x.left == null && x.right == null)
            return 1 + countLeaves(x.left) + countLeaves(x.right);
        return countLeaves(x.left) + countLeaves(x.right);
    }

    // Exercise 11:
    public int sumEvenKeysAtLeaves() {
        return sumEvenKeysAtLeaves(root);
    }

    private int sumEvenKeysAtLeaves(Node x) {
        if (x == null)
            return 0;
        if ((x.left == null && x.right == null) && (x.key % 2 == 0))
            return x.key + sumEvenKeysAtLeaves(x.left) + sumEvenKeysAtLeaves(x.right);
        return sumEvenKeysAtLeaves(x.left) + sumEvenKeysAtLeaves(x.right);
    }
}