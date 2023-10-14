import java.util.Stack;

class Ex01 {
    public static int calculate(String s) {
        Stack<Integer> stack = new Stack<>();
        String[] expression = s.split(" ");

        for (String part : expression) {
            if (!isOperator(part))
                stack.push(Integer.parseInt(part));
            else {
                int op1 = stack.pop();
                int op2 = stack.pop();
                stack.push(compute(op1, op2, part));
            }
        }
        return stack.pop();
    }

    private static boolean isOperator(String s) {
        return s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/");
    }

    private static int compute(int op1, int op2, String operator) {
        switch (operator) {
            case "+":
                return op1 + op2;
            case "-":
                return op2 - op1;
            case "*":
                return op1 * op2;
            case "/":
                return op2 / op1;
            default:
                return 0;
        }
    }

    public static void main(String[] args) {
        System.out.println(calculate("9 2 - 6 * 7 + 7 /"));
    }
}