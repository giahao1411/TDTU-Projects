class Ex01 {
    public static void main(String[] args) {
        MyStack<Fraction> stack = new MyStack<>();
        MyQueue<Fraction> queue = new MyQueue<>();

        for (int i = 1; i < 6; i++) {
            stack.push(new Fraction(i, 2 * i + 1));
            queue.enQueue(new Fraction(i, 2 * i + 1));
        }

        stack.print();
        queue.print();
    }
}
