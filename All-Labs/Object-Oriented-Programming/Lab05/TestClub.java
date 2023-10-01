public class TestClub
{
    public static void main(String[] args)
    {
        Club cl1 = new Club();
        Club cl2 = new Club("Manchester United", 4, 5, 1);
        Club cl3 = new Club(new Club("Bayern Munich", 8, 2, 0));

        System.out.println(cl1);
        System.out.println(cl2);
        System.out.println(cl3);
        System.out.println("Club 1: num matches played: " + cl1.numMatchesPlayed());
        System.out.println("Club 2: is finish: " + cl2.isFinish());
        System.out.println("Club 3: club points: " + cl3.getPoints());
    }
}