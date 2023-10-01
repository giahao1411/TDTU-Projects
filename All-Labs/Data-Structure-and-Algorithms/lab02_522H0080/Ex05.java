public class Ex05 {
    public static boolean isBalance(String seq) {
        MyStack<Character> stack = new MyStack<>();
        char ch;

        for (int i = 0; i < seq.length(); i++) {
            ch = seq.charAt(i);
            if (isLeft(ch))
                stack.push(ch);
            if (isRight(ch)) {
                if (!isMatched(stack.pop(), ch))
                    return false;
            }
        }
        return stack.isEmpty();
    }

    private static boolean isMatched(char left, char right) {
        return (left == '(' && right == ')') || (left == '{' && right == '}') || (left == '[' && right == ']');
    }

    private static boolean isLeft(char ch) {
        return ch == '(' || ch == '{' || ch == '[';
    }

    private static boolean isRight(char ch) {
        return ch == ')' || ch == '}' || ch == ']';
    }

    public static void main(String[] args) {
        System.out.println(isBalance("([a{aaa}]bZZ)"));
        System.out.println(isBalance("([a}])"));
        System.out.println(isBalance("([{b)])"));
        System.out.println(isBalance("([{}v]"));
    }
}
