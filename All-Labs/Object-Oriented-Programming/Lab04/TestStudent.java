public class TestStudent
{
    public static void main(String[] args)
    {
        Student st1 = new Student(5220080, "Tran", "Hao");
        Student st2 = new Student(5220046, "Nguyen", "Khoa");

        System.out.println("Full name: " + st1.getName());
        System.out.println("Student: " + st1);
        System.out.println("Full name: " + st2.getName());
        System.out.println("Student: " + st2);
    }
}