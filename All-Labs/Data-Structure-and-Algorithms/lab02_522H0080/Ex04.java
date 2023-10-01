import java.util.*;

public class Ex04 {
    public static String reverseStr(String s) {
        MyStack<Character> stack = new MyStack<>();
        for (int i = 0; i < s.length(); i++) {
            stack.push(s.charAt(i));
        }

        String res = "";
        while (!stack.isEmpty()) {
            res += stack.pop();
        }
        return res;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a string: ");
        String s = sc.nextLine();

        System.out.println("Reverse your string: " + reverseStr(s));

        sc.close();
    }
}
