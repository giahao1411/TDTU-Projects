import java.util.ArrayList;

public class PersonModel <T>
{
    private ArrayList<T> al = new ArrayList<T>();

    public void add(T obj)
    {
        al.add(obj);
    }

    public void display()
    {
        for(T obj : al)
        {
            System.out.println(obj);
        }
    }

    public static void main(String[] args)
    {
        //obj Student for PersonModel
        PersonModel<Student> student = new PersonModel<Student>();

        student.add(new Student("522H0080", 8.1, "Tran Gia Hao", 2004));
        student.add(new Student("22512", 9.1, "Quach Chan Long", 2004));
        student.display();

        System.out.println();

        //obj Employee for PersonModel
        PersonModel<Employee> employee = new PersonModel<Employee>();

        employee.add(new Employee("12a", 23.0, "Le Khai Minh", 2004));
        employee.add(new Employee("12i", 25.0, "Dao Cu Dat", 2004));
        employee.display();

        System.out.println();

        //obj Person for PersonModel
        PersonModel<Person> person = new PersonModel<Person>();

        person.add(new Person("Nguyen Huynh Anh Khoa", 2004));
        person.add(new Person("Pham Bao Long", 2004));
        person.display();
    }
}