import java.io.File;
import java.io.IOException;
import java.io.FileWriter;
import java.util.Scanner;

/* to read and write data with new line in the input file
you can comment codes from line 13 to 18 and codes from 24 to 36 */

public class Ex2
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a sentence: ");
        String userEnter = sc.nextLine();

        sc.close();

        File inputFile = new File("input.txt");
        File outputFile = new File("output.txt");

        //try-catch to write to input file
        try
        {
            //write the enter from user to input.txt
            FileWriter writeFile = new FileWriter(inputFile);
            writeFile.write(userEnter);
            writeFile.close();
            System.out.println("Write successfully");
        }
        catch (IOException e)
        {
            System.out.println("An error occurred");
            e.printStackTrace();
        }

        //try-catch to read from input file then write to the output file
        try 
        {
            //read and write data from input file
            Scanner readFile = new Scanner(inputFile);
            FileWriter writeData = new FileWriter(outputFile);
            while(readFile.hasNextLine())
            {
                String inputData = readFile.nextLine();
                String outputText = inputData.toUpperCase();
                writeData.write(outputText + "\n");
            }
            readFile.close();
            writeData.close();
            System.out.println("Read and Write successfully");
        }
        catch (IOException e)
        {
            System.out.println("An error occurred");
            e.printStackTrace();
        }
    }
}