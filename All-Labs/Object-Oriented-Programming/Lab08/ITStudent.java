public class ITStudent extends StudentB3
{
    private int ID;

    public ITStudent()
    {
        super();
        this.ID = 0;
    }

    public ITStudent(int ID, String name, double gpa)
    {
        super(name, gpa);
        this.ID = ID;
    }

    public int getID()
    {
        return this.ID;
    }

    public void setID(int ID)
    {
        this.ID = ID;
    }

    public String getRank()
    {
        double gpa = getGPA();
        if(gpa > 8 && gpa <= 10)
            return "A";
        else if(gpa > 5 && gpa <= 8)
            return "B";
        return "C";
    }

    public String toString()
    {
        return "ITStudent[name = " + getName() + ", ID = " + this.ID + ", GPA = " + getGPA() + ", rank = " + getRank() + "]";
    }
}