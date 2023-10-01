import java.util.ArrayList;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Ex3
{
    public <E> boolean writeFile(String path, ArrayList <E> lst)
    {
        try
        {
            FileWriter writeFile = new FileWriter(path);
            for(E obj : lst)
            {
                writeFile.write(obj.toString() + "\n");
            }
            writeFile.close();
            return true;
        }
        catch (IOException e)
        {
            System.out.println("An error occurred");
            e.printStackTrace();
            return false;
        }
    }

    public static void main(String[] args)
    {
        ArrayList<Student> lstStu = new ArrayList<Student>();
        File outputFileEx3 = new File("outputEx3.txt");

        lstStu.add(new ITStudent("Tran Gia Hao", 8.1, 52200080));
        lstStu.add(new ITStudent("Vo Nhat Hao", 9.2, 52200090));
        lstStu.add(new MathStudent("Nguyen Huynh Anh Khoa", 8.6, "522H0046"));
        lstStu.add(new MathStudent("Pham Bao Long", 9.0, "522H0062"));
        lstStu.add(new ITStudent("Lam Phu Cuong", 10.0, 52200025));

        Ex3 write = new Ex3();

        if(write.writeFile("outputEx3.txt", lstStu))
        {
            System.out.println("Write to file successfully");
        }
        else
        {
            System.out.println("Failed to write");
        }
    }
}
