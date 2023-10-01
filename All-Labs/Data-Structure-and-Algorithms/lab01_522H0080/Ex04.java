public class Ex04 {
    public static void main(String[] args) {
        MyDoubleLinkedList<Double> list = new MyDoubleLinkedList<>();

        for (double i = 1; i < 10; i++) {
            list.addFirst(i);
        }
        list.print();

        DoubleNode<Double> curr = list.getHead().getNext().getNext();
        System.out.println(curr.getPrev().getElement());

        list.removeFirst();
        list.print();

        curr = list.getHead().getNext().getNext();
        System.out.println(curr.getPrev().getElement());

        // curr = null;
        list.removeAfter(curr);
        list.print();
    }
}
