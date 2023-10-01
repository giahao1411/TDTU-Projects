class haha {
    public static void sortAscList(MyLinkedList<Integer> list) {
        if (!list.isEmpty()) {
            Node<Integer> curr = list.getHead();
            while (curr != null) {
                Node<Integer> minNode = findMinNode(curr);
                swapNode(curr, minNode);
                curr = curr.getNext();
            }
            list.print();
        }
    }

    private static Node<Integer> findMinNode(Node<Integer> node) {
        Node<Integer> minNode = node;
        Node<Integer> currNode = node.getNext();

        while (currNode != null) {
            if (currNode.getData() < minNode.getData())
                minNode = currNode;
            currNode = currNode.getNext();
        }
        return minNode;
    }

    private static void swapNode(Node<Integer> node1, Node<Integer> node2) {
        int temp = node1.getData();
        node1.setData(node2.getData());
        node2.setData(temp);
    }

    public static void main(String[] args) {
        MyLinkedList<Integer> list = new MyLinkedList<>();

        list.addLast(9);
        list.addLast(5);
        list.addLast(3);
        list.addLast(4);

        list.print();

        sortAscList(list);
    }
}