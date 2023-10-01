//using Scanner and HashMap
import java.util.*;

public class Dictionary
{
    public static void main(String[] args)
    {
        HashMap<String, String> dictionary = new HashMap<>();
        dictionary.put("english", "Tieng Anh");
        dictionary.put("dog", "Con cho");
        dictionary.put("attention", "Su chu y");
        dictionary.put("communicate", "Giao tiep");
        dictionary.put("polygon", "Hinh da giac");
        dictionary.put("accommodation", "Noi o");
        dictionary.put("headphone", "Tai nghe chup tai");
        dictionary.put("awesome", "Tuyet voi");
        dictionary.put("animation", "Hoat hinh");
        dictionary.put("technology", "Cong nghe");

        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter a word to look up or enter 'close' to exit: ");
        String word = sc.nextLine();

        while(!word.equals("close"))
        {
            if(dictionary.containsKey(word))
            {
                System.out.println("Meaning of " + word + " is: " + dictionary.get(word));
            }
            else
            {
                System.out.println("The word " + word + " does not exist in the dictionary");
            }

            System.out.print("Enter a word to look up another word or enter 'close' to exit: ");
            word = sc.nextLine();
        }

        sc.close();
    }
}