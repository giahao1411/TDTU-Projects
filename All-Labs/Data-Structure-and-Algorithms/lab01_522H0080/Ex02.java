public class Ex02 {
    public static void main(String[] args) {
        MyLinkedList<Fraction> list = new MyLinkedList<>();

        for(int i = 1; i < 10; i++)
        {
            list.addFirst(new Fraction(i, 2*i));
        }

        list.print();

        System.out.println(list.removeCurr(list.getHead()));
        list.print();
    }
}
