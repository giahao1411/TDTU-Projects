import java.util.*;

public class AL extends Graph {
    LinkedList<Edge>[] al;

    @Override
    public void read() {
        Scanner sc = new Scanner(System.in);

        this.V = sc.nextInt();
        this.E = sc.nextInt();
        this.al = new LinkedList[V];

        for (int i = 0; i < V; i++) {
            al[i] = new LinkedList<>();
        }

        int src, dest, weight;
        for (int i = 0; i < E; i++) {
            src = sc.nextInt();
            dest = sc.nextInt();
            weight = sc.nextInt();
            al[src].add(new Edge(src, dest, weight));
            al[dest].add(new Edge(dest, src, weight));
        }
        sc.close();
    }

    @Override
    public void print() {
        System.out.println(V + ", " + E);
        for (int i = 0; i < V; i++) {
            System.out.print(i + ": ");
            System.out.println(al[i]);
        }
    }

    @Override
    public boolean isAdjacent(int u, int v) {
        for (Edge e : al[u]) {
            if (e.dest == v)
                return true;
        }
        return false;
    }
}