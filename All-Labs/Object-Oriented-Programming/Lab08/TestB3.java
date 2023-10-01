import java.util.ArrayList;

public class TestB3
{
    public ArrayList<StudentB3> findStudent(ArrayList<StudentB3> lstStu)
    {
        ArrayList<StudentB3> res = new ArrayList<>();

        for(StudentB3 s : lstStu)
        {
            String rank = s.getRank();
            if(rank.equals("A") || rank.equals("Passed"))
            {
                res.add(s);
            }
        }
        return res;
    }

    public static void main(String[] args)
    {
        ArrayList<StudentB3> lstStu = new ArrayList<>();

        lstStu.add(new ITStudent(5220080, "Tran Gia Hao", 8.1));
        lstStu.add(new MathStudent("522H0080", "Nguyen Van A", 7.6));
        lstStu.add(new ITStudent(5220046, "Nguyen Huynh Anh Khoa", 9.0));
        lstStu.add(new MathStudent("522H0324", "Tran Van B", 4.9));

        System.out.println("Students:");

        for(StudentB3 stu :lstStu)
        {
            System.out.println(stu);
        }

        System.out.println("Students who reach rank A or Pass:");

        TestB3 find = new TestB3();

        ArrayList<StudentB3> result = find.findStudent(lstStu);

        for(StudentB3 stu1 : result)
        {
            System.out.println(stu1);
        }
    }
}