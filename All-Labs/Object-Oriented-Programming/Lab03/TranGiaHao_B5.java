import java.util.*;

public class TranGiaHao_B5
{
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Nhap vao 1 chuoi:");
        String paragraph = sc.nextLine();

        System.out.println("Dem so tu xuat hien trong chuoi:");
        countWordsAppear(paragraph);
    }

    public static void countWordsAppear(String paragraph)
    {
        //chuyen cac chu cai ve viet thuong va cac dau 
        String cleanStr = paragraph.toLowerCase().replaceAll("[,.!?;:()+-_*/<>=]", "");
        String[] words = cleanStr.split(" ");

        //tao 1 HashMap chua key la String, value la integer
        HashMap<String, Integer> wordCount = new HashMap<>();

        for(String word: words)
        {
            //kiem tra xem tu do co trong HashMap chua
            if(wordCount.containsKey(word))                                 //containKey(key): kiem tra xem key da ton tai trong HashMap chua
            {
                //Neu co thi cong so lan xuat hien len 1 lan
                wordCount.put(word, wordCount.get(word) + 1);               //put(key,value): them entry moi voi key va value tuong ung
            }                                                               //get(key): tra ve gia tri cua key do                                      
            else    
            {
                //Khong co thi khoi tao key = word, value = 1
                wordCount.put(word, 1);                                 
            }
        }
        //in cac tu va so lan xuat hien 
        for(String word : wordCount.keySet())                               //keySet(): tra ve mot tap hop chua tat ca key trong HashMap
        {
            System.out.println(word + ": " + wordCount.get(word));
        }
    }
}