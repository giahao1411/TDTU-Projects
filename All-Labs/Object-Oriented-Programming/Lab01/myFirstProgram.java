// Vi du 1

public class myFirstProgram {
	public static void main (String[] args) {
		System.out.println("Hello World!");
	}
}

// Vi du 2
/*
public class myFirstProgram {
	public static void main(String[] args) {
		int a = 5, b = 10;
		int sum = a + b;
		System.out.println(a + " + " +  b + " = " + sum);
	}
}
*/

// Vi du 3
/*
public class myFirstProgram {
	public static void main(String[] args) {
		int i = 1, sum = 0;
		while (i <= 10) {
			sum = sum + i;
			i++;
		}
		System.out.println("Sum = " + sum);
	}
}
*/

// Vi du 4
/*
public class myFirstProgram {
	public static void main (String[] args ) {
		int sum = 0;
		for (int i = 1; i <= 10; i++) {
			sum += i;
		}
		System.out.println("Sum = " + sum);
	}
}
*/

// Vi du 5
/*
public class myFirstProgram {
	public static void main(String[] args) {
		int i = 0, sum = 0;
		do {
			sum = sum + i;
			i++;
		} while (i <= 10);
		System.out.println("Sum = " + sum);
	}
}
*/

// Vi du 6
/*
public class myFirstProgram {
	public static void main(String[] args) {
		int x = 12;
		if (x % 2 == 0) {
			System.out.println(x + " is even");
		} else {
			System.out.println(x + " is odd");
		}
	}
}
*/

// Vi du 7
/*
public class myFirstProgram {
	public static void main(String[] args) {
		int x = 11, y = 12;
		if (x < y && x + y >= 10) {
			System.out.println("True");
		} else {
			System.out.println("False");
		}
	}
}
*/

// Vi du 8
/*
public class myFirstProgram {
	public static int findMax(int a, int b) {
		return a > b ? a : b;
	}
	public static void main(String[] args) {
		int x = 5, y = 6;
		System.out.println("Max is " + findMax(x, y));
	}
}
*/

// Vi du 9
/*
public class myFirstProgram {
	public static void main(String[] args) {
		System.out.print("Hello! ");
		System.out.print("Hello! ");
		System.out.print("Hello! ");
	}
}
*/

// Vi du 10
/*
public class myFirstProgram{
	public static void main(String[] args) {
		System.out.println("Hello! ");
		System.out.println("Hello! ");
		System.out.println("Hello! ");
	}
}
*/

// Vi du 11
/*
public class myFirstProgram {
	public static void main(String[] args) {
		int x = 100;
		System.out.printf("Printing simple" + " integer: x = %d\n", x);
		System.out.printf("Formatted with" + " precision: PI = %.2f\n", Math.PI);

		float n = 5.2f;
		System.out.printf("Formatted to " + "specific width: n = %.4f\n", n);
		
		n = 2324435.3f;
		System.out.printf("Formatted to " + "right margin: n = %20.4f\n", n);
	}
}
*/

// Vi du 12
/*
import java.util.Scanner;

public class myFirstProgram {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // Create a scanner project
		
		String name = sc.nextLine(); // Read user's input
		int age = sc.nextInt();

		System.out.println("Name: " + name); // Print user's input
		System.out.println("Age: " + age);
	}
}
*/

