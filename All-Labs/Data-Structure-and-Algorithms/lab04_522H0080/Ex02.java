import java.util.*;

class Ex02 {
    public static void main(String[] args) {
        Student[] arrStu = new Student[5];

        arrStu[0] = new Student("Bruce Lee", 7.0, 8.2, 8.4);
        arrStu[1] = new Student("Amber Heard", 9.0, 2.7, 6.7);
        arrStu[2] = new Student("Adobe Hitman", 6.7, 5.8, 8.7);
        arrStu[3] = new Student("Lil Luyen", 7.8, 6.9, 9.2);
        arrStu[4] = new Student("V", 8.7, 4.7, 8.5);

        System.out.println(Arrays.toString(arrStu));

        System.out.println();
        System.out.println("Ascending order:");
        Arrays.sort(arrStu, new StudentComparatorAsc());
        System.out.println(Arrays.toString(arrStu));

        System.out.println();
        System.out.println("Descending order:");
        Arrays.sort(arrStu, new StudentComparatorDesc());
        System.out.println(Arrays.toString(arrStu));

    }
}
