public class Ex06 {
    public static void main(String[] args) {
        QueueUsingStack<Integer> queueUS = new QueueUsingStack<>();

        for (int i = 1; i < 6; i++) {
            queueUS.enQueue(i);
        }
        queueUS.print();

        System.out.println(queueUS.getFront());
        queueUS.deQueue();
        queueUS.print();
    }
}
