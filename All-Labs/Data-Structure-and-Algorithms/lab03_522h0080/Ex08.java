import java.util.NoSuchElementException;

class Ex08 {
    public static void sortList(MyLinkedList<Integer> list) {
        if (!list.isEmpty()) {
            Node<Integer> currNode = list.getHead();

            // using selection sort structure
            while (currNode != null) {
                Node<Integer> minNode = findMinNode(currNode);
                swapNode(currNode, minNode);
                currNode = currNode.getNext();
            }
        } else
            throw new NoSuchElementException("The list is empty");
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

    public static void addSortedList(MyLinkedList<Integer> list, int item) {
        sortList(list);
        Node<Integer> prev = list.getHead();
        Node<Integer> curr = prev.getNext();

        while (curr != null) {
            if (item > prev.getData() && item < curr.getData()) {
                list.addAfter(prev, item);
                break;
            }
            if (item < prev.getData()) {
                list.addFirst(item);
                break;
            }
            prev = prev.getNext();
            curr = curr.getNext();
        }
    }

    public static void main(String[] args) {
        MyLinkedList<Integer> list = new MyLinkedList<>();

        list.addLast(5);
        list.addLast(1);
        list.addLast(3);
        list.addLast(2);

        list.print();
        sortList(list);
        list.print();
        addSortedList(list, 4);
        addSortedList(list, 0);
        list.print();
    }
}
