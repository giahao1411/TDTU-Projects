public class MathStudent extends StudentB3
{
    private String ID;

    public MathStudent()
    {
        super();
        this.ID = "";
    }

    public MathStudent(String ID, String name, double gpa)
    {
        super(name, gpa);
        this.ID = ID;
    }

    public String getID()
    {
        return this.ID;
    }

    public void setID(String ID)
    {
        this.ID = ID;
    }

    public String getRank()
    {
        double gpa = getGPA();
        if(gpa >= 5)
            return "Passed";
        return "Failed";
    }

    public String toString()
    {
        return "MathStudent[name = " + getName() + ", ID = " + this.ID + ", GPA = " + getGPA() + ", rank = " + getRank() + "]";
    }
}