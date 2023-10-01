import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Ex5
{
    public static void main(String[] args)
    {
        File inputFile = new File("inputEx5.txt");
        File outputFile = new File("outputEx5.txt");

        int sum = 0;

        try 
        {
            Scanner readFile = new Scanner(inputFile);
            FileWriter writeFile = new FileWriter(outputFile);
            while(readFile.hasNextInt())
            {
                int num = readFile.nextInt();
                sum += num;
            }
            readFile.close();

            writeFile.write(Integer.toString(sum));
            writeFile.close();

            System.out.println("Read and write successfully");
        }
        catch (IOException e)
        {
            System.out.println("An error occurred");
            e.printStackTrace();
        }
    }
}