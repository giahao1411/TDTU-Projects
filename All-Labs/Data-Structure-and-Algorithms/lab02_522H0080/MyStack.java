class MyStack<E> extends MyLinkedList<E> implements StackInterface<E> {
    @Override
    public void push(E item) {
        addFirst(item);
    }

    @Override
    public E pop() {
        return removeFirst();
    }

    @Override
    public E getPeek() {
        return getFirst();
    }
}
