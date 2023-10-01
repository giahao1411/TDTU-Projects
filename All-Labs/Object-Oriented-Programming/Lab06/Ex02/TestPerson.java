public class TestPerson
{
    public static void main(String[] args)
    {
        Person p1 = new Person("Tran Gia Hao", "199/54 Le Quang Sung");
        Student st1 = new Student(p1.getName(), p1.getAddress(), "Information Technology", 2022, 41000000);
        Staff sf1 = new Staff(p1.getName(), p1.getAddress(), "Ton Duc Thang University", 23000);

        System.out.println(p1);
        System.out.println(st1);
        System.out.println(sf1);
    }
}