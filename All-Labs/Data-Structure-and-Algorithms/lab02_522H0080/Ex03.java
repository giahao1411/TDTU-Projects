import java.lang.Math;

public class Ex03 {
    public static void main(String[] args) {
        System.out.println("Recursive solution: " + recursiveSolution(12));
        System.out.println("Stack solution: " + stackSolution(12));

        for (int i = 1; i < 4; i++) {
            System.out.println(stackSolution(i));
        }
    }

    public static int recursiveSolution(int n) {
        return n == 1 ? 3 : (int) Math.pow(2, n) + n * n + recursiveSolution(n - 1);
    }

    public static int stackSolution(int n) {
        MyStack<Integer> stack = new MyStack<>();
        stack.push(3);

        for (int i = 2; i <= n; i++) {
            stack.push((int) Math.pow(2, i) + i * i);
        }

        int res = 0;
        while (!stack.isEmpty()) {
            res += stack.pop();
        }
        return res;
    }
}
