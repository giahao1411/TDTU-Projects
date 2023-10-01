class DoubleNode<E> {
    private E element;
    private DoubleNode<E> prev;
    private DoubleNode<E> next;

    public DoubleNode() {
    }

    public DoubleNode(E element, DoubleNode<E> prev, DoubleNode<E> next) {
        this.element = element;
        this.prev = prev;
        this.next = next;
    }

    public DoubleNode(E item) {
        this(item, null, null);
    }

    public E getElement() {
        return element;
    }

    public DoubleNode<E> getPrev() {
        return prev;
    }

    public DoubleNode<E> getNext() {
        return next;
    }

    public void setPrev(DoubleNode<E> prev) {
        this.prev = prev;
    }

    public void setNext(DoubleNode<E> next) {
        this.next = next;
    }
}
