public class Ex07 {
    public static void main(String[] args) {
        System.out.println(isPalindrome("abba"));
        System.out.println(isPalindrome("abahbs"));
        System.out.println(isPalindrome("abba"));
    }

    public static boolean isPalindrome(String str) {
        MyStack<Character> stack = new MyStack<>();
        MyQueue<Character> queue = new MyQueue<>();

        for (int i = 0; i < str.length(); i++) {
            stack.push(str.charAt(i));
            queue.enQueue(str.charAt(i));
        }

        while (!stack.isEmpty()) {
            if (!stack.pop().equals(queue.deQueue()))
                return false;
        }
        return true;
    }
}
