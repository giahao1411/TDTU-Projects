KOclass QueueUsingStack<E> extends MyStack<E> implements QueueInterface<E> {
    MyStack<E> stack1 = new MyStack<>();
    MyStack<E> stack2 = new MyStack<>();

    private void pushToStack() {
        while (!stack1.isEmpty()) {
            stack2.push(stack1.pop());
        }
    }

    @Override
    public void enQueue(E item) {
        stack1.push(item);
    }

    @Override
    public E deQueue() {
        pushToStack();
        return stack2.pop();
    }

    @Override
    public E getFront() {
        pushToStack();
        return stack2.getPeek();
    }

    public void print() {
        pushToStack();
        if (!stack2.isEmpty())
            stack2.print();
    }
}
