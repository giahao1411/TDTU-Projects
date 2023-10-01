import java.util.*;

public class Ex03 {
    public static int countEven(MyLinkedList<Integer> list) {
        int count = 0;
        for (Node<Integer> n = list.getHead(); n != null; n = n.getNext()) {
            if (n.getData() % 2 == 0)
                count++;
        }
        return count;
    }

    public static int countPrime(MyLinkedList<Integer> list) {
        int count = 0;
        for (Node<Integer> n = list.getHead(); n != null; n = n.getNext()) {
            if (isPrime(n.getData()))
                count++;
        }
        return count;
    }

    public static boolean isPrime(int x) {
        if (x <= 1)
            return false;
        for (int i = 2; i <= x / 2; i++) {
            if (x % i == 0)
                return false;
        }
        return true;
    }

    public static void addBeforeFirstEven(MyLinkedList<Integer> list, int x) {
        if (!list.isEmpty()) {
            Node<Integer> n = list.getHead();
            if (n.getData() % 2 == 0) {
                list.addFirst(x);
                return;
            }

            Node<Integer> pre = null;
            while (n.getData() % 2 != 0) {
                pre = n;
                n = n.getNext();
            }

            if (n != null)
                list.addAfter(pre, x);
        }
    }

    public static int findMax(MyLinkedList<Integer> list) {
        Node<Integer> n = list.getHead();
        int max = n.getData();
        for (int i = 1; i < list.size(); i++) {
            n = n.getNext();
            if (n.getData() > max)
                max = n.getData();
        }
        return max;
    }

    public static void reverseList(MyLinkedList<Integer> list) {
        if (!list.isEmpty()) {
            list.addFirst(list.removeLast());
            Node<Integer> n = list.getHead();
            for (int i = 0; i < list.size() - 1; i++) {
                list.addAfter(n, list.removeLast());
                n = n.getNext();
            }
        }
    }

    public static void sortAscList(MyLinkedList<Integer> list) {
        if (!list.isEmpty()) {
            Node<Integer> curr = list.getHead();

            while (curr != null) {
                Node<Integer> minNode = findMinNode(curr);
                swapNode(curr, minNode);
                curr = curr.getNext();
            }
            list.print();
        } else
            throw new NoSuchElementException("No node to sort");
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

        // for (int i = 1; i < 10; i++) {
        // list.addFirst(i);
        // }

        list.addFirst(6);
        list.addLast(8);
        list.addFirst(1);
        list.addFirst(12);
        list.addLast(3);

        list.print();
        System.out.println("Numbers of even in ListNode: " + countEven(list));
        System.out.println("Nmubers of prime in ListNode: " + countPrime(list));

        addBeforeFirstEven(list, 90);
        list.print();

        System.out.println("Max element in ListNode is: " + findMax(list));

        reverseList(list);
        list.print();

        System.out.println("Sort ascending order of the list:");
        sortAscList(list);
    }
}
