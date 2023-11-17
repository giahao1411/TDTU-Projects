import java.util.*;

public class Main {
    public static void main(String[] args) {
        EL g = new EL();

        g.read();
        g.print();
        System.out.println(g.isAdjacent(0, 1));

        Collections.sort(g.el);
        g.print();
    }
}
