import java.util.*;

public class EL extends Graph {
    LinkedList<Edge> el;

    @Override
    public void read() {
        Scanner sc = new Scanner(System.in);
        this.V = sc.nextInt();
        this.E = sc.nextInt();
        this.el = new LinkedList<>();

        int src, dest, weight;
        for (int i = 0; i < E; i++) {
            src = sc.nextInt();
            dest = sc.nextInt();
            weight = sc.nextInt();
            el.add(new Edge(src, dest, weight));
        }
        sc.close();
    }

    @Override
    public void print() {
        System.out.println(V + " , " + E);
        for (Edge e : el) {
            System.out.println(e);
        }
    }

    @Override
    public boolean isAdjacent(int u, int v) {
        for (Edge e : el) {
            if (e.src == u && e.dest == v || e.src == v && e.dest == u)
                return true;
        }
        return false;
    }
}
