import java.util.Scanner; 

public class TranGiaHao_Bai14
{
    public static void main(String[] args)
    {
        boolean temp = true;

        while(temp)
        {
            Scanner sc = new Scanner(System.in);

            System.out.printf("\n---Menu---\n");
            System.out.println("1. Coca");
            System.out.println("2. Pepsi");
            System.out.println("3. Sprite");
            System.out.println("4. Snack");
            System.out.println("5. Shutdown Machine");
            System.out.print("Please enter a number: ");

            int num = sc.nextInt();

            switch (num) 
            {
                case 1:
                {
                    System.out.print("The price of Coca is 5$, please enter the amount of money: ");
                    int money = sc.nextInt();
                    if(money < 5)
                    {
                        System.out.print("Not enough money to buy this item. Please select again.");
                    }
                    else
                    {
                        System.out.print("Your change is " + (double)(money - 5) + "$");
                    }
                    break;
                }
                case 2:
                {
                    System.out.print("The price of Pepsi is 5$, please enter the amount of money: ");
                    int money = sc.nextInt();
                    if(money < 5)
                    {
                        System.out.print("Not enough money to buy this item. Please select again.");
                    }
                    else
                    {
                        System.out.print("Your change is " + (double)(money - 5) + "$");
                    }
                    break;
                }
                case 3:
                {
                    System.out.print("The price of Sprite is 3$, please enter the amount of money: ");
                    int money = sc.nextInt();
                    if(money < 3)
                    {
                        System.out.print("Not enough money to buy this item. Please select again.");
                    }
                    else
                    {
                        System.out.print("Your change is " + (double)(money - 3) + "$");
                    }
                    break;
                }
                case 4:
                {
                    System.out.print("The price of Snack is 2$, please enter the amount of money: ");
                    int money = sc.nextInt();
                    if(money < 2)
                    {
                        System.out.print("Not enough money to buy this item. Please select again.");
                    }
                    else
                    {
                        System.out.print("Your change is " + (double)(money - 2) + "$");
                    }
                    break;
                }
                case 5:
                {
                    System.out.print("Machine is shutting down.");
                    temp = false;
                    break;
                }
                default:
                {
                    System.out.print("Please enter a valid number.");
                }
            }
        }
    }
}