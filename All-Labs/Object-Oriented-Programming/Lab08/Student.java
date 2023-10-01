public class Student extends Person
{
    private String ID;
    private double score;

    public Student()
    {
        super();
        this.ID = "";
        this.score = 0.0;
    }

    public Student(String ID, double score, String name, int birthYear)
    {
        super(name, birthYear);
        this.ID = ID;
        this.score = score;
    }

    public String getID()
    {
        return this.ID;
    }

    public void setID(String ID)
    {
        this.ID = ID;
    }

    public double getScore()
    {
        return this.score;
    }

    public void setScore(double score)
    {
        this.score = score;
    }

    public String toString()
    {
        return "Student[name = " + getName() + ", birth year = " + getBirthYear() + ", ID = " + this.ID + ", score = " + this.score + "]";
    }
}