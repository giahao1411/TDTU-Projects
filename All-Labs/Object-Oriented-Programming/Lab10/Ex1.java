//Outer class
class Student
{
    String name;
    String address;
    String sex;
    double score;

    //Constructor with all attributes
    public Student(String name, String address, String sex, double score)
    {
        this.name = name;
        this.address = address;
        this.sex = sex;
        this.score = score;
    }

    //Inner class
    class StudentOperator
    {
        //print method 
        void print()
        {
            System.out.println("[" + name + ", " + address + ", " + sex + ", " + score + "]");
        }

        //type method
        String type()
        {
            if (score > 8)
                return "A";
            if (score < 5)
                return "C";
            return "B";
        }
    }
}

//Main class
public class Ex1
{
    public static void main(String[] args)
    {
        //Initiate an obj of outer class 
        Student stu = new Student("Tran Gia Hao", "TPHCM", "Male", 8.1);

        //Initiate an obj of inner class
        Student.StudentOperator operator = stu.new StudentOperator();
        
        //Test case
        operator.print();
        System.out.println("Stundent type: " + operator.type());

        /*Another way using ArrayList for more student require - need 'import java.util.ArrayList;'

        ArrayList<Student> lstStu = new ArrayList<>();

        lstStu.add(new Student(...));
        ...

        for(Student stu : lstStu)
        {
            Student.StudentOperator operator = stu.new StudentOperator();
            operator.print();
            System.out.println("Student type: " + operator.type());
            System.out.println();
        }
        */
    }
}